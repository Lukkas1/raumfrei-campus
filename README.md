# Raumfrei
Static day calendar from 10 user-supplied room-plan images, captured 2026-09-30. Open `dist/index.html` directly or serve `dist/`. No installation, server, tracking or third-party runtime dependency.

The primary key is the room number. 110 occupied/uncertain blocks. `dist/data.json` contains the transcription; `dist/data.js` is the identical browser payload. The public version intentionally excludes source images. Source filenames are retained for traceability; source image URLs are null. `make_data.py` documents transcription. Regeneration requires Pillow and the original numbered uploads: `python make_data.py /path/to/originals`. The website itself needs neither Python nor the full originals. `node verify.cjs` checks schedule integrity and availability boundaries.

## Important source limitations
Weekly recurrence is an explicit model assumption: no semester validity dates are visible. No live university synchronization, access guarantee, holiday or vacation overrides. All weekends are unknown. Paper plans SI0001–SI0003/SI0201–SI0203 cover 08:00–20:00. SI0024/SI0025 cover through 19:30 in the implemented conservative day window. Digital screenshots cover 08:00–18:00, except the explicitly labelled SD0002 Tuesday 16:30–19:30 booking.

SD0002/SI0038 weekday headers are cropped; Monday–Sunday column assignment is tentative and called out in the UI. SI0024 Tuesday's last parallel algorithms block is not clearly readable; 18:00–19:30 is uncertainty, NOT a verified booking. Tuesday 11:00–11:30 in SI0024 and SI0025 follows printed event labels instead of row headings. Systemzeit is occupied. Empty visible cells mean plan-free only.

## GitHub Pages
The workflow `.github/workflows/pages.yml` verifies the schedules and deploys `dist/` on every push to `main`. In repository Settings → Pages, select GitHub Actions as the publishing source. All asset paths are relative and work at a project subpath. The deployment URL is reported by the workflow. GitHub Pages is configured to publish through this workflow.
