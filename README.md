# ATIP Decision Lens

Read the published outcomes of access complaints. Compare institutions, issues and findings while keeping the original reports close.

Open https://coolcode.ca/atipdecisions/

<!-- coolcode:guide -->
Filter an institution and Act section, then open a decision for its published finding and original report. Listing/release dates are separate from decision dates. Published decisions are selected reports, not all complaints.
<!-- /coolcode:guide -->

## Sources and interpretation

This index follows the Information Commissioner’s published decisions and final reports. These are selected publications, not the complete universe of complaints; institution counts cannot be treated as complaint rates or a performance league table.

Listing dates and verified decision dates are retained separately. Where the source does not provide a verified decision date, it remains unknown. Issues and findings reflect source labels or clearly identified text extraction.

Search covers the saved title, institution, Act sections and summary. Original report links remain the authoritative context. Quarterly statistics are separately linked or tabulated; their different denominators must not be mixed with selected-decision counts.

## Collection and archive

Schedule: **Weekly** (`43 7 * * 2`, UTC). GitHub schedules are best effort. Scheduled and manual runs collect, validate, commit dated snapshots and deploy. A first code push also collects if no saved dataset exists. Other code pushes rebuild the saved dataset offline.

`data/current.json` contains the latest normalized source records and metadata. `archive/YYYY-MM/*.json.gz` retains distinct captured versions; `data/history.json` lists them. Identical data checks update the check time without manufacturing a change. An initial capture is labelled baseline. Archive data is tracked in Git and does not expire with Actions artifacts. The site has snapshot selection, filtering, source detail, CSV export and an RSS change feed.

The default build needs no network. Failed source validation does not replace the published dataset. Optional `HEALTHCHECKS_PING_URL` sends start/success/failure pings for collection runs; no accuracy email is implied.

```sh
python3 -m pip install -r requirements.txt
python3 scripts/collect.py
node --test tests/*.test.mjs
python3 -m unittest discover -s tests -v
python3 scripts/build.py
```

## Privacy

Search and filters are local to the browser; no upstream request is made by filtering. Public data collection runs in GitHub Actions. The shared CoolCode counter records aggregate page opens, without searches or filter values. The explorer and collector run without Cloudflare changes. To enable shared visit counts and private issue reports, add `atipdecisions` to the existing `coolcode-visitor-api` Worker’s `toolList` and deploy it, if not already registered. See the [batch setup notes](https://github.com/jsdyer/jsdyer.github.io/blob/main/docs/tier1-tools.md).

## Software and attribution

Application code is MIT licensed; upstream data retains its original licence and attribution. Follow the source links for original records and terms.

<!-- schedule-reliability -->
## Schedule reliability

Public GitHub repositories can have scheduled workflows disabled after 60 days of inactivity. A separate weekly [schedule guard](.github/workflows/schedule-guard.yml) calls GitHub's enable-workflow API for an explicit list of refresh workflows and itself. It can restore workflows disabled for inactivity, preserves manually disabled workflows, and runs independently of collection failures.

This is an interim mitigation, not a scheduling guarantee: GitHub does not document active-workflow renewal as a permanent exemption, and scheduled runs can be delayed or dropped. A scheduler on our own Linux server is the planned independent trigger. The guard does not collect data, create dummy commits, or change source/check timestamps; successful collection and published data freshness still need monitoring.
<!-- /schedule-reliability -->
