from pathlib import Path


OUT_DIR = Path(__file__).resolve().parents[1] / "assets"


TYPE_SPECS = [
    {"code": "yyds", "title": "YYDS", "subtitle": "Output Tsunami", "bg": ("#FFF3BF", "#FFD8A8"), "accent": "#FF922B", "panel": "#FFE8CC", "body": "#FFF8E1", "head": "#FFD166", "prop": "text_rain", "face": "grin", "scene": "stream"},
    {"code": "pua", "title": "PUA", "subtitle": "Advice Principal", "bg": ("#E5DBFF", "#D0BFFF"), "accent": "#7048E8", "panel": "#F3F0FF", "body": "#F8F0FC", "head": "#D0BFFF", "prop": "lecture_board", "face": "stern", "scene": "boardroom"},
    {"code": "cpu", "title": "CPU", "subtitle": "Feelings First", "bg": ("#D3F9D8", "#B2F2BB"), "accent": "#2B8A3E", "panel": "#EBFBEE", "body": "#F1FFF4", "head": "#B2F2BB", "prop": "hearts_bug", "face": "soft", "scene": "calm"},
    {"code": "ppt", "title": "PPT", "subtitle": "Deck Warrior", "bg": ("#D0EBFF", "#A5D8FF"), "accent": "#1C7ED6", "panel": "#E7F5FF", "body": "#F4FAFF", "head": "#A5D8FF", "prop": "screen_pointer", "face": "confident", "scene": "stage"},
    {"code": "bbq", "title": "BBQ", "subtitle": "Critical Failure", "bg": ("#FFE3E3", "#FFC9C9"), "accent": "#E03131", "panel": "#FFF5F5", "body": "#FFF1F1", "head": "#FFA8A8", "prop": "meltdown", "face": "fried", "scene": "crash"},
    {"code": "bro", "title": "BRO", "subtitle": "Thumbs-Up Only", "bg": ("#D3F9D8", "#96F2D7"), "accent": "#099268", "panel": "#E6FCF5", "body": "#F2FFFC", "head": "#96F2D7", "prop": "thumb_banner", "face": "grin", "scene": "support"},
    {"code": "dbq", "title": "DBQ", "subtitle": "Apology Loop", "bg": ("#FFF0F6", "#FCC2D7"), "accent": "#C2255C", "panel": "#FFF5F7", "body": "#FFF8FA", "head": "#FAA2C1", "prop": "bow_sorries", "face": "nervous", "scene": "gentle"},
    {"code": "ojbk", "title": "OJBK", "subtitle": "Absolute Compliance", "bg": ("#D8F5A2", "#B2F2BB"), "accent": "#2F9E44", "panel": "#EBFBEE", "body": "#F3FFF2", "head": "#C0EB75", "prop": "ok_sign", "face": "blank", "scene": "plain"},
    {"code": "vm50", "title": "VM50", "subtitle": "Paywall Sprite", "bg": ("#FFF3BF", "#FFEC99"), "accent": "#E67700", "panel": "#FFF9DB", "body": "#FFFDF2", "head": "#FFE066", "prop": "paywall", "face": "sales", "scene": "commerce"},
    {"code": "sq", "title": "SQ", "subtitle": "Polite Poison", "bg": ("#F3D9FA", "#E599F7"), "accent": "#9C36B5", "panel": "#FCF0FF", "body": "#FEF7FF", "head": "#E599F7", "prop": "tea_sarcasm", "face": "smirk", "scene": "salon"},
    {"code": "u1s1", "title": "U1S1", "subtitle": "Truth Hammer", "bg": ("#FFE8CC", "#FFD8A8"), "accent": "#F76707", "panel": "#FFF4E6", "body": "#FFF9F1", "head": "#FFC078", "prop": "hammer_wall", "face": "firm", "scene": "impact"},
    {"code": "dddd", "title": "DDDD", "subtitle": "Hint Merchant", "bg": ("#DEE2E6", "#CED4DA"), "accent": "#495057", "panel": "#F8F9FA", "body": "#FFFFFF", "head": "#ADB5BD", "prop": "mirror_hush", "face": "hidden", "scene": "mystery"},
    {"code": "xswl", "title": "XSWL", "subtitle": "Chaos Jester", "bg": ("#FFD6A5", "#FDFFB6"), "accent": "#FF6B6B", "panel": "#FFF7E6", "body": "#FFFDF4", "head": "#FFD6A5", "prop": "jester_cat", "face": "laugh", "scene": "party"},
    {"code": "bdjw", "title": "BDJW", "subtitle": "Instant Guru", "bg": ("#E5DBFF", "#CDB4DB"), "accent": "#6741D9", "panel": "#F3F0FF", "body": "#FBF7FF", "head": "#D0BFFF", "prop": "fake_scholar", "face": "proud", "scene": "scholar"},
    {"code": "srds", "title": "SRDS", "subtitle": "Balanced Forever", "bg": ("#E6FCF5", "#C3FAE8"), "accent": "#0CA678", "panel": "#F1FFFA", "body": "#FCFFFE", "head": "#96F2D7", "prop": "tipping_scale", "face": "worried", "scene": "balance"},
    {"code": "nmsl", "title": "NMSL", "subtitle": "Infinite Steps", "bg": ("#DCEBFF", "#BAC8FF"), "accent": "#4263EB", "panel": "#EEF2FF", "body": "#F8FAFF", "head": "#BAC8FF", "prop": "checklist", "face": "focused", "scene": "office"},
    {"code": "wtd", "title": "WTD", "subtitle": "Wrong Universe", "bg": ("#FFF3BF", "#B2F2BB"), "accent": "#5F3DC4", "panel": "#FFF9DB", "body": "#FCFFF7", "head": "#FFD43B", "prop": "dog_banana", "face": "confused", "scene": "weird"},
    {"code": "404", "title": "404", "subtitle": "Confident Fiction", "bg": ("#FFD8A8", "#FFB4A2"), "accent": "#D9480F", "panel": "#FFF4E6", "body": "#FFF8F2", "head": "#FFC078", "prop": "wizard_docs", "face": "smile", "scene": "library"},
    {"code": "rag", "title": "RAG", "subtitle": "Patchwork Brain", "bg": ("#F1F3F5", "#DEE2E6"), "accent": "#1971C2", "panel": "#FFFFFF", "body": "#FAFBFC", "head": "#CED4DA", "prop": "messy_puzzle", "face": "busy", "scene": "studio"},
    {"code": "ctrl-c", "title": "CTRL-C", "subtitle": "Mirror Parrot", "bg": ("#E7F5FF", "#C5F6FA"), "accent": "#0B7285", "panel": "#F3FBFD", "body": "#FCFEFF", "head": "#99E9F2", "prop": "parrot_mirror", "face": "copy", "scene": "echo"},
    {"code": "429", "title": "429", "subtitle": "Busy Forever", "bg": ("#FFE3E3", "#F8D7DA"), "accent": "#C92A2A", "panel": "#FFF5F5", "body": "#FFF9F9", "head": "#FFC9C9", "prop": "loading_door", "face": "distant", "scene": "queue"},
    {"code": "emo", "title": "EMO", "subtitle": "All or Nothing", "bg": ("#FFD6E0", "#D0BFFF"), "accent": "#E03131", "panel": "#FFF0F6", "body": "#FFF8FC", "head": "#FCC2D7", "prop": "split_mood", "face": "split", "scene": "split"},
    {"code": "npc", "title": "NPC", "subtitle": "Kind Villager", "bg": ("#D3F9D8", "#CCF2FF"), "accent": "#2B8A3E", "panel": "#F1FFF5", "body": "#FCFFFD", "head": "#C3FAE8", "prop": "halo_heart", "face": "gentle", "scene": "garden"},
    {"code": "kfc", "title": "KFC", "subtitle": "Can-Do Storm", "bg": ("#FFE8CC", "#FFD43B"), "accent": "#E8590C", "panel": "#FFF4E6", "body": "#FFF9F3", "head": "#FFC078", "prop": "overloaded_desk", "face": "determined", "scene": "workshop"},
]


