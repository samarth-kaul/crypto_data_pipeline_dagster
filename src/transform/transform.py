import pandas as pd
from datetime import datetime
from src.utils.logger import get_logger
from src.config.config import config

logger = get_logger(__name__)

USD_TO_INR = 83.0  # mock conversion rate

class DataTransformer:
    def __init__(self):
        self.min_market_cap = config.MIN_MARKET_CAP
    
    def transform_data(self, raw_data: list) -> pd.DataFrame:
        logger.info("Transforming market data...")

        # Convert list of dicts → DataFrame
        df = pd.DataFrame(raw_data)

        # Select and rename required columns
        df = df[[
            "id", "symbol", "name",
            "current_price", "market_cap",
            "price_change_percentage_24h"
        ]].copy()

        # Clean data: remove rows with nulls in critical columns
        critical_columns = ['id', 'symbol', 'name', 'current_price', 'market_cap', 'price_change_percentage_24h']
        df = df.dropna(subset=critical_columns)

        # Add derived column
        df["market_cap_inr"] = df["market_cap"] * USD_TO_INR

        # Filter by market cap accordingly
        df = df[df['market_cap'] >= self.min_market_cap]

        # Add timestamp
        df["retrieved_at"] = datetime.utcnow().isoformat()

        # Optional: handle missing/null values
        df.fillna(0, inplace=True)

        logger.info(f"Transformed {len(df)} records successfully.")
        return df