"""HR dashboard: read-only analytics built from the employee database.

Access follows the rest of the app and is re-checked against the database on every call:
  * hr_admin -> whole organisation, grouped by department
  * manager  -> own direct reports only, grouped by person
  * employee -> no dashboard
Only aggregates are shown. No salary, address, phone or leave *type* ever reaches the page.
"""
from __future__ import annotations

import calendar
import html
from datetime import date, timedelta
from typing import Optional

import hr_data
import hr_security as sec

WEEK_OPTIONS = ("This week", "Next week", "Last week")
_WEEK_OFFSET = {"This week": 0, "Next week": 1, "Last week": -1}
_DAY_NAMES = ("Mon", "Tue", "Wed", "Thu", "Fri")
_LEVEL_COLORS = ("#0e3b37", "#0f5f58", "#0f8a7e", "#1fb8a8", "#5eead4")


# --------------------------------------------------------------------------- access
def dashboard_role(actor_id: str) -> Optional[str]:
    """'hr_admin' or 'manager' when this person may open the dashboard, else None (re-read from the DB)."""
    u = sec.get_user(actor_id)
    if u and u["active"] and u["role"] in ("hr_admin", "manager"):
        return u["role"]
    return None


# --------------------------------------------------------------------------- data
def _short_name(full: str) -> str:
    parts = full.split()
    if len(parts) < 2:
        return full
    return f"{parts[0]} {parts[-1][0]}."


def collect(actor_id: str, week_label: str = "This week") -> Optional[dict]:
    role = dashboard_role(actor_id)
    if role is None:
        sec.audit(actor_id, "dashboard_view", outcome="denied")
        return None

    t = hr_data.today()
    monday = t - timedelta(days=t.weekday()) + timedelta(days=7 * _WEEK_OFFSET.get(week_label, 0))
    week_days = [monday + timedelta(days=i) for i in range(5)]
    m_start = t.replace(day=1)
    m_end = t.replace(day=calendar.monthrange(t.year, t.month)[1])
    prev_end = m_start - timedelta(days=1)
    prev_start = prev_end.replace(day=1)
    year_start = date(t.year, 1, 1)
    window_start = min(year_start, prev_start, monday)

    scope_sql = " AND a.manager_id = ?" if role == "manager" else ""
    scope_args = (actor_id,) if role == "manager" else ()

    with hr_data.hr_conn() as conn:
        people = conn.execute(
            "SELECT a.employee_id, a.name, COALESCE(p.department, 'Unassigned'), p.hire_date "
            "FROM auth.employees a LEFT JOIN employee_profile p ON p.employee_id = a.employee_id "
            "WHERE a.active = 1" + scope_sql + " ORDER BY a.name", scope_args).fetchall()
        leave = conn.execute(
            "SELECT l.employee_id, l.start_date, l.end_date, l.days, l.status "
            "FROM leave_requests l JOIN auth.employees a ON a.employee_id = l.employee_id "
            "WHERE a.active = 1" + scope_sql + " AND l.end_date >= ?",
            scope_args + (window_start.isoformat(),)).fetchall()

    # group key / label for heatmap rows and bars
    group_of, labels = {}, {}
    new_hires, hire_cutoff = 0, t - timedelta(days=30)
    for eid, name, dept, hired in people:
        key = dept if role == "hr_admin" else eid
        group_of[eid] = key
        labels[key] = dept if role == "hr_admin" else _short_name(name)
        if hired:
            try:
                if date.fromisoformat(hired) >= hire_cutoff:
                    new_hires += 1
            except ValueError:
                pass
    group_keys = sorted(labels, key=lambda k: labels[k].lower())

    req_this_month = req_prev_month = 0
    pending_total = pending_soon = 0
    on_leave_today = set()
    heat = {k: [0, 0, 0, 0, 0] for k in group_keys}
    days_by_group = {k: 0.0 for k in group_keys}

    for eid, s, e, days, status in leave:
        try:
            sd, ed = date.fromisoformat(s), date.fromisoformat(e)
        except ValueError:
            continue
        key = group_of.get(eid)
        if key is None:
            continue
        if status != "cancelled":
            if m_start <= sd <= m_end:
                req_this_month += 1
            elif prev_start <= sd <= prev_end:
                req_prev_month += 1
        if status == "pending" and not (role == "hr_admin" and eid == actor_id):
            if ed >= t:
                pending_total += 1
                if sd <= t + timedelta(days=7):
                    pending_soon += 1
        if status == "approved":
            if sd <= t <= ed:
                on_leave_today.add(eid)
            if sd.year == t.year:
                days_by_group[key] += float(days or 0)
            i = 0
            while i < 5:
                if sd <= week_days[i] <= ed:
                    heat[key][i] += 1
                i += 1

    headcount = len(people)
    mom = None
    if req_prev_month > 0:
        mom = (req_this_month - req_prev_month) / req_prev_month * 100.0

    return {
        "role": role, "today": t, "year": t.year,
        "headcount": headcount, "new_hires": new_hires,
        "req_this_month": req_this_month, "req_mom": mom,
        "pending": pending_total, "pending_soon": pending_soon,
        "on_leave": len(on_leave_today),
        "on_leave_pct": (len(on_leave_today) / headcount * 100.0) if headcount else 0.0,
        "week_days": week_days, "week_label": week_label,
        "groups": [(k, labels[k]) for k in group_keys],
        "heat": heat, "days_by_group": days_by_group,
    }


