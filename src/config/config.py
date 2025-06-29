import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BASE_URL = os.getenv("COINGECKO_BASE_URL")
    CURRENCY = os.getenv("MARKET_CURRENCY", "usd")
    ORDER = os.getenv("MARKET_ORDER", "market_cap_desc")
    MIN_MARKET_CAP = int(os.getenv("MIN_MARKET_CAP", 1000000))
    ENDPOINT = os.getenv("COINGECKO_ENDPOINT")
    PER_PAGE = int(os.getenv("MARKET_PER_PAGE", 50))
    PAGES = int(os.getenv("MARKET_PAGES", 2))


    # S3/MinIO
    S3_ENDPOINT = os.getenv("MINIO_ENDPOINT")
    S3_ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY")
    S3_SECRET_KEY = os.getenv("MINIO_SECRET_KEY")
    S3_BUCKET = os.getenv("MINIO_BUCKET_NAME")

config = Config()
