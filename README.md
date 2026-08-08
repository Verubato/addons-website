# Verz Addons Website

Static informational website for all of Verz's World of Warcraft addons, served
at [miniaddons.com](https://miniaddons.com) and
[verzaddons.com](https://verzaddons.com).

No backend and no build tooling required to host it; everything under `docs/`
is plain HTML, CSS and JS. GitHub Pages serves the `docs/` folder; any other
static file host can do the same.

## Editing

`docs/index.html` is generated. To add or change an addon, edit the `ADDONS`
list in `scripts/GenerateSite.py` and run:

```
python scripts/GenerateSite.py
```

Addon icons live in `docs/assets/icons/`, copied from each addon repo's
`assets/Icons/Icon.svg` (or the largest PNG where no SVG exists). Featured
screenshots are hotlinked from the addon repos on GitHub.

CurseForge links use the `https://www.curseforge.com/projects/<id>` redirect
form, with IDs taken from each addon's TOC `X-Curse-Project-ID` field.
