import requests
from time import sleep
from src.config.config import config
from src.utils.logger import get_logger

logger = get_logger(__name__)

class DataExtractor:
    def __init__(self):
        self.base_url = config.BASE_URL

    def extract_data(self, pages: int = 1, per_page: int = 50):
        all_data = []

        for page in range(1, pages + 1):
            try:
                url = f"{self.base_url}/coins/markets"
                params = {
                    "vs_currency": config.CURRENCY,
                    "order": config.ORDER,
                    "per_page": per_page,
                    "page": page,
                    "sparkline": False
                }
                logger.info(f"Fetching page {page} from CoinGecko API...")
                response = requests.get(url, params=params, timeout=10)

                if response.status_code == 200:
                    data = response.json()
                    all_data.extend(data)
                else:
                    logger.warning(f"Failed to fetch page {page}: {response.status_code}")
                sleep(1)  # respect API rate limit

            except Exception as e:
                logger.error(f"Error fetching page {page}: {str(e)}")

        logger.info(f"Fetched total {len(all_data)} records.")
        return all_data