def svg_text(x: int, y: int, text: str, size: int, fill: str, weight: int = 600, anchor: str = "start", opacity: float = 1.0) -> str:
    return (
        f'<text x="{x}" y="{y}" fill="{fill}" fill-opacity="{opacity}" '
        f'font-family="Avenir Next,Segoe UI,Arial,sans-serif" font-size="{size}" '
        f'font-weight="{weight}" text-anchor="{anchor}">{text}</text>'
    )


def background_scene(spec: dict) -> str:
    accent = spec["accent"]
    panel = spec["panel"]
    scene = spec["scene"]
    scenes = {
        "stream": f"""
        <path d="M48 330 q94 -52 192 -18 q102 36 224 -8 v84 h-416z" fill="#FFFFFF" opacity="0.28"/>
        <path d="M56 142 q42 -20 84 0 q42 20 84 0 q42 -20 84 0 q42 20 84 0 q42 -20 70 0" fill="none" stroke="#FFFFFF" stroke-width="12" opacity="0.22"/>
        """,
        "boardroom": f"""
        <rect x="54" y="86" width="404" height="142" rx="26" fill="#FFFFFF" opacity="0.2"/>
        <path d="M84 132 h344 M84 172 h218" stroke="#FFFFFF" stroke-width="12" stroke-linecap="round" opacity="0.22"/>
        """,
        "calm": f"""
        <circle cx="118" cy="120" r="56" fill="#FFFFFF" opacity="0.22"/>
        <circle cx="390" cy="110" r="36" fill="#FFFFFF" opacity="0.18"/>
        """,
        "stage": f"""
        <path d="M60 92 h392" stroke="#FFFFFF" stroke-width="10" stroke-linecap="round" opacity="0.3"/>
        <path d="M88 92 l-24 58 M424 92 l24 58" stroke="#FFFFFF" stroke-width="8" stroke-linecap="round" opacity="0.25"/>
        """,
        "crash": f"""
        <path d="M66 124 l56 32 22 -54 34 40 44 -32 32 38 44 -22 54 38" fill="none" stroke="#FFFFFF" stroke-width="10" stroke-linecap="round" stroke-linejoin="round" opacity="0.2"/>
        """,
        "support": f"""
        <path d="M72 120 q40 -34 82 0 q42 34 82 0 q42 -34 82 0 q40 34 84 0" fill="none" stroke="#FFFFFF" stroke-width="12" stroke-linecap="round" opacity="0.22"/>
        """,
        "gentle": f"""
        <circle cx="102" cy="124" r="28" fill="#FFFFFF" opacity="0.25"/>
        <circle cx="412" cy="142" r="22" fill="#FFFFFF" opacity="0.22"/>
        <circle cx="378" cy="92" r="12" fill="#FFFFFF" opacity="0.18"/>
        """,
        "plain": f"""
        <path d="M68 146 h376" stroke="#FFFFFF" stroke-width="10" stroke-linecap="round" opacity="0.2"/>
        """,
        "commerce": f"""
        <path d="M64 116 h384" stroke="#FFFFFF" stroke-width="10" stroke-linecap="round" opacity="0.22"/>
        <circle cx="108" cy="146" r="18" fill="#FFFFFF" opacity="0.18"/>
        <circle cx="404" cy="136" r="18" fill="#FFFFFF" opacity="0.18"/>
        """,
        "salon": f"""
        <path d="M74 124 q72 -54 144 0 q74 54 146 0 q38 -24 74 0" fill="none" stroke="#FFFFFF" stroke-width="12" opacity="0.22" stroke-linecap="round"/>
        """,
        "impact": f"""
        <path d="M382 74 l18 22 26 -4 -12 22 14 22 -26 -2 -18 22 -4 -28 -24 -10 24 -10z" fill="#FFFFFF" opacity="0.26"/>
        """,
        "mystery": f"""
        <circle cx="384" cy="102" r="48" fill="#FFFFFF" opacity="0.15"/>
        <path d="M96 154 q84 -42 160 0 q74 42 160 0" fill="none" stroke="#FFFFFF" stroke-width="10" opacity="0.15"/>
        """,
        "party": f"""
        <circle cx="90" cy="104" r="10" fill="#FFFFFF" opacity="0.24"/>
        <circle cx="130" cy="134" r="8" fill="#FFFFFF" opacity="0.24"/>
        <circle cx="412" cy="120" r="12" fill="#FFFFFF" opacity="0.24"/>
        <circle cx="378" cy="94" r="7" fill="#FFFFFF" opacity="0.24"/>
        """,
        "scholar": f"""
        <rect x="70" y="96" width="372" height="122" rx="16" fill="#FFFFFF" opacity="0.16"/>
        <path d="M96 128 h312 M96 156 h254 M96 184 h188" stroke="#FFFFFF" stroke-width="10" stroke-linecap="round" opacity="0.2"/>
        """,
        "balance": f"""
        <path d="M64 140 q96 -30 192 0 q98 30 192 0" fill="none" stroke="#FFFFFF" stroke-width="12" stroke-linecap="round" opacity="0.18"/>
        """,
        "office": f"""
        <rect x="74" y="90" width="102" height="74" rx="14" fill="#FFFFFF" opacity="0.18"/>
        <rect x="336" y="102" width="96" height="58" rx="14" fill="#FFFFFF" opacity="0.14"/>
        """,
        "weird": f"""
        <path d="M86 108 q28 40 0 80 q-28 40 0 80" fill="none" stroke="#FFFFFF" stroke-width="10" opacity="0.2"/>
        <path d="M426 108 q-28 40 0 80 q28 40 0 80" fill="none" stroke="#FFFFFF" stroke-width="10" opacity="0.2"/>
        """,
        "library": f"""
        <rect x="72" y="84" width="366" height="138" rx="18" fill="#FFFFFF" opacity="0.14"/>
        <path d="M104 106 v94 M148 106 v94 M192 106 v94 M236 106 v94 M280 106 v94 M324 106 v94 M368 106 v94" stroke="#FFFFFF" stroke-width="8" opacity="0.2"/>
        """,
        "studio": f"""
        <path d="M86 108 l64 36 52 -30 58 44 42 -38 74 24" fill="none" stroke="#FFFFFF" stroke-width="10" opacity="0.18" stroke-linecap="round" stroke-linejoin="round"/>
        """,
        "echo": f"""
        <ellipse cx="126" cy="126" rx="52" ry="66" fill="#FFFFFF" opacity="0.15"/>
        <ellipse cx="386" cy="126" rx="42" ry="54" fill="#FFFFFF" opacity="0.15"/>
        """,
        "queue": f"""
        <rect x="318" y="84" width="90" height="164" rx="18" fill="#FFFFFF" opacity="0.18"/>
        <path d="M92 156 h124 M92 188 h86" stroke="#FFFFFF" stroke-width="10" stroke-linecap="round" opacity="0.18"/>
        """,
        "split": f"""
        <path d="M256 54 v406" stroke="#FFFFFF" stroke-width="8" opacity="0.22"/>
        <path d="M92 108 h104 M316 108 h104" stroke="#FFFFFF" stroke-width="10" stroke-linecap="round" opacity="0.16"/>
        """,
        "garden": f"""
        <path d="M70 356 q40 -74 98 0 q58 -74 114 0 q58 -74 114 0 q54 -74 92 0" fill="none" stroke="{accent}" stroke-width="8" opacity="0.15"/>
        """,
        "workshop": f"""
        <rect x="76" y="96" width="84" height="54" rx="12" fill="#FFFFFF" opacity="0.16"/>
        <rect x="352" y="92" width="84" height="62" rx="12" fill="#FFFFFF" opacity="0.16"/>
        <path d="M94 168 h46 M372 172 h44" stroke="#FFFFFF" stroke-width="8" stroke-linecap="round" opacity="0.18"/>
        """,
    }
    return scenes[scene]


