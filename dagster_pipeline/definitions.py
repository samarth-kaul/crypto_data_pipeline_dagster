from dagster import Definitions
from dagster_pipeline.job import coingecko_etl_job
from dagster_pipeline.schedules import daily_crypto_schedule

defs = Definitions(
    jobs=[coingecko_etl_job],
    schedules=[daily_crypto_schedule]
)