# from dagster import ScheduleDefinition, define_asset_job

# # 1. Define a job that materializes our asset
# crypto_data_job = define_asset_job("crypto_data_job", selection=["crypto_market_data"])

# # 2. Define a schedule that runs this job daily
# daily_crypto_schedule = ScheduleDefinition(   
#     job=crypto_data_job,
#     cron_schedule="0 8 * * *",  # Everyday at 08:00 AM
# )

from dagster import schedule
from .job import coingecko_etl_job

@schedule(
    # cron_schedule="0 7 * * *",  # Runs every day at 07:00 UTC (12:30 PM IST)
    cron_schedule= "*/2 * * * *",
    job=coingecko_etl_job,
    execution_timezone="UTC"
)
def daily_crypto_schedule(_context):
    return {}
