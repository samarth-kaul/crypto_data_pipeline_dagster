import pandas as pd
from datetime import datetime
import s3fs
import os
from src.utils.logger import get_logger
from src.config.config import config

logger = get_logger(__name__)

class DataLoader:
    def __init__(self):
        self.S3_BUCKET = config.S3_BUCKET
        self.S3_ENDPOINT = config.S3_ENDPOINT
        self.S3_ACCESS_KEY = config.S3_ACCESS_KEY
        self.S3_SECRET_KEY = config.S3_SECRET_KEY
        
    def load_data(self, df: pd.DataFrame, filename_prefix: str = "market_data"):
        timestamp = datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{filename_prefix}_{timestamp}.parquet"
        s3_path = f"{self.S3_BUCKET}/{filename}"

        logger.info(f"Uploading file to s3://{s3_path}...")

        try:
            # Initialize S3 FileSystem using s3fs
            fs = s3fs.S3FileSystem(
                key=self.S3_ACCESS_KEY,
                secret=self.S3_SECRET_KEY,
                client_kwargs={"endpoint_url": self.S3_ENDPOINT}
            )

            # Write to Parquet
            with fs.open(s3_path, 'wb') as f:
                df.to_parquet(f, engine='pyarrow', index=False)

            logger.info(f"Upload successful: {s3_path}")

        except Exception as e:
            logger.error(f"Error uploading file to S3: {str(e)}")
