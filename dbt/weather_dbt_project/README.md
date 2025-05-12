Welcome to your new dbt project!

### Using the starter project

Try running the following commands:
- dbt run
- dbt test


### Resources:
- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [chat](https://community.getdbt.com/) on Slack for live discussions and support
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices



### Business Use Case: City-Level Daily Weather Summary

In this project, we simulated a real-world request from a product manager to provide a dashboard-ready summary of daily weather and air quality by city.

Key requirements:
- Clean and standardized staging models (dbt)
- Aggregated intermediate models with city-level grouping
- Metrics include temperature, humidity, wind, UV index, PM2.5 and PM10
- Snapshots or historical tracking can be implemented for time-series monitoring

This was achieved using a modular dbt architecture with `staging`, `intermediate`, and `marts` layers. The staging layer filters and cleans raw data ingested via Airbyte, while the transformation logic is implemented in intermediate models.
