---
name: finbif-datafile
description: Guide to working with FinBIF (Finnish Biodiversity Information Facility) biodiversity occurrence data packages downloaded from FinBIF or Laji.fi. Use this skill whenever the user is working with a FinBIF data download, occurrence records, occurrences.txt, or any file from a FinBIF data package — even if they only ask a simple question like "how do I read this file" or "what do these columns mean".
---

# FinBIF Data Package

A FinBIF data package is a ZIP archive of biodiversity occurrence records (nature observations and collected specimens) and associated files. The primary file is **occurrences.txt**.

## occurrences.txt — The Main Data File

Tab-separated (TSV), UTF-8 encoded. **Has 3 header rows — skip rows 2 and 3, use only row 1 (DwC field names) in code.**

```python
import pandas as pd
df = pd.read_csv("occurrences.txt", sep="\t", skiprows=[1, 2], low_memory=False)
```

Column reference: For field definitions, read `references/occurrences_columns.md` file. Load it when the user asks about specific columns, or when deciding which fields to use for a given purpose.

Key fields to know:
- `occurrenceID` — unique record identifier, used to join with supplementary files
- `scientificName` — taxon name
- `eventDate` — observation date(s)
- `decimalLatitude` / `decimalLongitude` — WGS84 coordinates
- `coordinateAccuracy` — spatial precision; filter on this for spatial analysis

## Other Files in the Package

| File | Contents |
|------|----------|
| `./facts/occurrence_facts.txt` | Extra per-occurrence attributes in long format (occurrenceID, fact, value) — join on `occurrenceID` |
| `./facts/event_facts.txt` | Extra per-event attributes in long format (eventID, fact, value) |
| `./media/occurrence_media.txt` | Media file metadata linked to occurrences |
| `samples.txt` | DNA/tissue sample records (if present) |
| `eml.xml` | Dataset metadata (title, creator, license, etc.) |
| `meta.xml` | Darwin Core Archive field mappings |

## Joining Supplementary Facts

`occurrence_facts.txt` and `event_facts.txt` use a long/narrow format — each row is one key-value pair for one occurrence. To attach facts to the main table:

```python
facts = pd.read_csv("facts/occurrence_facts.txt", sep="\t")
# Pivot to wide format, then merge
facts_wide = facts.pivot_table(index="occurrenceID", columns="fact", values="value", aggfunc="first")
df = df.merge(facts_wide, on="occurrenceID", how="left")
```

## Data Quality Notes

- Records come from many sources; quality and completeness vary significantly.
- Always check `coordinateAccuracy` before spatial analysis — some records have coarse or missing coordinates.
