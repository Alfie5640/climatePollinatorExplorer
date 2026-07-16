# Climate–Pollinator Explorer

An interactive geospatial platform exploring how changing climate conditions influence pollinator habitat suitability across the UK.

The project combines climate and environmental datasets to create an explainable **Pollinator Suitability Index**. Instead of predicting pollinator populations, it identifies areas experiencing climate stress or favourable conditions based on temperature, drought, vegetation, habitat, and seasonal factors.

## Overview

The platform integrates:

- ERA5 climate reanalysis data
- SPEI drought indicators
- NDVI vegetation indices
- Land cover data
- Flowering season information
- Buglife B-Lines habitat networks

These datasets are combined to produce spatial suitability scores that can be explored over time.

## Suitability Index

The current suitability score combines:

- **Heat suitability** — temperature conditions for pollinators
- **Drought suitability** — water stress conditions using SPEI
- **Habitat quality** — land cover based habitat availability
- **Vegetation condition** — NDVI based vegetation activity

## Example Output

heat_suitability:        0.69
drought_suitability:     1.00
habitat_quality:         0.20
pollinator_suitability:  0.14

scores are normalized:
0 = unsuitable conditions
1 = favourable conditions