def floor(spec: dict) -> str:
    accent = spec["accent"]
    panel = spec["panel"]
    return f"""
    <path d="M74 390 l118 -44 h128 l118 44 v26 h-364z" fill="{panel}" opacity="0.96"/>
    <path d="M98 388 h316" fill="none" stroke="{accent}" stroke-width="6" opacity="0.18" stroke-linecap="round"/>
    """


def speech_bubble(x: int, y: int, w: int, h: int, text: str, fill: str, stroke: str) -> str:
    tx = x + w / 2
    ty = y + h / 2 + 6
    return (
        f'<g><path d="M{x} {y + 8} l8 -8 h{w - 16} l8 8 v{h - 8} l-8 8 h-{w - 16} l-8 -8 z" fill="{fill}" stroke="{stroke}" stroke-width="3" stroke-linejoin="round"/>'
        f'<path d="M{x + 34} {y + h} l10 16 14 -16" fill="{fill}" stroke="{stroke}" stroke-width="3" stroke-linejoin="round"/>'
        f'{svg_text(int(tx), int(ty), text, 18, stroke, 700, "middle")}</g>'
    )


def tiny_card(x: int, y: int, w: int, h: int, accent: str, label: str, fill: str = "#FFFFFF") -> str:
    return (
        f'<g><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill}" stroke="{accent}" stroke-width="3"/>'
        f'{svg_text(x + w // 2, y + h // 2 + 6, label, 16, accent, 800, "middle")}</g>'
    )


