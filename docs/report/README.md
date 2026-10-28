# Technical report

**EnviroBot: A Mobile Robotic Arm that Detects and Picks Up Waste —
Design, YOLOv8 Waste Detection and Prototype.** Version 1.0, October 2026.

By Jewel Nath, Tasmiara Jahan Toma and Tanjina Akter (Comilla University).

[Read the PDF](envirobot-report.pdf) (14 pages, one column).

It describes EnviroBot's mechanical build, electronics, phone control, arm
model and YOLOv8 waste detection, the team's evaluation of the detector, the
behaviours recorded on video in 2024, and the next steps. Its numbers come
from the team's project report, the circuit diagram and this repository.

Every diagram is also in [docs/diagrams/](../diagrams/README.md) as its own PDF
and PNG, for reuse.

## Files

| Path | What it is |
|---|---|
| `envirobot-report.tex` | The report |
| `style.tex` | The page layout: one column, 11 pt, coloured headings and summary boxes |
| `figure-style.tex` | Fonts, the colour palette and the TikZ styles every figure shares |
| `references.bib` | The references; every DOI was checked at doi.org |
| `figures/` | One file per diagram (`figNN-*.tex`, TikZ) or plot (`plotNN-*.tex`, pgfplots), each naming the source it was drawn from |
| `make-diagrams.py` | Builds each figure as its own cropped PDF in `docs/diagrams/` |
| `envirobot-report.pdf` | The built report |

The photos and video frames come from [docs/media/](../media/). The report
and its diagrams are under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/);
the code keeps its MIT licence.

## Build it

With [Tectonic](https://tectonic-typesetting.github.io), which fetches the
LaTeX packages and the TeX Gyre fonts it needs on the first run:

```bash
cd docs/report
tectonic -X compile envirobot-report.tex
python make-diagrams.py
```

The style uses `fontspec`, so another TeX distribution needs XeLaTeX or
LuaLaTeX (`latexmk -xelatex envirobot-report.tex`).