# --------------------------------------------------------------------------- html
def _svg(inner: str, size: int = 18) -> str:
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{inner}</svg>')


_IC_USERS = ('<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/>'
             '<path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>')
_IC_CAL = '<rect width="18" height="18" x="3" y="4" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>'
_IC_CLOCK = '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>'
_IC_AWAY = ('<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/>'
            '<path d="M17 11h5"/>')
_ARROW_UP = '<path d="M12 19V5M5 12l7-7 7 7"/>'
_ARROW_DOWN = '<path d="M12 5v14M19 12l-7 7-7-7"/>'


def _delta(direction: str, text: str) -> str:
    if direction == "up":
        badge = f'<span class="db-arrow up">{_svg(_ARROW_UP, 10)}</span>'
    elif direction == "down":
        badge = f'<span class="db-arrow down">{_svg(_ARROW_DOWN, 10)}</span>'
    else:
        badge = '<span class="db-arrow flat"></span>'
    return f'<div class="db-stat-sub">{badge}<span>{html.escape(text)}</span></div>'


def _stat(icon: str, name: str, value: str, sub_html: str, hero: bool = False) -> str:
    cls = "db-card db-stat hero" if hero else "db-card db-stat"
    return (f'<div class="{cls}"><div class="db-stat-head"><span class="db-ic">{_svg(icon)}</span>'
            f'<span class="db-stat-name">{html.escape(name)}</span></div>'
            f'<div class="db-stat-val">{html.escape(value)}</div>{sub_html}</div>')


def _nice_step(max_val: float) -> float:
    """Smallest 'round' step such that five steps cover max_val."""
    if max_val <= 0:
        return 1.0
    base = 1.0
    while True:
        for mult in (1, 2, 2.5, 5):
            step = base * mult
            if step * 5 >= max_val:
                return step
        base *= 10


def _fmt_num(v: float) -> str:
    return f"{v:g}"