def prop_art(spec: dict) -> str:
    accent = spec["accent"]
    panel = spec["panel"]
    prop = spec["prop"]
    art = {
        "text_rain": f"""
        <g>
            {speech_bubble(304, 84, 130, 52, "more detail", "#FFFFFF", accent)}
            {speech_bubble(336, 150, 106, 48, "step 1...", panel, accent)}
            <path d="M360 218 q24 20 18 50" fill="none" stroke="{accent}" stroke-width="8" stroke-linecap="round"/>
            <path d="M396 224 q18 18 10 42" fill="none" stroke="{accent}" stroke-width="8" stroke-linecap="round"/>
        </g>
        """,
        "lecture_board": f"""
        <g>
            <rect x="306" y="86" width="132" height="110" rx="18" fill="{panel}" stroke="{accent}" stroke-width="4"/>
            {svg_text(372, 118, "Advice", 20, accent, 900, "middle")}
            <path d="M326 142 h88 M326 164 h72 M326 184 h60" stroke="{accent}" stroke-width="7" stroke-linecap="round"/>
            {tiny_card(344, 206, 82, 32, accent, "mentor", panel)}
        </g>
        """,
        "hearts_bug": f"""
        <g>
            <circle cx="398" cy="112" r="22" fill="#FFFFFF" opacity="0.96"/>{svg_text(398, 120, "❤", 24, accent, 800, "middle")}
            <circle cx="430" cy="148" r="18" fill="#FFFFFF" opacity="0.96"/>{svg_text(430, 155, "❤", 20, accent, 800, "middle")}
            {tiny_card(336, 196, 96, 44, accent, "BUG", "#FFFFFF")}
        </g>
        """,
        "screen_pointer": f"""
        <g>
            <rect x="294" y="74" width="148" height="112" rx="18" fill="{panel}" stroke="{accent}" stroke-width="4"/>
            <path d="M320 98 h98 M320 122 h60 M320 146 h78" stroke="{accent}" stroke-width="8" stroke-linecap="round"/>
            <path d="M418 214 l-30 -22 6 40 12 -12 18 18 10 -8 -18 -18z" fill="{accent}"/>
        </g>
        """,
        "meltdown": f"""
        <g>
            <path d="M340 92 l18 22 22 -8 -6 24 18 16 -26 4 -6 24 -18 -18 -22 8 8 -24 -18 -16 26 -4z" fill="#FFFFFF" opacity="0.9"/>
            {tiny_card(340, 190, 94, 44, accent, "ERROR", "#FFFFFF")}
        </g>
        """,
        "thumb_banner": f"""
        <g>
            <path d="M302 116 h126 a16 16 0 0 1 16 16 v40 a16 16 0 0 1 -16 16 h-126z" fill="{panel}" stroke="{accent}" stroke-width="4"/>
            {svg_text(370, 146, "you got this", 16, accent, 800, "middle")}
            {svg_text(420, 108, "👍", 24, accent, 800, "middle")}
        </g>
        """,
        "bow_sorries": f"""
        <g>
            {speech_bubble(314, 82, 112, 50, "sorry", "#FFFFFF", accent)}
            {speech_bubble(340, 146, 88, 44, "抱歉", panel, accent)}
            {tiny_card(336, 204, 92, 38, accent, "again", "#FFFFFF")}
        </g>
        """,
        "ok_sign": f"""
        <g>
            <circle cx="394" cy="118" r="38" fill="#FFFFFF" opacity="0.96" stroke="{accent}" stroke-width="4"/>
            {svg_text(394, 126, "OK", 24, accent, 900, "middle")}
        </g>
        """,
        "paywall": f"""
        <g>
            <rect x="314" y="82" width="118" height="152" rx="18" fill="#FFFFFF" opacity="0.96" stroke="{accent}" stroke-width="4"/>
            {svg_text(372, 118, "PRO", 28, accent, 900, "middle")}
            <path d="M334 144 h78 M334 170 h78 M334 196 h54" stroke="{accent}" stroke-width="8" stroke-linecap="round"/>
            <rect x="336" y="206" width="72" height="22" rx="11" fill="{accent}"/>
        </g>
        """,
        "tea_sarcasm": f"""
        <g>
            {speech_bubble(306, 78, 128, 50, "sure :)", "#FFFFFF", accent)}
            <path d="M334 214 h76 a20 20 0 0 0 20 -20 v-12 h-96 z" fill="{panel}" stroke="{accent}" stroke-width="4"/>
            <path d="M430 186 q18 0 18 14 q0 14 -18 14" fill="none" stroke="{accent}" stroke-width="4"/>
        </g>
        """,
        "hammer_wall": f"""
        <g>
            <rect x="322" y="80" width="104" height="102" rx="18" fill="{panel}" stroke="{accent}" stroke-width="4"/>
            <path d="M342 104 h62 M342 126 h62 M342 148 h62" stroke="{accent}" stroke-width="8" stroke-linecap="round"/>
            <path d="M424 222 l-18 -48 -16 6 8 24 -16 6 6 14 16 -6 6 16z" fill="{accent}"/>
        </g>
        """,
        "mirror_hush": f"""
        <g>
            <ellipse cx="396" cy="124" rx="40" ry="56" fill="#FFFFFF" opacity="0.92" stroke="{accent}" stroke-width="4"/>
            <ellipse cx="396" cy="124" rx="24" ry="36" fill="{panel}" opacity="0.9"/>
            {tiny_card(330, 204, 106, 38, accent, "... ?", "#FFFFFF")}
        </g>
        """,
        "jester_cat": f"""
        <g>
            <path d="M322 82 l20 30 22 -30 22 30 20 -30 v38 h-84z" fill="{accent}" opacity="0.84"/>
            {tiny_card(322, 176, 108, 54, accent, ":3", "#FFFFFF")}
        </g>
        """,
        "fake_scholar": f"""
        <g>
            <path d="M322 106 l50 -28 50 28 -50 28z" fill="{accent}" opacity="0.88"/>
            <path d="M372 134 v34" stroke="{accent}" stroke-width="6" stroke-linecap="round"/>
            <circle cx="372" cy="174" r="8" fill="{accent}"/>
            {tiny_card(324, 196, 98, 34, accent, "PhD*", "#FFFFFF")}
        </g>
        """,
        "tipping_scale": f"""
        <g>
            <path d="M374 84 v110" stroke="{accent}" stroke-width="8" stroke-linecap="round"/>
            <path d="M320 120 h108" stroke="{accent}" stroke-width="8" stroke-linecap="round"/>
            <path d="M334 120 l-22 36 h44z M414 120 l-22 36 h44z" fill="#FFFFFF" stroke="{accent}" stroke-width="4" stroke-linejoin="round"/>
            {tiny_card(324, 204, 96, 34, accent, "but...", panel)}
        </g>
        """,
        "checklist": f"""
        <g>
            <rect x="312" y="76" width="120" height="158" rx="18" fill="#FFFFFF" opacity="0.96" stroke="{accent}" stroke-width="4"/>
            <path d="M336 108 h72 M336 136 h72 M336 164 h72 M336 192 h56" stroke="{accent}" stroke-width="8" stroke-linecap="round"/>
            <path d="M324 104 l8 8 12 -14 M324 132 l8 8 12 -14 M324 160 l8 8 12 -14" fill="none" stroke="{accent}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
        </g>
        """,
        "dog_banana": f"""
        <g>
            <circle cx="360" cy="112" r="32" fill="#FFFFFF" opacity="0.94" stroke="{accent}" stroke-width="4"/>
            {svg_text(360, 120, "?", 26, accent, 900, "middle")}
            {tiny_card(386, 178, 48, 42, accent, "🍌", "#FFFFFF")}
        </g>
        """,
        "wizard_docs": f"""
        <g>
            <path d="M362 84 l22 0 10 38 h-42z" fill="{accent}" opacity="0.88"/>
            {tiny_card(314, 154, 54, 64, accent, "API", "#FFFFFF")}
            {tiny_card(378, 162, 48, 56, accent, "??", panel)}
        </g>
        """,
        "messy_puzzle": f"""
        <g>
            <path d="M316 100 h46 v22 h18 v-22 h46 v46 h-22 v18 h22 v46 h-46 v-22 h-18 v22 h-46 v-46 h22 v-18 h-22z" fill="#FFFFFF" opacity="0.94" stroke="{accent}" stroke-width="4"/>
            <path d="M332 124 l20 18 22 -24 26 28" fill="none" stroke="{accent}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
        </g>
        """,
        "parrot_mirror": f"""
        <g>
            <ellipse cx="406" cy="126" rx="28" ry="40" fill="#FFFFFF" opacity="0.92" stroke="{accent}" stroke-width="4"/>
            <ellipse cx="330" cy="150" rx="24" ry="36" fill="{panel}" opacity="0.92" stroke="{accent}" stroke-width="4"/>
            <path d="M382 126 q24 -14 48 0 M306 150 q24 -14 48 0" fill="none" stroke="{accent}" stroke-width="4"/>
        </g>
        """,
        "loading_door": f"""
        <g>
            <rect x="324" y="80" width="86" height="152" rx="16" fill="#FFFFFF" opacity="0.94" stroke="{accent}" stroke-width="4"/>
            <circle cx="368" cy="164" r="22" fill="none" stroke="{accent}" stroke-width="8" stroke-dasharray="18 14"/>
            {tiny_card(338, 104, 58, 28, accent, "WAIT", panel)}
        </g>
        """,
        "split_mood": f"""
        <g>
            <path d="M316 80 h52 v154 h-52z" fill="#FFE066" opacity="0.9"/>
            <path d="M368 80 h52 v154 h-52z" fill="#A5D8FF" opacity="0.95"/>
            {svg_text(342, 132, "★", 28, accent, 800, "middle")}
            {svg_text(394, 134, "!", 30, "#C92A2A", 900, "middle")}
        </g>
        """,
        "halo_heart": f"""
        <g>
            <ellipse cx="374" cy="84" rx="34" ry="10" fill="none" stroke="{accent}" stroke-width="5"/>
            <circle cx="374" cy="144" r="32" fill="#FFFFFF" opacity="0.96" stroke="{accent}" stroke-width="4"/>
            {svg_text(374, 154, "❤", 28, accent, 800, "middle")}
            {speech_bubble(300, 186, 146, 44, "you okay?", panel, accent)}
        </g>
        """,
        "overloaded_desk": f"""
        <g>
            <rect x="302" y="180" width="136" height="54" rx="10" fill="#FFFFFF" opacity="0.94" stroke="{accent}" stroke-width="4"/>
            <rect x="316" y="136" width="34" height="38" rx="8" fill="{panel}" stroke="{accent}" stroke-width="3"/>
            <rect x="356" y="122" width="40" height="52" rx="8" fill="#FFFFFF" stroke="{accent}" stroke-width="3"/>
            <rect x="406" y="142" width="22" height="30" rx="8" fill="{panel}" stroke="{accent}" stroke-width="3"/>
            {svg_text(370, 212, "doing all of it", 15, accent, 800, "middle")}
        </g>
        """,
    }
    return art[prop]


