from dagster import op, OpExecutionContext
from src.extract.extract import DataExtractor
from src.transform.transform import DataTransformer
from src.load.load import DataLoader
import pandas as pd


@op
def extract_op(context: OpExecutionContext) -> list:
    context.log.info("🚀 Starting data extraction from CoinGecko...")
    extractor = DataExtractor()
    data = extractor.extract_data(pages=2, per_page=50)
    context.log.info(f"✅ Extracted {len(data)} records from API.")
    return data

@op
def transform_op(context: OpExecutionContext, raw_data: list) -> pd.DataFrame:
    context.log.info("🔄 Starting data transformation...")
    transformer = DataTransformer()
    df = transformer.transform_data(raw_data)
    context.log.info(f"✅ Transformation complete. Final row count: {len(df)}")
    return df

@op
def load_op(context: OpExecutionContext, df: pd.DataFrame) -> None:
    context.log.info("📦 Starting data upload to MinIO (S3)...")
    loader = DataLoader()
    loader.load_data(df)
    context.log.info("✅ Data successfully uploaded to MinIO.")
