# 🧠 Crypto Market ETL Pipeline with Dagster, MinIO & Docker

A professional, production-grade **data engineering project** that demonstrates end-to-end ETL pipeline design using **Dagster**, **MinIO (S3-compatible object store)**, and **Docker**.

This project extracts structured crypto market data from the **CoinGecko API**, performs cleansing and transformation, and stores the processed data as **Parquet files in MinIO**.

---

## 🚀 Features

- ✅ Modular, scalable, and professional pipeline design
- 🧱 **ETL Pipeline**: Extract → Transform → Load
- 🕹️ **Dagster** for orchestration, manual + scheduled jobs
- 🪣 **MinIO** for object storage (S3 replacement)
- 🐳 **Dockerized** for portability and reproducibility
- 🛠️ **CI/CD-ready** structure (GitHub Actions pipeline coming soon)
- 📂 Clean and structured Python codebase with logging, config management, and `.env` usage

---

## 🧩 Tech Stack

| Component         | Tech Used                       |
|------------------|----------------------------------|
| Orchestration     | [Dagster](https://dagster.io/)   |
| Object Storage    | [MinIO](https://min.io/)         |
| API Source        | [CoinGecko](https://coingecko.com/) |
| File Format       | Parquet via `pyarrow`            |
| DevOps            | Docker, Git, GitHub              |
| Logging & Config  | Python `logging`, `dotenv`       |

---

## 📁 Project Structure

dagster_crypto_etl_pipeline/
├── dagster_pipeline/ 
│ ├── job.py
│ ├── schedules.py
│ └── definitions.py
├── src/ 
│ ├── extract/ 
│ ├── transform/ 
│ ├── load/ 
│ ├── config/ 
│ └── utils/ 
├── .env
├── requirements.txt
├── README.md
└── dagster.yaml 


## ⚙️ How It Works

### 1. Extract

- Uses `requests` to pull paginated crypto market data from CoinGecko's `/coins/markets` API.
- Respects rate limits using `sleep`.

### 2. Transform

- Cleans the raw data, removes nulls, selects relevant columns.
- Applies a mock **USD to INR conversion**, filters by market cap, adds timestamps.

### 3. Load

- Writes the transformed DataFrame as **Parquet** to MinIO using `s3fs` and `pyarrow`.
- S3 paths are dynamically timestamped for each run.

---

## 🧪 Run the Pipeline

### ▶️ Manually (Local)

dagster dev

### ▶️ Automatically (Scheduled)

dagster-daemon run