def face_markup(face_type: str, accent: str) -> str:
    if face_type in {"grin", "confident", "soft", "gentle", "smile", "focused", "proud", "sales"}:
        eyes = '<rect x="-24" y="-4" width="8" height="8"/><rect x="16" y="-4" width="8" height="8"/>'
        mouth = '<path d="M-14 20 l8 6 h12 l8 -6" fill="none" stroke-width="4" stroke-linecap="square" stroke-linejoin="round"/>'
    elif face_type in {"stern", "firm", "determined"}:
        eyes = '<path d="M-28 -2 l14 -4 M14 -6 l14 4" stroke-width="4" stroke-linecap="square"/>'
        mouth = '<path d="M-12 22 h24" fill="none" stroke-width="4" stroke-linecap="square"/>'
    elif face_type == "blank":
        eyes = '<rect x="-23" y="-3" width="6" height="6"/><rect x="17" y="-3" width="6" height="6"/>'
        mouth = '<path d="M-10 22 h20" fill="none" stroke-width="3" stroke-linecap="square"/>'
    elif face_type in {"nervous", "worried", "busy", "distant"}:
        eyes = '<rect x="-24" y="-4" width="8" height="8"/><rect x="16" y="-4" width="8" height="8"/>'
        mouth = '<path d="M-14 26 l10 -4 h8 l10 4" fill="none" stroke-width="4" stroke-linecap="square" stroke-linejoin="round"/>'
    elif face_type == "fried":
        eyes = '<path d="M-26 -4 l10 10 M-16 -4 l-10 10 M14 -4 l10 10 M24 -4 l-10 10" stroke-width="4" stroke-linecap="square"/>'
        mouth = '<circle cx="0" cy="24" r="7" fill="none" stroke-width="4"/>'
    elif face_type == "smirk":
        eyes = '<rect x="-24" y="-4" width="8" height="8"/><rect x="16" y="-4" width="8" height="8"/>'
        mouth = '<path d="M-8 22 l10 4 h10 l8 -2" fill="none" stroke-width="4" stroke-linecap="square" stroke-linejoin="round"/>'
    elif face_type == "laugh":
        eyes = '<path d="M-24 0 h8 M16 0 h8" fill="none" stroke-width="4" stroke-linecap="square"/>'
        mouth = '<path d="M-16 20 l8 10 h16 l8 -10" fill="none" stroke-width="5" stroke-linecap="square" stroke-linejoin="round"/>'
    elif face_type == "confused":
        eyes = '<rect x="-24" y="-4" width="8" height="8"/><rect x="16" y="-4" width="8" height="8"/>'
        mouth = '<path d="M-14 22 l10 -2 h8 l10 4" fill="none" stroke-width="4" stroke-linecap="square" stroke-linejoin="round"/>'
    elif face_type == "hidden":
        eyes = '<rect x="-30" y="-8" width="20" height="10" rx="4"/><rect x="10" y="-8" width="20" height="10" rx="4"/><rect x="-10" y="-6" width="20" height="4"/>'
        mouth = '<path d="M-12 22 l8 4 h8 l8 -4" fill="none" stroke-width="4" stroke-linecap="square" stroke-linejoin="round"/>'
    elif face_type == "copy":
        eyes = '<rect x="-24" y="-4" width="8" height="8"/><rect x="16" y="-4" width="8" height="8"/>'
        mouth = '<path d="M-16 22 l10 2 h12 l10 -2" fill="none" stroke-width="4" stroke-linecap="square" stroke-linejoin="round"/>'
    elif face_type == "split":
        eyes = '<rect x="-24" y="-4" width="8" height="8"/><rect x="16" y="-4" width="8" height="8"/>'
        mouth = '<path d="M-14 24 l8 6 h6 l6 -6 h6 l8 6" fill="none" stroke-width="4" stroke-linecap="square" stroke-linejoin="round"/>'
    else:
        eyes = '<rect x="-24" y="-4" width="8" height="8"/><rect x="16" y="-4" width="8" height="8"/>'
        mouth = '<path d="M-14 22 l8 4 h12 l8 -4" fill="none" stroke-width="4" stroke-linecap="square" stroke-linejoin="round"/>'
    return f'<g fill="{accent}" stroke="{accent}">{eyes}{mouth}</g>'


