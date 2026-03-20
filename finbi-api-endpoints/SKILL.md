---
name: finbif-api-endpoints
description: Detailed OpenAPI reference for every FinBIF API endpoint at api.laji.fi. Use this skill when you need exact parameter names, types, required fields, response schemas, or query string options for any specific endpoint. Contains a lookup table mapping each endpoint to its OpenAPI spec file. Use this after consulting finbif-api (general) or other skills when you need precise parameter-level detail to construct an API call correctly.
---

# Purpose

This skill provides detailed information about specific FinBIF API endpoints. For general information about the FinBIF API (e.g. authentication, pagination, error handling, etc.) and example usage, see the `finbif-api` skill.

# API Endpoints

The OpenAPI specification of the API is at https://api.laji.fi/openapi-json in OpenAPI 3.x JSON format. It is very large, so prefer using references associated with this skill.

Base URL for all endpoints is `https://api.laji.fi`

## Endpoint Eeference Files

`references` folder inside this skill contains OpenAPI spefication document of each endpoint. Each reference file is a JSON document containing the OpenAPI 3.x specification for that single endpoint. It includes:

- Parameter names, types, and descriptions
- Required vs optional parameters
- Response schema

To use, read the reference file for the endpoint you need, then extract the parameter details to construct your API call. Don't read reference files speculatively — only load the specific endpoint file you need for the task at hand.

