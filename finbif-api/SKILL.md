---
name: finbif-api
description: General guide to the FinBIF (Finnish Biodiversity Information Facility) REST API at api.laji.fi. Use this skill whenever the user mentions FinBIF, laji.fi, Finnish biodiversity data, Finnish species observations, or is building anything that queries biodiversity/nature data from Finland. Covers authentication, pagination, rate limiting, error handling, and endpoint overview. This is the starting point — read this first for any FinBIF-related task.
---

# Purpose

This skill provides high-level information about the FinBIF API at `https://api.laji.fi`, which provides open data about biodiversity in Finland, hosted by the Finnish Biodiversity Information Facility (FinBIF).

If the task is clearly about one API area, prefer the matching specialized skill over this general skill:

- `finbif-occurrence` for occurrence search and filtering
- `finbif-taxonomy` for taxon lookup and taxonomic metadata
- `finbif-api-endpoints` for a list of all API endpoints and detailed information about each

# Using the FinBIF API

Every request must include API-Version and Accept headers:

`API-Version: 1`
`Accept: application/json`

Each entity in the API has a unique HTTP-URI identifier, for example `http://tun.fi/MX.123`. The identifier is usually prefixed with `http://tun.fi/`. Museum specimens have identifiers can have different prefixes, e.g. `http://id.luomus.fi`. Usually only the short qname format `MX.123` is used.

## Authentication

Every request must include Authorization header:

`Authorization: Bearer <ACCESS TOKEN>`

To obtain an access token:
1. Send a `POST` request with your email address to `/api-user` (see `api.laji.fi` for details).
2. FinBIF sends the access token to your email.
3. Store the token in a secure location and use it in all requests to the API.

Example:

```bash
curl -X 'GET' \
  'https://api.laji.fi/taxa' \
  -H 'Authorization: Bearer <ACCESS TOKEN>' \
  -H 'API-Version: 1' \
  -H 'Accept-Language: fi' \
  -H 'Accept: application/json'
```

Other token types exist and are not the same as the REST API access token:
- `Person-Token` (`Person-Token: <PERSON TOKEN>`) identifies the user. Required by endpoints that return logged-in user info or execute with user permissions.
- `Permission-Token` (`Permission-Token: <PERMISSION TOKEN>`) is system-specific and used with `/warehouse` for limited access to secured/private occurrence data according to the granted data request scope and validity period.

## Language

Use the standard `Accept-Language` header with values `en`, `fi`, or `sv`. Defaults to `en` if not specified.

## Pagination

Endpoints that return a large number of records (e.g. `/warehouse/query/unit/list`) support pagination.

Use the `page` and `pageSize` parameters to control the pagination.

Every response contains pagination metadata on the root level.

Example:

```json
{
  "currentPage": 1,
  "nextPage": 2,
  "lastPage": 6,
  "pageSize": 100,
  "total": 506,
  "results": [ ... ]
}
```

## Error handling

The API returns errors directly at the top level of the response body. Errors include an `errorCode` that allows clients to identify the type of error. Some errors messages are localized. Localized errors have property localized: true. These messages are intended for end users and can be displayed directly.

Example:

```json
{
	"message":"Your login is not valid. Please log out and log in again.",
	"errorCode":"PERSON_TOKEN_IS_INVALID",
	"localized":true
}
```

## Rate limiting and performance

Avoid making more than one request to the same endpoint per second. Don't make parallel requests to the same endpoint; it won't increase overall performance.

Use `cache=true` GET parameter unless you require data that is fresher than 1 hour.

## Test API

Test/development API at https://apitest.laji.fi has the same features as the production API but can have less data and some of it is be bogus test data. It is best to start with the test API and move on to the production API after your application is in stable state.

The test API may have bugs and new features that are not been noted in official documentation.

Important: The test API uses a different Access Token than the production API.

## Endpoints

The following are the most commonly used endpoints of the API. To see all endpoints and get more details about a specific endpoint, use the `finbif-api-endpoints` skill.

### Occurrence data (i.e. nature observations)

Use `finbif-occurrence` skill for more details about occurrence-related endpoints.

- `/warehouse` – Querying occurrence data from FinBIF data warehouse. Can be also used to send data to the data warehouse.
- `/collections` – Metadata about occurrence datasets/collections. All occurrences belong to one collection and the metadata provides information about the dataset.
- `/source` – Data source. Each occurrence has a source. The source might be an IT-system, but also an Excel spreadsheet copied to FinBIF for long term storage, etc.
- `/documents` – Metadata about occurrence documents. Each occurrence belongs to one document.
- `/images` – Images associated with occurrence records.
- `/audio` – Audio associated with occurrence records.

See `finbif-occurrence` skill for query examples.

### Taxonomy

Use `finbif-taxonomy` skill for more details about taxonomy-related endpoints.

- `/taxa` – Information about naming of organisms, classifying organisms in a hierarchical system or in taxonomic ranks, distribution data and biological interactions, identifiers across different systems, etc.
- `/informal-taxon-groups` – Informal groups may be taxonomic groups (such as Aves) or can be used to group similar species together (for example Aphyllophoroid fungi). Some species do not belong to any informal groups and some may belong to several. Informal groups can be used to filter taxa and occurrences.
- `/checklists` - Checklists taxa belong to
- `/autocomplete` - Autocomplete for taxa, persons, friends, etc.

See `finbif-taxonomy` skill for query examples.

### Other endpoints

- `/forms` - Notebook (Vihko forms)
- `/form-permissions` - Permissions for Notebook (Vihko forms)
- `/named-places` - Places associated with Vihko form and monitoring projects
- `/person` - Laji.fi users information
- `/api-user` - API user information
- `/annotations` - Annotations associated with occurrence records
- `/notifications` - Notifications sent for users regarding their obsrervations
- `/information` - Laji.fi information page content
- `/metadata` – Variable names, descriptions, ranges, enumeration values, etc. used in this API in three languages. This data can be browsed at http://schema.laji.fi in human readable format.
- `/areas` – Countries, Finnish municipalities, Finnish biogeographical provinces, etc.
- `/organizations` - Organizations owning datasets
- `/sound-identification` - Sound identification AI
- `/shorthand` - Shorthand for entering observations to Notebook (Vihko) forms
- `/sources` - Sources of occurrences, e.g. applications, Excel spreadsheets, etc.
- `/red-list-evaluation-groups` - Red list evaluation groups
- `/login` - For logging in users to native applications

Example: Get all alternative names as a lookup object where keys are property names and values are the alternative names:

```bash
curl -X 'GET' \
  'https://api.laji.fi/metadata/alts' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer <ACCESS TOKEN>' \
  -H 'Accept-Language: fi' \
  -H 'API-Version: 1'
```