def _heatmap(d: dict) -> str:
    wd, today = d["week_days"], d["today"]
    top = max([max(row) for row in d["heat"].values()] + [0])
    cols = "".join(f'<div class="hm-col">{n}</div>' for n in _DAY_NAMES)
    body = []
    for key, label in d["groups"]:
        cells = []
        i = 0
        while i < 5:
            c = d["heat"][key][i]
            level = 0 if c == 0 or top == 0 else min(5, max(1, -(-c * 5 // top)))
            style = f' style="background:{_LEVEL_COLORS[level - 1]}"' if level else ""
            cls = f"hm-cell l{level}" + (" today" if wd[i] == today else "")
            tip = f"{label} · {_DAY_NAMES[i]} {wd[i].strftime('%d %b')}: {c} on leave"
            cells.append(f'<div class="{cls}"{style} title="{html.escape(tip)}">{c if c else ""}</div>')
            i += 1
        body.append(f'<div class="hm-label" title="{html.escape(label)}">{html.escape(label)}</div>' + "".join(cells))
    if not body:
        body.append('<div class="db-empty" style="grid-column:1/-1">No people in scope yet.</div>')
    rng = f"{wd[0].strftime('%d %b')} – {wd[4].strftime('%d %b')}"
    legend = "".join(f'<i style="background:{c}"></i>' for c in _LEVEL_COLORS)
    return (f'<div class="db-card db-heat"><div class="db-card-head"><div><div class="db-card-title">Leave overview</div>'
            f'<div class="db-card-sub">People on approved leave · {html.escape(rng)}</div></div></div>'
            f'<div class="hm-grid"><div></div>{cols}{"".join(body)}</div>'
            f'<div class="hm-legend"><span>Fewer</span>{legend}<span>More</span></div></div>')


def _bars(d: dict) -> str:
    groups = d["groups"]
    vals = [d["days_by_group"][k] for k, _ in groups]
    total = sum(vals)
    top = max(vals + [0.0])
    step = _nice_step(top)
    ymax = step * 5
    peak = vals.index(top) if (vals and top > 0) else -1

    grid = "".join(
        f'<div class="bc-gl" style="bottom:{n * 20}%"><span>{_fmt_num(step * n)}</span></div>' for n in range(6))
    cols, labs = [], []
    i = 0
    for key, label in groups:
        v = vals[i]
        h = (v / ymax * 100.0) if ymax else 0.0
        pct = (v / total * 100.0) if total else 0.0
        cls = "bc-bar hi" if i == peak else "bc-bar"
        cols.append(f'<div class="bc-col" title="{html.escape(label)}: {_fmt_num(v)} days">'
                    f'<div class="bc-pct" style="bottom:calc({h:.2f}% + 8px)">{pct:.0f}%</div>'
                    f'<div class="{cls}" style="height:{h:.2f}%"></div></div>')
        labs.append(f'<div class="bc-lab" title="{html.escape(label)}">{html.escape(label)}</div>')
        i += 1
    if not groups:
        return ('<div class="db-card db-bars"><div class="db-card-title">Leave usage</div>'
                '<div class="db-empty">No data yet.</div></div>')
    unit = "department" if d["role"] == "hr_admin" else "person"
    return (f'<div class="db-card db-bars"><div class="db-card-head"><div><div class="db-card-title">Leave usage</div>'
            f'<div class="db-card-sub">Approved leave days by {unit}, {d["year"]} to date · share of total</div></div></div>'
            f'<div class="bc-plot">{grid}<div class="bc-cols">{"".join(cols)}</div></div>'
            f'<div class="bc-labs">{"".join(labs)}</div></div>')


def build_html(d: dict) -> str:
    """One markdown-safe HTML string: no blank lines and no indentation."""
    new_h = d["new_hires"]
    c1 = _stat(_IC_USERS, "Total employees" if d["role"] == "hr_admin" else "Team members", f'{d["headcount"]:,}',
               _delta("up" if new_h else "flat", f"{new_h} joined in the last 30 days"), hero=True)

    mom = d["req_mom"]
    if mom is None:
        sub2 = _delta("flat", "No requests last month to compare")
    else:
        sub2 = _delta("up" if mom >= 0 else "down", f"{abs(mom):.0f}% vs last month")
    c2 = _stat(_IC_CAL, "Leave requests", f'{d["req_this_month"]:,}', sub2)

    soon = d["pending_soon"]
    c3 = _stat(_IC_CLOCK, "Pending approvals", f'{d["pending"]:,}',
               _delta("flat", f"{soon} starting within 7 days" if soon else "None starting within 7 days"))

    c4 = _stat(_IC_AWAY, "On leave today", f'{d["on_leave"]:,}',
               _delta("flat", f'{d["on_leave_pct"]:.1f}% of the workforce'))

    return (f'<div class="db-wrap"><div class="db-top"><div class="db-stats">{c1}{c2}{c3}{c4}</div>'
            f'{_heatmap(d)}</div>{_bars(d)}</div>')
