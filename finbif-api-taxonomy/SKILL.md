---
name: finbif-taxonomy
description: Detailed guide to looking up species names, taxonomy, data, and classification through the FinBIF API at api.laji.fi. Use this skill when the user wants to find a taxon ID (MX code), look up species by scientific or common name, browse taxonomic hierarchies, get red list evaluations, find informal taxon groups, or work with /taxa, /informal-taxon-groups, /checklists, or /autocomplete/taxa endpoints. Also use when the user needs to resolve a species name to an identifier.
---

# Purpose

This skill provides detailed information about the taxonomy-related endpoints. For general information about the FinBIF API (e.g. authentication, pagination, error handling, etc.), see the `finbif-api` skill. For detailed information about specific endpoints and their parameters, see the `finbif-api-endpoints` skill.

# Taxonomy on FinBIF

Finnish Biodiversity Information Facility (FinBIF) data warehouse holds data about 40.000 species mostly from Finland.

Each taxon concept has a unique identifier (informally known as MX-code) in the format `http://tun.fi/MX.123`. Often only the short qname format `MX.123` is used.

# Endpoints

- `/taxa` – Information about naming of organisms, classifying organisms in a hierarchical system or in taxonomic ranks, distribution data and biological interactions, identifiers across different systems, etc.
- `/informal-taxon-groups` – Informal groups may be taxonomic groups (such as Aves) or can be used to group similar species together (for example Aphyllophoroid fungi). Some species do not belong to any informal groups and some may belong to several. Informal groups can be used to filter taxa and occurrences.
- `/checklists` - Checklists taxa belong to
- `/autocomplete` - Autocomplete for taxa, persons, friends, etc.

## `/taxa`

Information about naming of organisms, classifying organisms in a hierarchical system or in taxonomic ranks, distribution data and biological interactions, identifiers across different systems, etc.

**Shared parameters:**

- `includeMedia` boolean - Whether to include links to media files.
- `includeDescriptions` boolean - Whether to include descriptions, e.g. about ecology and identification of the taxon.
- `includeRedListEvaluations` boolean - Whether to include IUCN Red List evaluations.
- `checklistVersion` string - Checklist version to use. Almost always it's best to use the `current` version.

**Commonly used parameters:**

Example: Get information about Whooper Swan (Cygnus cygnus) taxon with qname `MX.26280`:

```bash
curl -X 'GET' \
  'https://api.laji.fi/taxa/MX.26280?includeMedia=false&includeDescriptions=false&includeRedListEvaluations=false&checklistVersion=current' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer <ACCESS TOKEN>' \
  -H 'Accept-Language: fi' \
  -H 'API-Version: 1'
```

## `/informalTaxonGroup`

Informal groups may be taxonomic groups (such as Aves) or can be used to group similar species together (for example Aphyllophoroid fungi). Some species do not belong to any informal groups and some may belong to several. Informal groups can be used to filter taxa and occurrences.