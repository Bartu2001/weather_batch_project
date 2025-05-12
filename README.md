# 🌦️ Weather Batch Project – A Real-World Data Pipeline Simulation

This project simulates a real-world daily batch pipeline that processes weather data using modern data engineering tools. It covers the full cycle from ingestion to transformation to visualization and analytics.



---

## 🔧 Core Stack

- **PostgreSQL**: Stores raw and transformed weather data  
- **Airbyte**: Ingests external data sources (e.g., weather APIs) into PostgreSQL  
- **DBT**: Transforms and models the data for analytics  
- **MinIO**: Acts as a cloud-like object store (S3-compatible)  
- **Metabase**: Visualizes the insights via dashboards  
- **Trino**: Enables powerful distributed SQL analytics  

This project is fully orchestrated using **Docker Compose** and mimics a production-grade pipeline with modular and scalable components.

Designed for:

- 💡 Junior data engineers wanting to learn batch data architecture  
- 🧠 Professionals building a portfolio project  
- 📚 Anyone exploring open-source data tools in action  

---

## 🧩 Architecture Overview

This project uses the following stack:

| Tool           | Purpose                                            |
| -------------- | -------------------------------------------------- |
| **Airbyte**    | Ingest weather data into PostgreSQL                |
| **PostgreSQL** | Raw & transformed data storage                     |
| **DBT**        | SQL-based data transformation & modeling           |
| **MinIO**      | Object storage (simulated S3)                      |
| **Trino**      | Federated SQL engine for querying multiple sources |
| **Metabase**   | Interactive dashboard & data visualization         |

---

## 🚀 Project Flow

1. **Data Ingestion**

   * **Source**: Weather API via Airbyte
   * **Destination**: PostgreSQL (`weather_db`)

2. **Transformation**

   * Staging & Intermediate layers with **DBT**
   * Snapshot support available

3. **Storage**

   * Final datasets stay in PostgreSQL
   * MinIO used for object storage simulation (if needed)

4. **Federated Queries**

   * Trino connects to PostgreSQL
   * Enables performant SQL queries across sources

5. **Visualization**

   * **Metabase** connects to `weather_db`
   * Dashboards for temperature, PM2.5, UV risk, etc.

---


---

## 📊 Key Metabase Dashboards

* **City-Based Avg. Temperature**
* **Top 10 Hottest Cities**
* **Average PM2.5 by Country**
* **Air Pollution Rankings by City**
* **Extreme UV Risk Locations**
* **Weather Pattern Snapshot**

---

## ⚙️ How to Run

1. Clone the repo:

```bash
git clone https://github.com/Bartu2001/weather_batch_project.git
cd weather_batch_project
```

2. Launch all services:

```bash
docker compose up -d --build
```

3. Access services:

| Service    | URL                                            |
| ---------- | ---------------------------------------------- |
| Metabase   | [http://localhost:3000](http://localhost:3000) |
| Trino UI   | [http://localhost:8080](http://localhost:8080) |
| MinIO      | [http://localhost:9001](http://localhost:9001) |
| Airflow UI | [http://localhost:8081](http://localhost:8081) |

---

## 🧠 Notes

* **MinIO**, **Airbyte**, and **Metabase** are inside containers.
* Trino configuration located at `trino/etc/`.
* DBT models live under `dbt/weather_dbt_project/models/`.
* `airflow/dags/airbyte_dag.py` simulates orchestration.

> This project simulates a real-world daily weather pipeline and can be easily extended for production use.

---

Made with ☀️ by Bartu Tanacan
