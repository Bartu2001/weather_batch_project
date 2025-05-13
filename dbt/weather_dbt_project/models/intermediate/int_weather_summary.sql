{{ config(
    materialized = 'table',
    tags = ['intermediate']
) }}

-- Purpose: Calculate daily city-based weather summary metrics

with base as (

    select *
    from {{ ref('stg_weather_data') }}

),

aggregated as (
    
    select
    location_name,
    country,
    CAST(record_date AS DATE) as record_date,
    AVG(CAST(temperature_celsius AS FLOAT)) as avg_temp,
    AVG(CAST(feels_like_celsius AS FLOAT)) as avg_feels_like,
    AVG(CAST(humidity AS FLOAT)) as avg_humidity,
    AVG(CAST(uv_index AS FLOAT)) as avg_uv,
    AVG(CAST("air_quality_PM2_5" AS FLOAT)) as avg_pm25,
    AVG(CAST("air_quality_PM10" AS FLOAT)) as avg_pm10,
    AVG(CAST("air_quality_Ozone" AS FLOAT)) as avg_ozone
from {{ ref('stg_weather_data') }}
group by location_name, country, record_date

)

select * from aggregated