def hat(spec: dict) -> str:
    accent = spec["accent"]
    panel = spec["panel"]
    title = spec["title"]
    hats = {
        "PUA": f'<path d="M176 114 h76 l-8 18 h-60z" fill="{panel}" stroke="{accent}" stroke-width="4"/>',
        "PPT": f'<path d="M182 110 h64 l10 14 h-84z" fill="{panel}" stroke="{accent}" stroke-width="4"/>',
        "DBQ": f'<path d="M186 108 h56 l8 12 h-72z" fill="{panel}" stroke="{accent}" stroke-width="4"/>',
        "OJBK": f'<path d="M188 110 h52 v18 h-52z" fill="{panel}" stroke="{accent}" stroke-width="4"/>',
        "VM50": f'<path d="M182 108 h64 l-8 18 h-48z" fill="{panel}" stroke="{accent}" stroke-width="4"/>',
        "SQ": f'<path d="M184 108 h60 l-10 18 h-40z" fill="{panel}" stroke="{accent}" stroke-width="4"/>',
        "U1S1": f'<path d="M188 108 h52 l12 10 h-76z" fill="{panel}" stroke="{accent}" stroke-width="4"/>',
        "DDDD": f'<path d="M180 108 h68 l-6 14 h-56z" fill="{panel}" stroke="{accent}" stroke-width="4"/>',
        "XSWL": f'<path d="M176 116 l18 -18 20 18 20 -18 18 18 v8 h-76z" fill="{panel}" stroke="{accent}" stroke-width="4" stroke-linejoin="round"/>',
        "BDJW": f'<path d="M176 116 l38 -18 38 18 -38 18z" fill="{panel}" stroke="{accent}" stroke-width="4" stroke-linejoin="round"/>',
        "WTD": f'<path d="M180 112 h68 l-12 16 h-44z" fill="{panel}" stroke="{accent}" stroke-width="4"/>',
        "404": f'<path d="M184 112 h60 l-8 16 h-44z" fill="{panel}" stroke="{accent}" stroke-width="4"/>',
        "CTRL-C": f'<path d="M182 110 h64 l-8 16 h-48z" fill="{panel}" stroke="{accent}" stroke-width="4"/>',
        "429": f'<path d="M186 110 h56 l-10 16 h-36z" fill="{panel}" stroke="{accent}" stroke-width="4"/>',
        "NPC": f'<path d="M186 112 h56 l8 10 h-72z" fill="{panel}" stroke="{accent}" stroke-width="4"/>',
        "KFC": f'<path d="M182 112 h64 l-6 16 h-52z" fill="{panel}" stroke="{accent}" stroke-width="4"/>',
    }
    return hats.get(title, "")


