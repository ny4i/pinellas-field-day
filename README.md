# Pinellas Field Day

Planning, site-setup documentation, network diagrams, and flyer assets for the
UPARC / Pinellas County ARRL Field Day operation.

## Repo contents

```
site-setup/         On-site logging and operating setup
  network.md          Logical network and station-to-rig assignment
  troubleshooting.md  Expected traffic on TRLOG, link/protocol reference
  setup-checklist.md  Phase-by-phase setup-day checklist (master)
  site-layout.drawio  Physical room floor plan
  operator-position.drawio  Per-station wiring detail (rig + peripherals)
  station-cards/      One-page printable setup card per station
    station-1-k4.md       K4 — SSB
    station-2-k3s.md      K3S — SSB / Digital + VGA monitor
    station-3-k3-cw.md    K3 — CW + WinKey + paddle
  reference/          Original OmniGraffle diagrams and ARRL FD packet/presentation
                      Includes Ryan AF4O's 2026 ARRL Field Day Presentation (.pptx)
                      which covers much of the same setup/operating info as these docs

brochures/          2026 Field Day flyer + club logos
  FieldDay2026-Flyer*.{pdf,jpg,png}   Final flyer in print and social formats
  build/              Working set used to render the flyer (SVG + PNGs)
  reference/          ARRL Field Day packet, DARA flyer used as design input
```

## Viewing the diagrams

The `.drawio` files (site-layout, operator-position, future cable-power) are
draw.io / diagrams.net XML. Three ways to view or edit them:

### 1. In a web browser — no install

Open <https://app.diagrams.net>, then **File → Open from device** and choose
the `.drawio` file. Works on any modern browser; no account needed.

To view a file directly from this repo without downloading first, use the
GitHub viewer URL pattern:

```
https://viewer.diagrams.net/?lightbox=1&edit=_blank&layers=1&nav=1&url=<raw-file-url>
```

### 2. Draw.io Desktop — local app

Free download, available for macOS, Windows, and Linux:

<https://github.com/jgraph/drawio-desktop/releases>

After installing, double-click any `.drawio` file to open it.

### 3. VS Code extension

Install the **"Draw.io Integration"** extension (publisher: Henning
Dieterichs) and `.drawio` files render inline in the editor.

## Viewing the markdown files

Markdown files (`*.md`) render natively on GitHub — just click them in the
web view. For local viewing, any markdown previewer works (VS Code preview,
Typora, MarkText, BBEdit's markdown preview, etc.).

The network diagram inside `site-setup/network.md` is a Mermaid block;
GitHub renders it inline. To render it locally, your markdown previewer
needs Mermaid support.
