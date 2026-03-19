---
name: finbif-taxonomy
description: Use FinBIF API to retrieve taxonomical data, e.g. taxa, species names, taxonomic ranks, etc. Apply when user asks for taxonomic information.
---

# Purpose

This skill provides detailed information about the taxonomy-related endpoints. For general information about the FinBIF API (e.g. authentication, pagination, error handling, etc.), see the `finbif-api` skill.

# Taxonomy on FinBIF

Finnish Biodiversity Information Facility (FinBIF) data warehouse holds data about 40.000 species and their taxonomic relationships, mostly from Finland.

Each taxon concept has a unique identifier in the format `http://tun.fi/MX.123`. Often only the short qname format `MX.123` is used.

## Important Endpoints

These are the most commonly used taxonomy-related endpoints of the FInBIF API. See `http://api.laji.fi` for full details.

### `/taxa`

Information about naming of organisms, classifying organisms in a hierarchical system or in taxonomic ranks, distribution data and biological interactions, identifiers across different systems, etc.

### `/informalTaxonGroup`

Informal groups may be taxonomic groups (such as Aves) or can be used to group similar species together (for example Aphyllophoroid fungi). Some species do not belong to any informal groups and some may belong to several. Informal groups can be used to filter taxa and occurrences.