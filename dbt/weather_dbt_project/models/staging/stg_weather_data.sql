{{ config(
    materialized = 'view',
    tags = ['staging']
) }}

with source as (

    select * 
    from {{ source('public', 'minio_weather_source') }}

),

cleaned as (

    select
        location_name,
        country,
        CAST(last_updated AS DATE) as record_date,
        temperature_celsius,
        feels_like_celsius,
        humidity,
        wind_kph,
        uv_index,
        "air_quality_PM2_5",
        "air_quality_PM10",
        "air_quality_Ozone",
        condition_text,
        visibility_km

    from source

)

select * from cleaned
