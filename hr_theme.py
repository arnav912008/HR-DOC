"""Dark teal design language for the HR Assistant (login, chat and dashboard).

Palette
  page      #050708   surface #0b0f11   raised #10161a   border rgba(255,255,255,.07)
  text      #e8eef0   muted   #8b979c   dim    #5d6a70
  accent    #2dd4bf (bright)  #14b8a6 (base)  #0f9d8f (deep)
"""

BASE_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

html, body, .stApp, .stApp p, .stApp label, .stApp button, .stApp input,
.stApp textarea, .stApp li, .stApp div, .stApp h1, .stApp h2, .stApp h3, .stApp h4 {
    font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', sans-serif !important;
    -webkit-font-smoothing: antialiased;
}
html, body { background: #050708 !important; color-scheme: dark; }
.stApp { color: #e8eef0; color-scheme: dark;
    background: radial-gradient(900px 520px at 78% -8%, rgba(20,184,166,0.12), transparent 62%),
                radial-gradient(700px 480px at 0% 100%, rgba(20,184,166,0.05), transparent 60%), #050708 !important; }
header[data-testid="stHeader"], header[data-testid="stHeader"]::before, header[data-testid="stHeader"]::after {
    background: transparent !important; background-image: none !important; border: 0 !important; box-shadow: none !important; }
#MainMenu, [data-testid="stMainMenu"], footer, [data-testid="stDecoration"], #stDecoration { display: none !important; }
[data-testid="stToolbar"] button, [data-testid="stToolbar"] a, [data-testid="stAppDeployButton"] button { color: #8b979c !important; font-size: 14px; font-weight: 500; }

::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: #1d2529; border-radius: 9999px; }
::-webkit-scrollbar-thumb:hover { background: #2a343a; }

@keyframes fadeInUp { 0% { opacity: 0; transform: translateY(12px); } 100% { opacity: 1; transform: translateY(0); } }
@keyframes fadeInSidebar { 0% { opacity: 0; transform: translateX(-8px); } 100% { opacity: 1; transform: translateX(0); } }
@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after { animation-duration: 0.01ms !important; animation-iteration-count: 1 !important;
                              transition-duration: 0.01ms !important; scroll-behavior: auto !important; }
}

/* shared small text styles */
.hr-eyebrow { font-size: 11px; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; color: #6f7d83; line-height: 16.5px; }
.hr-eyebrow.light { color: #6f7d83; }
.hr-muted { font-size: 13px; color: #8b979c; line-height: 20px; }
.hr-mark { display: inline-flex; align-items: center; justify-content: center; flex: 0 0 auto; width: 40px; height: 40px; border-radius: 12px;
           background: linear-gradient(145deg, #2dd4bf, #0f9d8f); color: #021412; font-size: 17px; font-weight: 700; letter-spacing: -0.02em;
           box-shadow: 0 6px 20px rgba(20,184,166,0.28); }
.hr-mark.sm { width: 32px; height: 32px; border-radius: 10px; font-size: 14px; }

/* generic controls (zero specificity; the keyed rules below win) */
:where(.stApp) :where([data-testid^="stBaseButton-secondary"]) { background: #10161a !important; color: #e8eef0 !important; border: 1px solid rgba(255,255,255,0.08) !important; border-radius: 10px !important; }
:where(.stApp) :where([data-testid^="stBaseButton-secondary"]:hover) { background: #151d22 !important; border-color: rgba(45,212,191,0.35) !important; }
[data-testid="stTextInputRootElement"], div[data-baseweb="input"] { background: #0b0f11 !important; border: 1px solid rgba(255,255,255,0.09) !important;
    border-radius: 10px !important; box-shadow: none; min-height: 0; transition: all .15s ease-in-out; }
div[data-baseweb="input"]:not([data-testid="stTextInputRootElement"]) { border: 0 !important; background: transparent !important; }
[data-testid="stTextInputRootElement"]:focus-within { border-color: #2dd4bf !important; box-shadow: 0 0 0 3px rgba(45,212,191,0.16) !important; }
div[data-baseweb="base-input"], div[data-baseweb="base-input"] > div { background: transparent !important; border: 0 !important; }
[data-testid="stTextInputRootElement"] input { padding: 11px 14px !important; font-size: 14px !important; line-height: 20px; color: #e8eef0 !important;
    background: transparent !important; -webkit-text-fill-color: #e8eef0; caret-color: #2dd4bf; }
[data-testid="stTextInputRootElement"] button { color: #8b979c !important; background: transparent !important; border: 0 !important; }
[data-testid="stTextInputRootElement"] button svg { color: #8b979c !important; fill: currentColor; }
[data-testid="stWidgetLabel"] { min-height: 0; margin: 0; }
[data-testid="stWidgetLabel"] p { font-size: 13px !important; font-weight: 500 !important; line-height: 20px; color: #b4c0c5 !important; margin: 0; }
[data-testid="stTextInput"] { gap: 6px !important; }
[data-testid="stForm"] { border: 0 !important; padding: 0 !important; background: transparent !important; }
[data-testid="stFormSubmitButton"] button { min-height: 0; padding: 11px 16px; border-radius: 10px; border: 0 !important;
    background: linear-gradient(180deg, #2dd4bf, #14b8a6) !important; box-shadow: 0 6px 18px rgba(20,184,166,0.22); transition: all .15s; }
[data-testid="stFormSubmitButton"] button:hover { filter: brightness(1.06); transform: translateY(-1px); }
[data-testid="stFormSubmitButton"] button, [data-testid="stFormSubmitButton"] button * { color: #021412 !important; font-size: 14px; font-weight: 600; }
[data-testid="stAlert"] { border-radius: 12px; }
[data-testid="stToast"] { background: #10161a !important; border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; }
[data-testid="stToast"] * { color: #e8eef0 !important; }
"""

LOGIN_CSS = """
.stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"] { background: transparent !important; }
.block-container, [data-testid="stMainBlockContainer"] { max-width: none !important; width: 100% !important; margin: 0 !important; padding: 0 !important; }
[data-testid="stMainBlockContainer"] > [data-testid="stVerticalBlock"] { gap: 0 !important; }

/* right-hand brand panel */
.st-key-login_panel, .st-key-login_panel > [data-testid="stVerticalBlock"] { height: 0; min-height: 0; overflow: visible; }
.hr-lg-panel { position: fixed; top: 16px; right: 16px; bottom: 16px; width: calc(50vw - 24px); z-index: 1; border-radius: 20px; overflow: hidden;
    border: 1px solid rgba(255,255,255,0.07);
    background-color: #07211f;
    background-image: radial-gradient(520px 420px at 85% 10%, rgba(45,212,191,0.28), transparent 65%),
        radial-gradient(420px 360px at 0% 100%, rgba(20,184,166,0.16), transparent 70%),
        url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='640' height='640' viewBox='0 0 640 640' fill='none' stroke='%232dd4bf' stroke-opacity='0.14'%3E%3Ccircle cx='560' cy='80' r='120'/%3E%3Ccircle cx='560' cy='80' r='200'/%3E%3Ccircle cx='560' cy='80' r='280'/%3E%3Ccircle cx='560' cy='80' r='360'/%3E%3Ccircle cx='560' cy='80' r='440'/%3E%3C/svg%3E");
    background-repeat: no-repeat; background-position: top right; background-size: auto, auto, 640px; }
.hr-lg-panel-inner { box-sizing: border-box; height: 100%; width: 100%; padding: clamp(28px, 4vw, 56px); display: flex; flex-direction: column; justify-content: space-between; }
.hr-lg-chip { align-self: flex-start; padding: 6px 12px; border: 1px solid rgba(45,212,191,0.35); border-radius: 9999px; font-size: 11px; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; color: #99f6e4; background: rgba(45,212,191,0.08); }
.hr-lg-h { max-width: 30rem; font-size: clamp(28px, 2.6vw, 40px); line-height: 1.2; font-weight: 700; letter-spacing: -0.025em; color: #f1fbfa; }
.hr-lg-p { max-width: 27rem; margin-top: 16px; font-size: 16px; line-height: 1.6; color: rgba(225,245,242,0.72); }
.hr-lg-topics { display: flex; flex-wrap: wrap; gap: 8px; max-width: 30rem; margin-top: 28px; }
.hr-lg-topics span { padding: 6px 12px; border: 1px solid rgba(255,255,255,0.12); border-radius: 9999px; background: rgba(255,255,255,0.05); font-size: 13px; color: #d5ece8; }
.hr-lg-card { display: flex; align-items: center; gap: 14px; padding: 14px 16px; max-width: 30rem; border: 1px solid rgba(255,255,255,0.1); border-radius: 14px; background: rgba(0,0,0,0.28); }
.hr-lg-card-dot { flex: 0 0 auto; width: 36px; height: 36px; border-radius: 50%; background: rgba(45,212,191,0.18); position: relative; }
.hr-lg-card-dot::after { content: ""; position: absolute; inset: 12px; border-radius: 50%; background: #2dd4bf; }
.hr-lg-card-title { font-size: 13px; font-weight: 600; line-height: 1.4; color: #f1fbfa; }
.hr-lg-card-sub { margin-top: 2px; font-size: 12px; line-height: 1.5; color: rgba(225,245,242,0.64); }

/* left-hand sign-in column */
.st-key-login_left, .st-key-login_left > [data-testid="stVerticalBlock"] { display: flex; flex-direction: column; justify-content: space-between; min-height: 100vh; gap: 0 !important; }
.st-key-login_left { width: 50vw; max-width: 50vw; margin: 0; padding: 0 max(24px, calc((50vw - 28rem) / 2)); box-sizing: border-box; }
.hr-lg-brand { display: flex; align-items: center; gap: 10px; height: 88px; font-size: 16px; font-weight: 700; letter-spacing: -0.01em; color: #f1f5f6; }
.hr-lg-foot { display: flex; align-items: center; height: 88px; font-size: 12px; color: #5d6a70; }
.st-key-login_zone, .st-key-login_zone > [data-testid="stVerticalBlock"] { gap: 0 !important; }
.hr-lg-eyebrow { font-size: 11px; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; color: #2dd4bf; }
.hr-lg-title { margin-top: 8px; font-size: 30px; line-height: 38px; font-weight: 700; letter-spacing: -0.025em; color: #f1f5f6; }
.hr-lg-sub { margin: 8px 0 28px; font-size: 14px; line-height: 20px; color: #8b979c; }
[data-testid="stForm"] [data-testid="stVerticalBlock"] { gap: 20px; }
[data-testid="stFormSubmitButton"], [data-testid="stForm"] [data-testid="stElementContainer"]:has([data-testid="stFormSubmitButton"]),
[data-testid="stForm"] .stElementContainer:has([data-testid="stFormSubmitButton"]) { margin-top: 8px; width: 100% !important; }
[data-testid="stFormSubmitButton"] button { width: 100% !important; justify-content: center; }

@media (max-width: 899px) {
    .hr-lg-panel { display: none; }
    .st-key-login_left { width: 100%; max-width: 100%; padding: 0 24px; }
}
"""

MAIN_CSS = """
.stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"] { background: transparent !important; }

/* ---------- Sidebar ---------- */
section[data-testid="stSidebar"] { background: #070a0c !important; border-right: 1px solid rgba(255,255,255,0.06);
    width: 20rem !important; min-width: 20rem !important; max-width: 20rem !important;
    transform: none !important; margin-left: 0 !important; visibility: visible !important; }
section[data-testid="stSidebar"] > div:first-child { background: #070a0c !important; width: 100% !important; }
[data-testid="stSidebarHeader"], [data-testid="stSidebarCollapseButton"], [data-testid="stSidebarCollapsedControl"],
[data-testid="collapsedControl"], [data-testid="stExpandSidebarButton"], [data-testid="stSidebarResizeHandle"] { display: none !important; }
[data-testid="stSidebarContent"] { padding: 0 !important; }
[data-testid="stSidebarUserContent"] { padding: 26px 22px 96px !important; animation: fadeInSidebar .5s cubic-bezier(.16,1,.3,1) 50ms backwards; }
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p { margin: 0 !important; }

.st-key-side_root, .st-key-side_root > [data-testid="stVerticalBlock"] { display: flex; flex-direction: column; gap: 24px !important; }
.st-key-side_root > [data-testid="stVerticalBlock"] { flex: 1 1 auto; }
.st-key-side_root > *, .st-key-side_root > [data-testid="stVerticalBlock"] > * { animation: fadeInUp .5s cubic-bezier(.16,1,.3,1) backwards; }

.hr-brandrow { display: flex; align-items: center; gap: 12px; padding-bottom: 18px; border-bottom: 1px solid rgba(255,255,255,0.06); }
.hr-brand-title { font-size: 17px; line-height: 1.3; font-weight: 700; letter-spacing: -0.02em; color: #f1f5f6; }
.hr-brand-sub { font-size: 12px; line-height: 16px; font-weight: 500; color: #6f7d83; }
.hr-user-name { font-size: 14px; line-height: 1.25; font-weight: 600; color: #e8eef0; }
.hr-user-role { margin-top: 2px; font-size: 12px; line-height: 16px; color: #6f7d83; }

.st-key-side_nav, .st-key-side_nav > [data-testid="stVerticalBlock"] { gap: 4px !important; }
.st-key-side_recent, .st-key-side_recent > [data-testid="stVerticalBlock"] { gap: 6px !important; }
.st-key-side_cats, .st-key-side_cats > [data-testid="stVerticalBlock"] { gap: 8px !important; }
.st-key-side_nav .hr-eyebrow, .st-key-side_cats .hr-eyebrow, .st-key-side_recent .hr-eyebrow { padding-bottom: 8px; }
.st-key-side_cats { margin-top: 6px; }
.st-key-side_footer { position: fixed !important; left: 0; bottom: 0; z-index: 20; box-sizing: border-box; width: 20rem; margin: 0 !important;
    padding: 14px 22px 18px; background: #070a0c; border-top: 1px solid rgba(255,255,255,0.06); }
.st-key-side_footer [data-testid="stHorizontalBlock"] { flex-wrap: nowrap !important; align-items: center; gap: 8px !important; }
.st-key-side_footer [data-testid="stColumn"], .st-key-side_footer [data-testid="column"] { min-width: 0 !important; width: auto !important; }
.st-key-side_footer [data-testid="stColumn"]:last-child, .st-key-side_footer [data-testid="column"]:last-child { flex: 0 0 auto !important; display: flex; justify-content: flex-end; }
.st-key-side_footer [data-testid="stColumn"]:first-child, .st-key-side_footer [data-testid="column"]:first-child { flex: 1 1 auto !important; overflow: hidden; }
.hr-user-name, .hr-user-role { white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }

/* shared button reset */
.st-key-new_conv button, [class*="st-key-cat_"] button, [class*="st-key-sq_"] button, [class*="st-key-recent_"] button,
[class*="st-key-nav_"] button, .st-key-signout button { min-height: 0; line-height: 20px; transition: all .15s ease-out; }
.st-key-new_conv, [class*="st-key-cat_"], [class*="st-key-sq_"], [class*="st-key-recent_"], [class*="st-key-nav_"] { width: 100% !important; }
.st-key-new_conv button, [class*="st-key-cat_"] button, [class*="st-key-sq_"] button, [class*="st-key-recent_"] button, [class*="st-key-nav_"] button { width: 100%; }
.st-key-new_conv button p, [class*="st-key-cat_"] button p, [class*="st-key-sq_"] button p, [class*="st-key-recent_"] button p,
[class*="st-key-nav_"] button p, .st-key-signout button p { margin: 0 !important; line-height: inherit; }

/* Main-menu navigation (Chat / Dashboard) */
[class*="st-key-nav_"] button { padding: 10px 12px; border: 1px solid transparent !important; border-radius: 12px; background: transparent !important;
    justify-content: flex-start !important; text-align: left; gap: 10px; box-shadow: none; }
[class*="st-key-nav_"] button:hover { background: rgba(255,255,255,0.04) !important; }
[class*="st-key-nav_"] button, [class*="st-key-nav_"] button * { color: #9aa7ac !important; font-size: 14px; font-weight: 500; }
[class*="st-key-nav_"] button:hover, [class*="st-key-nav_"] button:hover * { color: #e8eef0 !important; }
.st-key-nav_chat_on button, .st-key-nav_dash_on button { background: linear-gradient(180deg, rgba(255,255,255,0.085), rgba(255,255,255,0.025)) !important;
    border-color: rgba(255,255,255,0.08) !important; box-shadow: inset 0 1px 0 rgba(255,255,255,0.05); }
.st-key-nav_chat_on button, .st-key-nav_chat_on button *, .st-key-nav_dash_on button, .st-key-nav_dash_on button * { color: #ffffff !important; }
[class*="st-key-nav_"] button [data-testid="stIconMaterial"] { font-size: 20px; }
[class*="st-key-nav_"] button > div { justify-content: flex-start !important; width: 100%; }

/* New conversation */
.st-key-new_conv button { padding: 10px 20px; border: 0 !important; border-radius: 12px; background: linear-gradient(180deg, #2dd4bf, #14b8a6) !important; box-shadow: 0 6px 18px rgba(20,184,166,0.22); }
.st-key-new_conv button:hover { filter: brightness(1.07); transform: translateY(-1px); }
.st-key-new_conv button:active { transform: translateY(0) scale(0.98); }
.st-key-new_conv button, .st-key-new_conv button * { color: #021412 !important; font-size: 14px; font-weight: 600; }

/* Category buttons, recent items, sign out */
[class*="st-key-cat_"] button, .st-key-signout button { padding: 8px 14px; border: 1px solid rgba(255,255,255,0.07) !important; border-radius: 10px; background: #0b0f11 !important;
    box-shadow: none; justify-content: flex-start; text-align: left; }
[class*="st-key-cat_"] button:hover, .st-key-signout button:hover { background: #10161a !important; border-color: rgba(45,212,191,0.35) !important; }
[class*="st-key-cat_"] button, [class*="st-key-cat_"] button * { color: #b4c0c5 !important; font-size: 14px; font-weight: 500; }
[class*="st-key-cat_"] button:hover, [class*="st-key-cat_"] button:hover * { color: #f1f5f6 !important; }
.st-key-signout button { padding: 6px 14px; width: auto; }
.st-key-signout button, .st-key-signout button * { color: #b4c0c5 !important; font-size: 12px; font-weight: 500; }
.st-key-signout button:active { transform: scale(0.95); }

[class*="st-key-recent_"] button { padding: 6px 8px; border: 0 !important; border-radius: 8px; background: transparent !important; justify-content: flex-start; text-align: left; }
[class*="st-key-recent_"] button:hover { background: rgba(255,255,255,0.05) !important; }
[class*="st-key-recent_"] button, [class*="st-key-recent_"] button * { color: #9aa7ac !important; font-size: 14px; font-weight: 400; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }

[class*="st-key-cat_"] button > div, [class*="st-key-sq_"] button > div, [class*="st-key-recent_"] button > div,
[class*="st-key-cat_"] [data-testid="stMarkdownContainer"], [class*="st-key-sq_"] [data-testid="stMarkdownContainer"], [class*="st-key-recent_"] [data-testid="stMarkdownContainer"] {
    width: 100%; justify-content: flex-start !important; text-align: left !important; }
[class*="st-key-cat_"] button p, [class*="st-key-sq_"] button p, [class*="st-key-recent_"] button p { text-align: left !important; width: 100%; }
[class*="st-key-cat_"] button, [class*="st-key-sq_"] button, [class*="st-key-recent_"] button { justify-content: flex-start !important; }
.st-key-new_conv button, .st-key-new_conv button > div { justify-content: center !important; text-align: center; }

/* Admin / account panels */
[data-testid="stSidebar"] [data-testid="stExpander"] { border: 1px solid rgba(255,255,255,0.07) !important; border-radius: 12px; background: #0b0f11; }
[data-testid="stSidebar"] [data-testid="stExpander"] details { border: 0 !important; background: transparent; }
[data-testid="stSidebar"] [data-testid="stExpander"] summary { padding: 8px 14px; }
[data-testid="stSidebar"] [data-testid="stExpander"] summary p, [data-testid="stSidebar"] [data-testid="stExpander"] summary span { color: #b4c0c5 !important; font-size: 14px; font-weight: 500; }
[data-testid="stSidebar"] [data-testid="stExpander"] [data-testid="stExpanderDetails"], [data-testid="stSidebar"] [data-testid="stExpander"] details > div:last-child { padding: 4px 14px 16px; }
[data-testid="stSidebar"] [data-testid="stExpander"] [data-testid="stVerticalBlock"] { gap: 12px; }
.hr-admin-note { font-size: 12px; line-height: 1.5; color: #7d8a90; }
.hr-admin-meta { font-size: 12px; line-height: 1.5; color: #9aa7ac; }
.hr-admin-meta b { color: #e8eef0; font-weight: 600; }
[data-testid="stFileUploader"] label p { font-size: 12px !important; font-weight: 500; color: #b4c0c5 !important; }
[data-testid="stFileUploaderDropzone"] { background: #0b0f11 !important; border: 1px dashed rgba(255,255,255,0.14) !important; border-radius: 10px; padding: 10px 12px; }
[data-testid="stFileUploaderDropzone"] *, [data-testid="stFileUploader"] small { color: #9aa7ac !important; font-size: 12px; }
[data-testid="stFileUploaderDropzone"] button { background: #10161a !important; border: 1px solid rgba(255,255,255,0.09) !important; border-radius: 8px; padding: 4px 12px; min-height: 0; }
[class*="st-key-admin_"] { width: 100% !important; }
[class*="st-key-admin_"] button { width: 100%; min-height: 0; padding: 8px 16px; line-height: 20px; border-radius: 10px; justify-content: center !important; transition: all .15s ease-out; }
[class*="st-key-admin_"] button p { margin: 0 !important; font-size: 14px; font-weight: 500; }
.st-key-admin_download button, .st-key-admin_rebuild button, .st-key-admin_mfa_start button { background: #10161a !important; border: 1px solid rgba(255,255,255,0.09) !important; }
.st-key-admin_download button:hover, .st-key-admin_rebuild button:hover, .st-key-admin_mfa_start button:hover { border-color: rgba(45,212,191,0.4) !important; }
.st-key-admin_download button, .st-key-admin_download button *, .st-key-admin_rebuild button, .st-key-admin_rebuild button *,
.st-key-admin_mfa_start button, .st-key-admin_mfa_start button * { color: #d5dde0 !important; }
.st-key-admin_replace button { background: linear-gradient(180deg, #2dd4bf, #14b8a6) !important; border: 0 !important; }
.st-key-admin_replace button:hover:not(:disabled) { filter: brightness(1.07); }
.st-key-admin_replace button, .st-key-admin_replace button * { color: #021412 !important; font-weight: 600; }
[class*="st-key-admin_"] button:disabled { opacity: .45; cursor: not-allowed; }
button:focus:not(:active) { border-color: inherit; }

/* ---------- Main area ---------- */
.block-container, [data-testid="stMainBlockContainer"] { max-width: none !important; padding: 0 36px 7rem !important; }
[data-testid="stMainBlockContainer"] > [data-testid="stVerticalBlock"] { gap: 0 !important; }

.hr-main-head { display: flex; align-items: center; justify-content: space-between; gap: 24px; margin: 0 -36px; padding: 22px 120px 22px 36px;
                border-bottom: 1px solid rgba(255,255,255,0.06); animation: fadeInUp .5s cubic-bezier(.16,1,.3,1) 150ms both; }
.hr-main-brand { display: flex; align-items: center; gap: 14px; }
.hr-main-title { font-size: 20px; line-height: 28px; font-weight: 600; letter-spacing: -0.02em; color: #f1f5f6; }
.hr-main-sub { margin-top: 1px; font-size: 13px; line-height: 20px; color: #8b979c; }
.hr-main-note { max-width: 22rem; text-align: right; }
.hr-main-note-label { font-size: 11px; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; color: #5d6a70; }
.hr-main-note-text { margin-top: 2px; font-size: 13px; line-height: 1.5; color: #8b979c; }
.hr-chip { display: inline-flex; align-items: center; gap: 8px; padding: 7px 14px; border: 1px solid rgba(255,255,255,0.09); border-radius: 9999px;
           background: rgba(255,255,255,0.03); font-size: 13px; color: #b4c0c5; white-space: nowrap; }
.hr-chip i { width: 7px; height: 7px; border-radius: 50%; background: #2dd4bf; box-shadow: 0 0 10px rgba(45,212,191,0.8); }
@media (max-width: 1023px) { .hr-main-note { display: none; } }

.st-key-body { max-width: 944px; padding-top: 36px; }
.st-key-body, .st-key-body > [data-testid="stVerticalBlock"] { gap: 0 !important; }
.hr-welcome { margin-bottom: 36px; animation: fadeInUp .5s cubic-bezier(.16,1,.3,1) 220ms both; }
.hr-welcome-title { font-size: 22px; line-height: 30px; font-weight: 600; letter-spacing: -0.02em; color: #f1f5f6; }
.hr-welcome-text { margin-top: 8px !important; font-size: 14px; line-height: 1.625; color: #8b979c; }
.hr-sq-label { padding-bottom: 14px; animation: fadeInUp .5s cubic-bezier(.16,1,.3,1) 280ms both; }

.st-key-sq_wrap { max-width: 768px; }
.st-key-sq_wrap, .st-key-sq_wrap > [data-testid="stVerticalBlock"] { gap: 14px !important; }
.st-key-sq_wrap [data-testid="stHorizontalBlock"] { gap: 14px !important; }
[class*="st-key-sq_"]:not(.st-key-sq_wrap) { animation: fadeInUp .5s cubic-bezier(.16,1,.3,1) both; }
.st-key-sq_1 { animation-delay: 340ms !important; } .st-key-sq_2 { animation-delay: 400ms !important; }
.st-key-sq_3 { animation-delay: 460ms !important; } .st-key-sq_4 { animation-delay: 520ms !important; }
[class*="st-key-sq_"] button { padding: 16px; border: 1px solid rgba(255,255,255,0.07) !important; border-radius: 16px;
    background: linear-gradient(180deg, rgba(255,255,255,0.05), rgba(255,255,255,0.015)), #0b0f11 !important;
    justify-content: flex-start; text-align: left; transition-duration: .2s; }
[class*="st-key-sq_"] button:hover { border-color: rgba(45,212,191,0.4) !important; transform: translateY(-2px); box-shadow: 0 10px 30px rgba(0,0,0,0.4), 0 0 0 1px rgba(45,212,191,0.08); }
[class*="st-key-sq_"] button:active { transform: translateY(0); }
[class*="st-key-sq_"] button, [class*="st-key-sq_"] button * { color: #c5d0d4 !important; font-size: 14px; font-weight: 400; }
[class*="st-key-sq_"] button:hover, [class*="st-key-sq_"] button:hover * { color: #ffffff !important; }

/* ---------- Chat messages ---------- */
[data-testid="stChatMessageAvatarUser"], [data-testid="stChatMessageAvatarAssistant"], [data-testid="stChatMessageAvatarCustom"] { display: none !important; }
[data-testid="stChatMessage"] { background: linear-gradient(180deg, rgba(255,255,255,0.045), rgba(255,255,255,0.01)), #0b0f11; border: 1px solid rgba(255,255,255,0.07);
    border-radius: 16px; padding: 14px 18px; margin-bottom: 14px; gap: 0; }
[data-testid="stChatMessage"] p, [data-testid="stChatMessage"] li { font-size: 14px; line-height: 1.65; }
[data-testid="stChatMessage"] p, [data-testid="stChatMessage"] li, [data-testid="stChatMessage"] strong, [data-testid="stChatMessage"] h1,
[data-testid="stChatMessage"] h2, [data-testid="stChatMessage"] h3 { color: #d5dde0; }
div[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]),
div[data-testid="stChatMessage"]:has(div[aria-label="Chat message from user"]) { background: linear-gradient(180deg, rgba(45,212,191,0.20), rgba(20,184,166,0.10)), #0b1715; border-color: rgba(45,212,191,0.30); }
div[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) :is(p, li, strong, span),
div[data-testid="stChatMessage"]:has(div[aria-label="Chat message from user"]) :is(p, li, strong, span) { color: #effffc !important; }
[data-testid="stSpinner"], [data-testid="stSpinner"] * { color: #8b979c !important; font-size: 14px; }

/* ---------- Chat input bar ---------- */
[data-testid="stBottom"], [data-testid="stBottom"] > div, [data-testid="stBottomBlockContainer"] { background: linear-gradient(180deg, rgba(5,7,8,0), #050708 38%) !important; }
[data-testid="stBottomBlockContainer"] { max-width: none !important; padding: 20px 32px 24px !important; }
[data-testid="stChatInput"] { max-width: 64rem; margin: 0 auto; background: transparent !important; animation: fadeInUp .5s cubic-bezier(.16,1,.3,1) 450ms both; }
[data-testid="stChatInput"] > div { background: #0d1215 !important; border: 1px solid rgba(255,255,255,0.09) !important; border-radius: 16px !important;
    box-shadow: 0 10px 30px rgba(0,0,0,0.45); transition: all .2s; }
[data-testid="stChatInput"] > div:hover { border-color: rgba(255,255,255,0.16) !important; }
[data-testid="stChatInput"] > div:focus-within { border-color: #2dd4bf !important; box-shadow: 0 0 0 3px rgba(45,212,191,0.16), 0 10px 30px rgba(0,0,0,0.45) !important; }
[data-testid="stChatInput"] [data-baseweb="textarea"], [data-testid="stChatInput"] [data-baseweb="base-input"] { background: transparent !important; border: 0 !important; }
[data-testid="stChatInput"] textarea { background: transparent !important; color: #e8eef0 !important; -webkit-text-fill-color: #e8eef0; caret-color: #2dd4bf;
    font-size: 14px !important; line-height: 20px; padding: 14px 56px 14px 20px !important; }
[data-testid="stChatInput"] textarea::placeholder { color: #6f7d83 !important; -webkit-text-fill-color: #6f7d83; opacity: 1; }
[data-testid="stChatInputSubmitButton"] { background: #2dd4bf !important; color: #021412 !important; border-radius: 10px !important; transition: all .15s; }
[data-testid="stChatInputSubmitButton"]:hover { background: #5eead4 !important; }
[data-testid="stChatInputSubmitButton"]:disabled { background: #1a2328 !important; color: #5d6a70 !important; opacity: .8; }

/* ---------- Dashboard ---------- */
.st-key-dash_ctl { max-width: 190px; margin-left: auto; padding-top: 22px; }
.st-key-dash_ctl [data-baseweb="select"] div { background: #0b0f11 !important; }
.st-key-dash_ctl [data-baseweb="select"] > div { background: #0b0f11 !important; border: 1px solid rgba(255,255,255,0.09) !important; border-radius: 10px !important; min-height: 38px; }
.st-key-dash_ctl [data-baseweb="select"] * { color: #d5dde0 !important; font-size: 13px; }
.st-key-dash_ctl [data-baseweb="select"] svg { fill: #8b979c !important; }
[data-baseweb="popover"] ul, [data-baseweb="menu"] { background: #10161a !important; }
[data-baseweb="popover"] li { color: #d5dde0 !important; }
[data-baseweb="popover"] li:hover { background: rgba(45,212,191,0.12) !important; }

.db-wrap { display: flex; flex-direction: column; gap: 16px; padding-top: 16px; animation: fadeInUp .5s cubic-bezier(.16,1,.3,1) 120ms both; }
.db-top { display: grid; grid-template-columns: minmax(0, 2fr) minmax(0, 1.15fr); gap: 16px; align-items: stretch; }
.db-stats { display: grid; grid-template-columns: 1fr 1fr; grid-auto-rows: 1fr; gap: 16px; }
@media (max-width: 1100px) { .db-top { grid-template-columns: 1fr; } }
@media (max-width: 640px) { .db-stats { grid-template-columns: 1fr; } }

.db-card { background: #0a0d0f; border: 1px solid rgba(255,255,255,0.07); border-radius: 20px; padding: 20px 22px; box-shadow: inset 0 1px 0 rgba(255,255,255,0.03); }
.db-card-head { display: flex; align-items: flex-start; justify-content: space-between; gap: 12px; }
.db-card-title { font-size: 16px; font-weight: 600; letter-spacing: -0.01em; color: #f1f5f6; }
.db-card-sub { margin-top: 3px; font-size: 12px; color: #6f7d83; }
.db-empty { padding: 28px 0; font-size: 13px; color: #6f7d83; text-align: center; }

.db-stat { display: flex; flex-direction: column; justify-content: center; gap: 16px; min-height: 148px; }
.db-stat.hero { background: linear-gradient(180deg, rgba(255,255,255,0.10), rgba(255,255,255,0) 62%), #0a0d0f; }
.db-stat-head { display: flex; align-items: center; gap: 12px; }
.db-ic { display: inline-flex; align-items: center; justify-content: center; width: 34px; height: 34px; border-radius: 50%; background: #14191c; color: #d5dde0; flex: 0 0 auto; }
.db-stat.hero .db-ic { background: linear-gradient(145deg, #2dd4bf, #0f9d8f); color: #021412; }
.db-stat-name { font-size: 16px; font-weight: 500; color: #eef3f4; }
.db-stat-val { font-size: 34px; line-height: 1.1; font-weight: 500; letter-spacing: -0.02em; color: #ffffff; }
.db-stat-sub { display: flex; align-items: center; gap: 8px; font-size: 13px; color: #9aa7ac; }
.db-arrow { display: inline-flex; align-items: center; justify-content: center; width: 16px; height: 16px; border-radius: 50%; color: #ffffff; flex: 0 0 auto; }
.db-arrow.up { background: #22a447; }
.db-arrow.down { background: #d93636; }
.db-arrow.flat { background: #2dd4bf; width: 8px; height: 8px; margin: 0 4px; opacity: .7; }

.hm-grid { display: grid; grid-template-columns: 86px repeat(5, minmax(0, 1fr)); gap: 8px; margin-top: 18px; align-items: center; }
.hm-col { text-align: center; font-size: 12px; color: #8b979c; }
.hm-label { font-size: 12px; color: #8b979c; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; padding-right: 6px; }
.hm-cell { height: 42px; border-radius: 6px; background: rgba(255,255,255,0.04); display: flex; align-items: center; justify-content: center;
           font-size: 12px; font-weight: 600; color: #d5f7f2; transition: transform .15s; }
.hm-cell:hover { transform: scale(1.06); }
.hm-cell.l4, .hm-cell.l5 { color: #021412; }
.hm-cell.today { outline: 1.5px solid rgba(255,255,255,0.55); outline-offset: 1px; }
.hm-legend { display: flex; align-items: center; justify-content: flex-end; gap: 6px; margin-top: 16px; font-size: 11px; color: #6f7d83; }
.hm-legend i { width: 14px; height: 8px; border-radius: 3px; display: inline-block; }

.bc-plot { position: relative; height: 250px; margin: 34px 0 0 46px; }
.bc-gl { position: absolute; left: 0; right: 0; border-top: 1px dashed rgba(255,255,255,0.14); height: 0; }
.bc-gl span { position: absolute; left: -46px; top: -8px; width: 38px; text-align: right; font-size: 12px; color: #8b979c; }
.bc-cols { position: absolute; inset: 0; display: flex; gap: 14px; }
.bc-col { position: relative; flex: 1 1 0; min-width: 0; height: 100%; }
.bc-bar { position: absolute; left: 0; right: 0; bottom: 0; min-height: 2px; border-radius: 10px 10px 8px 8px; background: #12171a; border: 1px solid rgba(255,255,255,0.05);
          transition: filter .15s; }
.bc-col:hover .bc-bar { filter: brightness(1.5); }
.bc-bar.hi { background: linear-gradient(180deg, #14b8a6, #0b7f74); border-color: rgba(45,212,191,0.5); box-shadow: 0 0 28px rgba(20,184,166,0.28); }
.bc-pct { position: absolute; left: 0; right: 0; text-align: center; font-size: 13px; font-weight: 500; color: #eef3f4; }
.bc-labs { display: flex; gap: 14px; margin: 12px 0 0 46px; }
.bc-lab { flex: 1 1 0; min-width: 0; text-align: center; font-size: 13px; color: #b4c0c5; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
"""
