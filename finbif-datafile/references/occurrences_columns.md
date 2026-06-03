| Column | Label | Definition |
| --- | --- | --- |
| occurrenceID | Occurrence ID | A unique identifier for the occurrence. |
| eventID | Event ID | A unique identifier for the event/gathering during which the occurrence record was made. |
| parentEventID | Specimen ID / Parent Event ID | A unique identifier for a preserved specimen or an observation submission. For collection specimens, this refers to the identifier of the physical item (e.g., a pinned insect or a plant sheet). In the case of an observation submission, this is the identifier for the entity that links together observations and collection events. |
| verbatimIdentification | Verbatim Identification | The taxonomic identification as it appeared in the original record. |
| recordedBy | Recorded By / Collector | Names of people, groups, or organizations that observed or collected the occurrence ("leg"). |
| identifiedBy | Identified By | The name of the person responsible for the currently used taxon identification. |
| taxonConceptID | Taxon Concept ID | A persistent and unique identifier for the taxonomic concept to which the occurrence is currently linked. |
| scientificName | Scientific Name | The full scientific name of the taxon concept to which the occurrence is currently linked. |
| scientificNameAuthorship | Scientific Name Authorship | The author(s) who originally described and published the scientific name of the taxon concept the occurrence is currently linked to. |
| taxonRank | Taxon Rank | The taxonomic rank or level of the organism in the classification hierarchy of the taxon to which the occurrence is currently linked. |
| kingdom | Kingdom | The full scientific name of the kingdom in which the taxon is classified. |
| class | Class | The full scientific name of the class in which the taxon is classified. |
| order | Order | The full scientific name of the order in which the taxon is classified. |
| family | Family | The full scientific name of the family in which the taxon is classified. |
| informalTaxonGroup | Informal Taxon Group | Informal groups the occurrence is currently linked to. |
| vernacularName | Vernacular Name (Finnish) | The recommended common name in Finnish of the taxon to which the occurrence is currently linked. |
| vernacularNameSwedish | Vernacular Name (Swedish) | The recommended common name in Finland Swedish (according to FinBIF taxonomy) of the taxon to which the occurrence is currently linked. |
| redListStatusFinland | Red List Status (Finland) | The most recently assessed Finnish regional Red List status for the taxon to which the occurrence is currently linked. |
| lajiturvaStatus | Lajiturva Status | A classification defined for the use of forest and nature management solutions, in which species are categorized into three classes: legally protected ("Lakisääteinen"), threatened ("Uhanalainen"), and near threatened ("Silmälläpidettävä"). This is the classification of the taxon to which the occurrence is currently linked. |
| regulatoryStatuses | Regulatory Statuses | The regulatory statuses or other species lists for the taxon to which the occurrence is currently linked. |
| taxonPreferredHabitat | Taxon Preferred Habitat | The primary habitat for the taxon to which the occurrence is currently linked. |
| habitat | Occurrence Habitat | The habitat as reported by the original observer. |
| isSensitiveTaxon | Is Sensitive Taxon | Is the occurrence currently linked to a taxon that is classified as sensitive in FinBIF. |
| dataGeneralizations | Data Generalizations | The indicator of level of data generalization of the occurrence record incuding geographic aggregation. |
| informationWithheld | Information Withheld | The reason or reasons why data associated with the record (time, location, personal information) has been restricted. |
| datasetCurationLevel | Dataset Curation Level | Describes the overall quality and reliability of the dataset or collection the occurrence record belongs to. The curation level is based on the origin of the data — such as whether the records were submitted by professionals, expert amateurs, or citizen observers — as well as the extent of any post-submission curation applied to the dataset. |
| identificationVerificationStatus | Identification Verification Status | Describes the reliability and trustworthiness of this individual occurrence record, based on both the original data source’s quality rating and subsequent quality control assessments by FinBIF. |
| qualityControl | Quality Control Tags | More precise quality control tags currently applied to this individual occurrence record (from the original data source, FinBIF quality assessment, automated validations, etc.) |
| datasetID | Dataset ID | A unique identifier for the dataset or specimen collection in which the information about this occurrence/specimen is stored. |
| datasetName | Dataset Name | The name of the dataset or collection. |
| source | Source ID | A unique identifier for the source information data system in which the information about this occurrence/specimen is stored. |
| sourceName | Source Name | The name of the information data source. |
| originatingSource | Originating Source | Information about where the data was originally recorded in the source system or where it originates from / how it was delivered to the source system. |
| eventDate | Event Date | The date-time or interval during which the occurrence was made or specimen collected. |
| countryCode | Country | The standard code for the country in which the occurrence was made/specimen collected. |
| biogeographicalProvince | Biogeographical Province | The Finnish biogeographical province in which the occurrence was made/specimen collected. Resolved from reported provice or by coordinates. |
| county | County | The name of the county, municipality, or the next smaller administrative unit below state or province where the occurrence was made or the specimen was collected. Originally reported municipality (verbatim) or in Finland the names of municipalities resolved from coordinates. |
| verbatimLocality | Verbatim Locality | The higher geography, country, province, biogeographical province, second order division and locality as reported in the original occurrence. |
| locationID | Site ID | A unique identifier for a monitoring site such as bird monitoring route or LajiGIS species monitoring or survey site in which this occurrence was made. |
| locationName | Site Name | The name of a monitoring site, such as a bird monitoring route or LajiGIS species monitoring or survey site, in which this occurrence was made. |
| locationType | Site Type | The type of the monitoring site or route as described in the original data source (in Finnish). |
| locationStatus | Site Status | The status of the monitoring site at the time of the occurrence, or in some cases its current status, as reported by the original data source (in Finnish). |
| basisOfRecord | Basis of Record | The specific nature of the data record, indicating the type of evidence the occurrence is based on. |
| lifeStage | Life Stage | The age class or life stage of the biological individual(s), or other type of evidence, represented in the occurrence. |
| sex | Sex | The sex of the biological individual(s) represented in the occurrence. |
| femaleIndividualCount | Female Individual Count | The number of female individuals represented in the occurrence record. |
| maleIndividualCount | Male Individual Count | The number of male individuals represented in the occurrence record. |
| organismQuantity | Abundance | Numeric or textual representation for the quantity of organisms. |
| organismQuantityType | Abundance Unit | The type of quantification system used for the quantity of organisms. |
| individualCount | Interpreted Individual Count (min) | The interpreted minimum number of individuals present at the time of the occurrence. For absence records, this is zero; for all others, it is at least one. |
| pairCount | Pair Count | Reported or interpreted pair count. Mostly for birds. |
| isMigrating | Migration Status | Indicates whether the individual is migrating (true) or local (false) at the time of observation. |
| isBreedingSite | Breeding Site | Indicates whether the individual was observed at a breeding site (true). A breeding site may be a nest, a spawning ground, or another location used for reproduction. |
| invasiveTaxonManagementAction | Invasive Taxon Management Action | Indicates the observed outcome of management actions taken to control or eradicate an invasive species at the site. |
| dnaSequence | DNA Sequence | DNA sequences associated with the occurrence, stored in FASTA format. |
| atlasCode | Breeding Bird Atlas Code | A description of the breeding behavior or indirect evidence shown by the subject taxon at the time of the occurrence. |
| atlasClass | Breeding Bird Atlas Class | The reproductive condition of the biological individual(s) represented in the occurrence. Derived from the Atlas Code. |
| dynamicProperties | Additional Attributes | A list of additional measurements, facts, characteristics, or assertions related to the occurrence record. |
| georeferenceSources | Coordinate Source | The origin of the coordinates: either directly reported as coordinates or as a geometry, or interpreted from the name of a Finnish municipality or former municipality. |
| isStateLand | State Land | This field indicates whether the occurrence is located entirely on state-owned land or not. It distinguishes occurrences as either on state land (true) or on non-state land / very close to non-state land (false, including buffered areas). |
| coordinateAccuracy | Coordinate Accuracy (m) | The largest distance (in meters) defining the smallest bounding box that contains the entire location of the occurrence. |
| footprintWKT | Footprint WKT | A Well-Known Text (WKT) representation of the shape (footprint or geometry) that defines the occurrence or observation area. The geometry is expressed in the WGS84 coordinate reference system. |
| decimalLatitude | Decimal Latitude | The geographic latitude (in decimal degrees, expressed in the WGS84 coordinate reference system) of the geographic center of the occurrence area. Positive values are north of the Equator, negative values are south of it. Valid range: -90 to 90. |
| decimalLongitude | Decimal Longitude | The geographic longitude (in decimal degrees, expressed in the WGS84 coordinate reference system) of the geographic center of the occurrence area. Positive values are east of the Greenwich Meridian, negative values are west of it. Valid range: -180 to 180. |
| gridCellYKJ | YKJ 10km Grid Cell | The 10-km grid cell in the Finnish Uniform Coordinate System (YKJ), based on the center point of the occurrence area. |
| occurrenceRemarks | Occurrence Remarks | Free-text comments or notes about the occurrence. |
| eventRemarks | Event Remarks | Free-text comments or notes about the observation or collection event, or the documentation process. |
| otherCatalogNumbers | Additional IDs | Additional identifiers associated with the occurrence record. These may include specimen IDs, collection catalog numbers, database-specific identifiers, or other codes relevant to the observation or specimen. |
| availableDate | Date Available in FinBIF | The date when the resource (e.g., a document, dataset, or observation) was made available or received by FinBIF (Finnish Biodiversity Information Facility). This typically indicates when the data was first accessible in the FinBIF system. |
| license | License | The legal license under which the resource (e.g., document, dataset, or observation) is published or made available. This defines the terms of use, permissions, and restrictions associated with the resource. |
| qualityIssues | Quality Issues | For records marked as erroneous, this field describes the reason(s) why the record has been classified as erroneous. Issues may relate to species identification, location, time, observer information, or other critical errors affecting data quality. |
