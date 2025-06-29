import logging
from datetime import datetime

from src.extract.extract import DataExtractor
from src.transform.transform import DataTransformer
from src.load.load import DataLoader

logging.basicConfig(level=logging.INFO)

def run():
    data_extractor = DataExtractor()
    raw_data = data_extractor.extract_data()

    data_transformer = DataTransformer()
    df = data_transformer.transform_data(raw_data)

    data_loader = DataLoader()
    data_loader.load_data(df)

if __name__ == "__main__":
    run()