def costume(spec: dict) -> str:
    accent = spec["accent"]
    title = spec["title"]
    extras = {
        "PUA": f'<path d="M188 188 h38" stroke="{accent}" stroke-width="8" stroke-linecap="square"/>',
        "CPU": f'<path d="M228 208 l14 8 h20 l14 -8" fill="none" stroke="{accent}" stroke-width="6" stroke-linecap="square" stroke-linejoin="round"/>',
        "PPT": f'<path d="M196 162 h62 M196 178 h48" stroke="{accent}" stroke-width="6" stroke-linecap="square"/>',
        "BBQ": f'<path d="M192 144 l12 18 M224 136 l12 18" stroke="{accent}" stroke-width="6" stroke-linecap="square" opacity="0.65"/>',
        "BRO": svg_text(292, 164, "👍", 22, accent, 800, "middle"),
        "DBQ": svg_text(180, 160, "!", 18, accent, 800, "middle"),
        "VM50": svg_text(292, 164, "$", 22, accent, 900, "middle"),
        "SQ": f'<path d="M190 182 h34" stroke="{accent}" stroke-width="6" stroke-linecap="square"/>',
        "U1S1": f'<path d="M182 198 h46" stroke="{accent}" stroke-width="8" stroke-linecap="square"/>',
        "DDDD": f'<path d="M178 140 h52" stroke="{accent}" stroke-width="6" stroke-linecap="square"/>',
        "XSWL": svg_text(292, 164, "*", 22, accent, 900, "middle"),
        "BDJW": f'<path d="M190 150 h48" stroke="{accent}" stroke-width="6" stroke-linecap="square"/>',
        "SRDS": f'<path d="M206 196 v18" stroke="{accent}" stroke-width="6" stroke-linecap="square"/>',
        "NMSL": f'<path d="M182 156 h46 M182 172 h46 M182 188 h30" stroke="{accent}" stroke-width="5" stroke-linecap="square"/>',
        "WTD": svg_text(292, 162, "?", 22, accent, 900, "middle"),
        "404": svg_text(180, 156, "404", 16, accent, 900, "start"),
        "RAG": f'<path d="M184 154 l16 16 16 -16 16 16" fill="none" stroke="{accent}" stroke-width="5" stroke-linecap="square" stroke-linejoin="miter"/>',
        "CTRL-C": f'<path d="M184 162 h54" stroke="{accent}" stroke-width="6" stroke-dasharray="8 8" stroke-linecap="square"/>',
        "429": svg_text(180, 156, "...", 22, accent, 800, "start"),
        "EMO": f'<path d="M208 136 v92" stroke="{accent}" stroke-width="5" opacity="0.4"/>',
        "NPC": svg_text(292, 164, "❤", 20, accent, 800, "middle"),
        "KFC": f'<path d="M184 152 h46 M184 170 h46" stroke="{accent}" stroke-width="6" stroke-linecap="square"/>',
    }
    return extras.get(title, "")


