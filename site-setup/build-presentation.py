"""
Build the 2026 Field Day presentation. Run from anywhere:

    python3 site-setup/build-presentation.py

Output is written next to this script as 2026-field-day-presentation.pptx.

Slide style follows the 7x7 rule: at most 7 bullets per slide, at most ~7
words per bullet. Split content across more slides rather than letting text
overflow.
"""
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
import os

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
OUT = os.path.join(HERE, "2026-field-day-presentation.pptx")
LOGO_STRIP = os.path.join(REPO, "brochures", "build", "four_club_strip.png")

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

LAY_TITLE = prs.slide_layouts[0]
LAY_CONTENT = prs.slide_layouts[1]
LAY_SECTION = prs.slide_layouts[5]

ACCENT = RGBColor(0x1F, 0x4E, 0x79)
MUTED = RGBColor(0x55, 0x55, 0x55)


def add_title_slide(title, subtitle):
    s = prs.slides.add_slide(LAY_TITLE)
    s.shapes.title.text = title
    s.placeholders[1].text = subtitle
    for para in s.shapes.title.text_frame.paragraphs:
        for r in para.runs:
            r.font.color.rgb = ACCENT
            r.font.bold = True
    return s


def add_bullets(title, bullets, subtitle=None):
    s = prs.slides.add_slide(LAY_CONTENT)
    s.shapes.title.text = title
    for r in s.shapes.title.text_frame.paragraphs[0].runs:
        r.font.color.rgb = ACCENT
        r.font.bold = True
    body = s.placeholders[1].text_frame

    # Build a flat sequence: optional subtitle, then bullets.
    items = []
    if subtitle:
        items.append({"text": subtitle, "level": 0, "subtitle": True})
    for item in bullets:
        if isinstance(item, tuple):
            text, level = item
        else:
            text, level = item, 0
        items.append({"text": text, "level": level, "subtitle": False})

    # First item replaces the existing single paragraph; the rest are added.
    # This avoids text_frame.clear(), which has produced files that PowerPoint
    # flags for repair in some cases.
    for i, it in enumerate(items):
        if i == 0:
            body.text = it["text"]
            p = body.paragraphs[0]
        else:
            p = body.add_paragraph()
            p.text = it["text"]
        p.level = it["level"]
        if it["subtitle"]:
            for r in p.runs:
                r.font.italic = True
                r.font.color.rgb = MUTED
                r.font.size = Pt(16)
    return s


def add_section_divider(title, subtitle=None):
    s = prs.slides.add_slide(LAY_SECTION)
    s.shapes.title.text = title
    for r in s.shapes.title.text_frame.paragraphs[0].runs:
        r.font.color.rgb = ACCENT
        r.font.bold = True
        r.font.size = Pt(44)
    if subtitle:
        tb = s.shapes.add_textbox(Inches(1), Inches(4), Inches(11.33), Inches(1))
        tf = tb.text_frame
        tf.text = subtitle
        for r in tf.paragraphs[0].runs:
            r.font.italic = True
            r.font.color.rgb = MUTED
            r.font.size = Pt(24)
    return s


# ---------------------------------------------------------------- slides
# Title
s = add_title_slide(
    "2026 ARRL Field Day",
    "UPARC · SPARC · WORMs · CARS  —  W4TA  —  Class 3A",
)
if os.path.exists(LOGO_STRIP):
    s.shapes.add_picture(LOGO_STRIP, Inches(2.5), Inches(5.5), height=Inches(1.4))

# Intro
add_bullets("What is ARRL Field Day?", [
    "Ham radio's annual open house",
    "Set up under field conditions",
    "40,000+ hams across N. America",
    "Public service + skill demo",
    "Annual since 1933",
])

add_bullets("Why we do it", [
    "Preparedness — deploy on demand",
    "Skill — pile-ups on every band",
    "Community — four clubs, one event",
    "Outreach — visitors welcome",
    "Fun — 24 hours of QSOs",
])

# Logistics
add_bullets("When & Where", [
    "June 27–28, 2026 (Sat – Sun)",
    "Clearwater Fire Station #48",
    "1700 N Belcher Rd., Clearwater, FL",
    "Indoors (except Satellite)",
    "ARRL Class: 3A",
])

add_bullets("Schedule", [
    "Setup: 8:00 AM Sat June 27",
    "Lunch: around noon",
    "Operating: 2:00 PM Sat → 2:00 PM Sun",
    "Teardown: 2:00 PM Sun June 28",
    "Dry-run: 9:00 AM Sat June 20",
    "Dry-run at Clearwater Fire Training Center",
])

add_bullets("Operating Modes & Bands", [
    "Modes: CW · SSB · FT8",
    "Bands: 6 m through 80 m",
    "Each station has a primary mode",
    "Other modes if conditions allow",
    "Bring your own wired headset",
    "3.5 mm or 1/4 inch plug",
])

# Station lineup
add_section_divider(
    "Station Lineup",
    "Three HF positions + VHF + Satellite",
)

