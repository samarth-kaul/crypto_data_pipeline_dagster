# from dagster import Definitions
# from dagster_pipeline.assets import crypto_market_data

# defs = Definitions(
#     assets=[crypto_market_data], 
# )

from .job import coingecko_etl_job
from dagster import Definitions
from dagster_pipeline.schedules import daily_crypto_schedule

defs = Definitions(
    jobs=[coingecko_etl_job],
    schedules=[daily_crypto_schedule]
)