Business Use Case: City-Level Daily Weather Summary
In this project, we simulated a real-world request from a product manager to provide a dashboard-ready summary of daily weather and air quality by city.

Key requirements:

Clean and standardized staging models (dbt)
Aggregated intermediate models with city-level grouping
Metrics include temperature, humidity, wind, UV index, PM2.5 and PM10
Snapshots or historical tracking can be implemented for time-series monitoring
This was achieved using a modular dbt architecture with staging, intermediate, and marts layers. The staging layer filters and cleans raw data ingested via Airbyte, while the transformation logic is implemented in intermediate models.