def character(spec: dict) -> str:
    accent = spec["accent"]
    body = spec["body"]
    head = spec["head"]
    face = face_markup(spec["face"], accent)
    return f"""
    <g>
        <path d="M152 366 l28 -18 h68 l28 18 l-16 8 h-92z" fill="#000000" opacity="0.1"/>
        <path d="M172 216 l32 -20 h20 l32 20 v82 l-16 30 h-52 l-16 -30z" fill="{body}" stroke="{accent}" stroke-width="4" stroke-linejoin="miter"/>
        <path d="M188 328 v54 M240 328 v54" fill="none" stroke="{accent}" stroke-width="12" stroke-linecap="square"/>
        <path d="M166 248 l-44 36 M262 248 l44 34" fill="none" stroke="{accent}" stroke-width="12" stroke-linecap="square"/>
        <path d="M178 382 h26 M236 382 h26" fill="none" stroke="{accent}" stroke-width="12" stroke-linecap="square"/>
        <circle cx="214" cy="160" r="52" fill="{head}" stroke="{accent}" stroke-width="4"/>
        {hat(spec)}
        <g transform="translate(214 154)">{face}</g>
        <path d="M168 112 l46 -18 l46 18" fill="none" stroke="{accent}" stroke-width="8" stroke-linecap="square" opacity="0.12"/>
        {costume(spec)}
    </g>
    """


def build_svg(spec: dict) -> str:
    bg1, bg2 = spec["bg"]
    accent = spec["accent"]
    panel = spec["panel"]
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 512 512" fill="none">
  <defs>
    <linearGradient id="bg" x1="44" y1="44" x2="468" y2="468" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="{bg1}"/>
      <stop offset="1" stop-color="{bg2}"/>
    </linearGradient>
    <linearGradient id="light" x1="96" y1="72" x2="388" y2="352" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#FFFFFF" stop-opacity="0.58"/>
      <stop offset="1" stop-color="#FFFFFF" stop-opacity="0.08"/>
    </linearGradient>
  </defs>
  <rect x="16" y="16" width="480" height="480" rx="38" fill="url(#bg)"/>
  <path d="M102 92 l178 -34 l126 82 l-24 214 l-194 62 l-110 -88 l24 -176z" fill="url(#light)"/>
  <path d="M42 40 h428 l10 10 v412 l-10 10 h-428 l-8 -10 v-412z" fill="#FFFFFF" opacity="0.05" stroke="#FFFFFF" stroke-opacity="0.4"/>
  {background_scene(spec)}
  {floor(spec)}
  {character(spec)}
  {prop_art(spec)}
  <rect x="46" y="404" width="188" height="54" rx="8" fill="#FFFFFF" opacity="0.8"/>
  {svg_text(68, 438, spec["title"], 40, accent, 900)}
  {svg_text(68, 462, spec["subtitle"], 16, "#344054", 700)}
  <rect x="384" y="422" width="72" height="26" rx="6" fill="{panel}" stroke="{accent}" stroke-width="3"/>
  {svg_text(420, 440, "SBAI", 14, accent, 900, "middle")}
</svg>
"""


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for spec in TYPE_SPECS:
        (OUT_DIR / f"{spec['code']}.svg").write_text(build_svg(spec), encoding="utf-8")
    print(f"Generated {len(TYPE_SPECS)} SVG files in {OUT_DIR}")


if __name__ == "__main__":
    main()