METHOD | ENDPOINT_PATH | REFERENCE_FILE
GET | /forms/{id}/participants | references/get_forms_{id}_participants.json
GET | /forms | references/get_forms.json
POST | /forms | references/post_forms.json
GET | /forms/{id} | references/get_forms_{id}.json
PUT | /forms/{id} | references/put_forms_{id}.json
DELETE | /forms/{id} | references/delete_forms_{id}.json
POST | /forms/transform | references/post_forms_transform.json
GET | /person/profile | references/get_person_profile.json
POST | /person/profile | references/post_person_profile.json
PUT | /person/profile | references/put_person_profile.json
GET | /person/{id} | references/get_person_{id}.json
GET | /person | references/get_person.json
GET | /person/{id}/profile | references/get_person_{id}_profile.json
PUT | /person/friends/{id} | references/put_person_friends_{id}.json
DELETE | /person/friends/{id} | references/delete_person_friends_{id}.json
POST | /person/friends/{id} | references/post_person_friends_{id}.json
GET | /person/exists-by-email/{email} | references/get_person_exists-by-email_{email}.json
GET | /authentication-event | references/get_authentication-event.json
DELETE | /authentication-event | references/delete_authentication-event.json
GET | /notifications | references/get_notifications.json
PUT | /notifications/{id} | references/put_notifications_{id}.json
DELETE | /notifications/{id} | references/delete_notifications_{id}.json
GET | /metadata/classes | references/get_metadata_classes.json
GET | /metadata/classes/{class} | references/get_metadata_classes_{class}.json
GET | /metadata/classes/{class}/properties | references/get_metadata_classes_{class}_properties.json
GET | /metadata/properties | references/get_metadata_properties.json
GET | /metadata/properties/{property} | references/get_metadata_properties_{property}.json
GET | /metadata/properties/{property}/alt | references/get_metadata_properties_{property}_alt.json
GET | /metadata/alts | references/get_metadata_alts.json
GET | /metadata/alts/{alt} | references/get_metadata_alts_{alt}.json
GET | /collections | references/get_collections.json
GET | /collections/roots | references/get_collections_roots.json
GET | /collections/{id} | references/get_collections_{id}.json
GET | /collections/{id}/children | references/get_collections_{id}_children.json
GET | /context/{context} | references/get_context_{context}.json
GET | /form-permissions | references/get_form-permissions.json
GET | /form-permissions/{collectionID} | references/get_form-permissions_{collectionID}.json
POST | /form-permissions/{collectionID} | references/post_form-permissions_{collectionID}.json
PUT | /form-permissions/{collectionID}/{personID} | references/put_form-permissions_{collectionID}_{personID}.json
DELETE | /form-permissions/{collectionID}/{personID} | references/delete_form-permissions_{collectionID}_{personID}.json
POST | /documents/batch | references/post_documents_batch.json
GET | /documents/batch/{jobID} | references/get_documents_batch_{jobID}.json
POST | /documents/batch/{jobID} | references/post_documents_batch_{jobID}.json
POST | /documents/validate | references/post_documents_validate.json
GET | /documents/count/byYear | references/get_documents_count_byYear.json
GET | /documents/stats | references/get_documents_stats.json
GET | /documents | references/get_documents.json
POST | /documents | references/post_documents.json
GET | /documents/{id} | references/get_documents_{id}.json
PUT | /documents/{id} | references/put_documents_{id}.json
DELETE | /documents/{id} | references/delete_documents_{id}.json
POST | /named-places/{id}/reservation | references/post_named-places_{id}_reservation.json
DELETE | /named-places/{id}/reservation | references/delete_named-places_{id}_reservation.json
GET | /named-places | references/get_named-places.json
POST | /named-places | references/post_named-places.json
GET | /named-places/{id} | references/get_named-places_{id}.json
PUT | /named-places/{id} | references/put_named-places_{id}.json
DELETE | /named-places/{id} | references/delete_named-places_{id}.json
GET | /taxa/search | references/get_taxa_search.json
GET | /taxa | references/get_taxa.json
POST | /taxa | references/post_taxa.json
GET | /taxa/aggregate | references/get_taxa_aggregate.json
POST | /taxa/aggregate | references/post_taxa_aggregate.json
GET | /taxa/species | references/get_taxa_species.json
POST | /taxa/species | references/post_taxa_species.json
GET | /taxa/species/aggregate | references/get_taxa_species_aggregate.json
POST | /taxa/species/aggregate | references/post_taxa_species_aggregate.json
GET | /taxa/{id} | references/get_taxa_{id}.json
GET | /taxa/{id}/children | references/get_taxa_{id}_children.json
POST | /taxa/{id}/children | references/post_taxa_{id}_children.json
GET | /taxa/{id}/parents | references/get_taxa_{id}_parents.json
POST | /taxa/{id}/parents | references/post_taxa_{id}_parents.json
GET | /taxa/{id}/species | references/get_taxa_{id}_species.json
POST | /taxa/{id}/species | references/post_taxa_{id}_species.json
GET | /taxa/{id}/species/aggregate | references/get_taxa_{id}_species_aggregate.json
POST | /taxa/{id}/species/aggregate | references/post_taxa_{id}_species_aggregate.json
GET | /taxa/{id}/descriptions | references/get_taxa_{id}_descriptions.json
GET | /taxa/{id}/media | references/get_taxa_{id}_media.json
GET | /areas/{id} | references/get_areas_{id}.json
GET | /areas | references/get_areas.json
GET | /api-user | references/get_api-user.json
POST | /api-user | references/post_api-user.json
PUT | /api-user/{email} | references/put_api-user_{email}.json
POST | /images | references/post_images.json
GET | /images/{id} | references/get_images_{id}.json
PUT | /images/{id} | references/put_images_{id}.json
DELETE | /images/{id} | references/delete_images_{id}.json
GET | /images/{id}/large.jpg | references/get_images_{id}_large.jpg.json
GET | /images/{id}/square.jpg | references/get_images_{id}_square.jpg.json
GET | /images/{id}/thumbnail.jpg | references/get_images_{id}_thumbnail.jpg.json
POST | /images/{tempId} | references/post_images_{tempId}.json
POST | /audio | references/post_audio.json
GET | /audio/{id} | references/get_audio_{id}.json
PUT | /audio/{id} | references/put_audio_{id}.json
DELETE | /audio/{id} | references/delete_audio_{id}.json
GET | /audio/{id}/mp3 | references/get_audio_{id}_mp3.json
GET | /audio/{id}/thumbnail.jpg | references/get_audio_{id}_thumbnail.jpg.json
GET | /audio/{id}/wav | references/get_audio_{id}_wav.json
GET | /audio/{id}/flac | references/get_audio_{id}_flac.json
POST | /audio/{tempId} | references/post_audio_{tempId}.json
GET | /annotations/tags | references/get_annotations_tags.json
GET | /annotations | references/get_annotations.json
POST | /annotations | references/post_annotations.json
DELETE | /annotations/{id} | references/delete_annotations_{id}.json
GET | /information/index | references/get_information_index.json
GET | /information/{id} | references/get_information_{id}.json
GET | /information | references/get_information.json
GET | /checklists/{id} | references/get_checklists_{id}.json
GET | /checklists | references/get_checklists.json
GET | /checklist-versions/{id} | references/get_checklist-versions_{id}.json
GET | /checklist-versions | references/get_checklist-versions.json
GET | /organizations | references/get_organizations.json
GET | /organizations/{id} | references/get_organizations_{id}.json
GET | /informal-taxon-groups | references/get_informal-taxon-groups.json
GET | /informal-taxon-groups/tree | references/get_informal-taxon-groups_tree.json
GET | /informal-taxon-groups/roots | references/get_informal-taxon-groups_roots.json
GET | /informal-taxon-groups/{id} | references/get_informal-taxon-groups_{id}.json
GET | /informal-taxon-groups/{id}/children | references/get_informal-taxon-groups_{id}_children.json
GET | /informal-taxon-groups/{id}/parent | references/get_informal-taxon-groups_{id}_parent.json
GET | /informal-taxon-groups/{id}/siblings | references/get_informal-taxon-groups_{id}_siblings.json
POST | /sound-identification | references/post_sound-identification.json
GET | /autocomplete/persons | references/get_autocomplete_persons.json
GET | /autocomplete/friends | references/get_autocomplete_friends.json
GET | /autocomplete/taxa | references/get_autocomplete_taxa.json
GET | /shorthand/unit/trip-report | references/get_shorthand_unit_trip-report.json
GET | /shorthand/unit/list | references/get_shorthand_unit_list.json
GET | /shorthand/unit/line-transect | references/get_shorthand_unit_line-transect.json
GET | /shorthand/unit/water-bird-pair-count | references/get_shorthand_unit_water-bird-pair-count.json
GET | /sources/{id} | references/get_sources_{id}.json
GET | /sources | references/get_sources.json
GET | /red-list-evaluation-groups | references/get_red-list-evaluation-groups.json
GET | /red-list-evaluation-groups/tree | references/get_red-list-evaluation-groups_tree.json
GET | /red-list-evaluation-groups/roots | references/get_red-list-evaluation-groups_roots.json
GET | /red-list-evaluation-groups/{id} | references/get_red-list-evaluation-groups_{id}.json
GET | /red-list-evaluation-groups/{id}/children | references/get_red-list-evaluation-groups_{id}_children.json
GET | /red-list-evaluation-groups/{id}/parent | references/get_red-list-evaluation-groups_{id}_parent.json
GET | /red-list-evaluation-groups/{id}/siblings | references/get_red-list-evaluation-groups_{id}_siblings.json
GET | /login | references/get_login.json
POST | /login/check | references/post_login_check.json
POST | /warehouse/push | references/post_warehouse_push.json
DELETE | /warehouse/push | references/delete_warehouse_push.json
GET | /warehouse/query/document | references/get_warehouse_query_document.json
GET | /warehouse/query/document/aggregate | references/get_warehouse_query_document_aggregate.json
GET | /warehouse/query/gathering/aggregate | references/get_warehouse_query_gathering_aggregate.json
GET | /warehouse/query/gathering/statistics | references/get_warehouse_query_gathering_statistics.json
GET | /warehouse/query/unit/count | references/get_warehouse_query_unit_count.json
GET | /warehouse/query/unit/list | references/get_warehouse_query_unit_list.json
GET | /warehouse/query/unit/aggregate | references/get_warehouse_query_unit_aggregate.json
GET | /warehouse/query/unit/statistics | references/get_warehouse_query_unit_statistics.json
GET | /warehouse/query/annotation/list | references/get_warehouse_query_annotation_list.json
GET | /warehouse/query/unitMedia/list | references/get_warehouse_query_unitMedia_list.json
GET | /warehouse/query/sample/list | references/get_warehouse_query_sample_list.json
GET | /warehouse/query/annotation/aggregate | references/get_warehouse_query_annotation_aggregate.json
GET | /warehouse/enumeration-labels | references/get_warehouse_enumeration-labels.json
GET | /warehouse/enumeration-labels/{enumeration} | references/get_warehouse_enumeration-labels_{enumeration}.json
GET | /warehouse/filters | references/get_warehouse_filters.json
GET | /warehouse/filters/{filter} | references/get_warehouse_filters_{filter}.json
POST | /warehouse/polygon | references/post_warehouse_polygon.json
GET | /warehouse/polygon/{id} | references/get_warehouse_polygon_{id}.json


