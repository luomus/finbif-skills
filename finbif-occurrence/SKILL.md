---
name: finbif-occurrence
description: Detailed guide to querying nature observations and biodiversity occurrence records through the FinBIF API at api.laji.fi. Use this skill when the user wants to search, filter, aggregate, count, or analyze species observations, museum specimen records, monitoring data, or any occurrence data from Finland. Also use when working with /warehouse, /collection, /source, /images, or /documents endpoints. Covers the Document→Gathering→Unit data model, all major warehouse query parameters, and common query patterns.
---

# Purpose

This skill provides detailed information about the occurrence-related endpoints. For general information about the FinBIF API and example usage, see the `finbif-api` skill. For detailed information about specific endpoints and their parameters, see the `finbif-api-endpoints` skill.

# Occurrence records on FinBIF

Finnish Biodiversity Information Facility (FinBIF) data warehouse holds about 60 million biodiversity occurrence records (i.e. nature observations), most of which are from Finland and from recent decades. They are very varied and compiled from over 30 different data sources and 600 datasets. They range from citizen science observations to museum specimen records and biodiversity monitoring data collected by research institutes.

95% of the occurrence records are open data and available in detailed format as FAIR data. The remaining 5% are available in a coarsened format for various reasons: species sensitivity, research embargo or by data owners' request. Coarsening makes coordinates and date information less detailed, and hides observer and notes fields.

# Data model

- Occurrence data follows a hierarhical data model: `Document` -> `Gathering` -> `Unit`.
  - `Document` is the top level entity containing metadata about how the data was collected, e.g. observer, date, collection, keywords, etc.
  - A document contains one or more gatherings. A gathering contains data about the collecting event, e.g. location names, coordinates/geometries, habitat information, collecting methods etc.
  - A `Gathering` contains one or more `Units`. A `Unit` contains data about the occurrence, e.g. taxon, count, notes, etc.
  - If both upper and lower level entities are present, lower level overrides upper level data.
- For museum specimens, `Document` is the specimen. It almost always contains one `Gathering` and one `Unit`, but there are exceptions.
- For nature observations, a `Document` is usually an event containing rich data about one to many observations i.e. `Units`.
- Images can be associated with any of the entities in the data model, but most commonly with `Units`.

# Important Endpoints

These are the most commonly used occurrence-related endpoints of the FInBIF API related to occurrence data.

## `/warehouse`

Querying occurrence data from FinBIF data warehouse. Can be also used to send data to the data warehouse. When working with occurrence data, use units as the primary entity.

**Shared parameters:**

- `pageSize` integer - Number of records to return per page. Default is 100. Maximum is 1000.
- `page` integer - Page number to return. Default is 1.
- `cache` boolean - Whether to use cached data.
- `useIdentificationAnnotations` boolean - Whether to include identifications changed by user annotations. Default is true.
- `includeSubTaxa` boolean - Whether to include sub-taxa of the given taxon.
- `includeNonValidTaxa` boolean - Whether to include non-valid taxa.
- `individualCountMin` integer - Minimum number of individuals in the unit.
- `includeNullLoadDates` boolean - Whether to include units with null load dates.
- `wild` string - Wildness. Byt default non-wild units are excluded.
- `qualityIssues` string - Quality issues. By default units with quality issues are excluded.

**Commonly used parameters:**

- `informalTaxonGroupId` string - Informal taxon group qname identifier.
- `informalTaxonGroupIdNot` string - Informal taxon group qname identifier to exclude.
- `countryId` string - Country qname identifier. Finland is `ML.206`.
- `time` string - Time range in ISO 8601 format or number of days before present (e.g. `-6/0` for the last week).
- `biogeographicalProvinceId` string - Biogeographical province qname identifier.
- `target` - Taxon name to search for. Multiple values are seperated by ','. When multiple values are given, this is an OR search.
- `finnish` boolean - Include only taxa defined as Finnish.
- `invasive` boolean - Include only invasive species.
- `sensitive` boolean - Include only sensitive species.
- `finnishMunicipalityId` string - Finnish municipality qname identifier.
- `timeAccuracy` integer - Include entries where time span in days is less or equal to the given value. Useful for fenology studies since excludes records with low time accuracy.
- `season` string - Day ignoring year. For example `1/59` gives all records for Jan-Feb.
- `collectionId` string - Collection qname identifier.

Tip: Easy way to get correct parameters for fetching occurrence records is to use the manual observation search UI at https://laji.fi/en/observation to explore what you want to fetch, then copy the URL and use the parameters from the URL.

Example: Fetch bird observations from Finland during the the last week:

```bash
curl -X 'GET' \
  'https://api.laji.fi/warehouse/query/unit/list?pageSize=100&page=1&cache=true&useIdentificationAnnotations=true&includeSubTaxa=true&includeNonValidTaxa=true&informalTaxonGroupId=MVL.1&countryId=ML.206&time=-6%2F0&individualCountMin=1&includeNullLoadDates=false&wild=WILD%2CUNKNOWN&qualityIssues=NO_ISSUES' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer <ACCESS TOKEN>' \
  -H 'API-Version: 1'
```

Example: Fetch observations from Uusimaa biogeographical province since 2000, aggregated by 10km YKJ grid cells:

```bash
curl -X 'GET' \
  'https://api.laji.fi/warehouse/query/unit/aggregate?aggregateBy=gathering.conversions.ykj10km.lat&aggregateBy=gathering.conversions.ykj10km.lon&pageSize=100&page=1&cache=false&useIdentificationAnnotations=true&includeSubTaxa=true&includeNonValidTaxa=true&biogeographicalProvinceId=ML.253&time=2000%2F2026&individualCountMin=1&includeNullLoadDates=false&wild=WILD%2CUNKNOWN&qualityIssues=NO_ISSUES' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer <ACCESS TOKEN>' \
  -H 'Accept-Language: fi' \
  -H 'API-Version: 1'
```

Example: Fetch a document using its document identifier `http://id.luomus.fi/C.318832`:

```bash
curl -X 'GET' \
  'https://api.laji.fi/warehouse/query/document?documentId=http%3A%2F%2Fid.luomus.fi%2FC.318832' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer <ACCESS TOKEN>' \
  -H 'Accept-Language: fi' \
  -H 'API-Version: 1'
```

Example: Fetch number of insect observations:

```bash
curl -X 'GET' \
  'https://api.laji.fi/warehouse/query/unit/count?cache=false&target=Insecta&useIdentificationAnnotations=true&includeSubTaxa=true&includeNonValidTaxa=true&individualCountMin=1&includeNullLoadDates=false&wild=WILD%2CUNKNOWN&qualityIssues=NO_ISSUES' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer <ACCESS TOKEN>' \
  -H 'Accept-Language: fi' \
  -H 'API-Version: 1'
```

## `/collection`

Metadata about occurrence datasets/collections. All occurrences belong to one collection and the metadata provides information about the dataset.

Example: Fetch collection metadata for the Notebook (Vihko) observation system collection with identifier `HR.1747`:

```bash
curl -X 'GET' \
  'https://api.laji.fi/collections/HR.1747' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer <ACCESS TOKEN>' \
  -H 'Accept-Language: fi' \
  -H 'API-Version: 1'
```

## `/images`

Images associated with occurrences records.

Example: Fetch an image using its qname identifier `MM.3668604`. You can get the image identifier from e.g. `/warehouse/unit/list` or `/warehouse/query/document` response.

```bash
curl -X 'GET' \
  'https://api.laji.fi/images/MM.3668604' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer <ACCESS TOKEN>' \
  -H 'API-Version: 1'
```