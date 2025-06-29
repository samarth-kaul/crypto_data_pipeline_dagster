from dagster import job
from .ops import extract_op, transform_op, load_op

@job
def coingecko_etl_job():
    load_op(transform_op(extract_op()))
