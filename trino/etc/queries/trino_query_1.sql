-- Query: Average Temperature per Country
SELECT country, AVG(temperature_celsius) as avg_temp
FROM postgresql.int_weather_summary
GROUP BY country
ORDER BY avg_temp DESC;