add_bullets("Station 1 — Elecraft K4", [
    "Primary mode: SSB",
    "Native USB to laptop",
    "CESSB feature: 6–8 dB extra TX",
    "Best single-rig use is SSB",
    "InRad mic; Heil adapter optional",
])

add_bullets("Station 2 — Elecraft K3S", [
    "Primary mode: FT8 / digital",
    "External VGA monitor for waterfall",
    "DB9-to-USB adapter to laptop",
    "Also capable of SSB",
    "InRad mic; Heil adapter optional",
])

add_bullets("Station 3 — Elecraft K3 (CW)", [
    "Primary mode: CW",
    "WinKey Mini + Bencher paddle",
    "Paddle supplied by NY4I",
    "Coax: 65 ft RG-8X around room",
    "Also runs SSB and Digital",
])

add_bullets("VHF Station — Yaesu FT-897", [
    "Band: 6 m",
    "Brought by Paul KC4YDY",
    "Hand mic only (no Heil)",
    "Owns its own setup / power",
])

add_bullets("Satellite Station", [
    "ICOM IC-9700 transceiver",
    "Yaesu AZ/EL rotator",
    "Arrow yagi antenna",
    "Tracking / control device",
    "Operated outdoors",
])

# Logging / network
add_bullets("Logging Network — Overview", [
    "All HF laptops run TR4W",
    "Laptops on TRLOG WiFi (10.0.0/24)",
    "Pi 400 is the server",
    "Pi 400 wired to Linksys router",
    "Pi 400 address: 192.168.0.100",
    "UPS protects Pi + router",
], subtitle="Tom NY4I")

add_bullets("Pi 400 — What it runs", [
    "TR4W Server (Python)",
    "NTP — laptop time sync",
    "n1mm_view — stats images",
    "Local web UI on :8080",
    "rsync publisher → UPARC + SPARC",
    "Replaces old Windows server box",
], subtitle="Tom NY4I")

# Antennas
add_bullets("Antennas & Patch Panel", [
    "All feedlines go to patch panel",
    "Radios connect via the patch panel",
    "No coax changes without Band Boss",
    "Station 3: 65 ft RG-8X",
    "Routes east wall + top wall",
], subtitle="Ryan AF4O")

# Education
add_bullets("Education & Training Sessions", [
    "Welcome to Field Day (visitors)",
    "Ham Radio Basics",
    "Awards & Achievements",
    "EFHW kit antenna build",
    "Antenna Analyzer use",
    "All sessions led by Fred W2SUB",
], subtitle="Fred W2SUB")

# Hospitality
add_bullets("Meals — Saturday", [
    "Breakfast: donuts, coffee",
    "Lunch: burgers, dogs, salad, chips",
    "Dinner: TBD",
    "Bring a side dish to share",
], subtitle="Ron W4RFA")

add_bullets("Meals — Sunday", [
    "Breakfast: bagels (Tom), coffee",
    "Lunch: leftovers",
    "Water, tea, sodas all event",
    "Special diets: bring your own",
], subtitle="Ron W4RFA")

add_bullets("Meal Signup", [
    "Signup at www.uparc.org",
    "Deadline: 11:59 PM June 22",
    "Required for headcount",
    "No signup = no guaranteed meal",
])

# Visitors / members
add_bullets("Visitors Welcome", [
    "Field Day is a public event",
    "Watch the stations operate",
    "Talk to operators between QSOs",
    "Ask about licensing",
    "Education sessions all Saturday",
])

add_bullets("Members — Get Involved", [
    "Sign up for meals by June 22",
    "Attend the dry-run June 20",
    "Help setup Sat 8:00 AM",
    "Help teardown Sun 2:00 PM",
    "New operators paired with veterans",
    "Bring your own wired headset",
])

# Etiquette
add_bullets("Operating Etiquette", [
    "OPON when starting your shift",
    "Listen before calling",
    "Log every QSO immediately",
    "Check your station card first",
    "Have fun",
])

# Q&A
s = prs.slides.add_slide(LAY_SECTION)
s.shapes.title.text = "Q & A"
for r in s.shapes.title.text_frame.paragraphs[0].runs:
    r.font.color.rgb = ACCENT
    r.font.bold = True
    r.font.size = Pt(60)
tb = s.shapes.add_textbox(Inches(1), Inches(4), Inches(11.33), Inches(2))
tf = tb.text_frame
tf.text = "Questions?  Concerns?  Volunteers?"
for r in tf.paragraphs[0].runs:
    r.font.italic = True
    r.font.color.rgb = MUTED
    r.font.size = Pt(28)
p2 = tf.add_paragraph()
p2.text = ("Section leads — Ryan AF4O · Fred W2SUB · "
           "Tom NY4I · Paul KC4YDY · Ron W4RFA")
for r in p2.runs:
    r.font.color.rgb = MUTED
    r.font.size = Pt(18)

prs.save(OUT)
print(f"Saved {OUT}")
print(f"Slide count: {len(prs.slides)}")
