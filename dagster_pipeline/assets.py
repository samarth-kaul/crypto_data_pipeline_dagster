# from dagster import asset
# from src.extract.extract import DataExtractor
# from src.transform.transform import DataTransformer
# from src.load.load import DataLoader

# @asset
# def crypto_market_data():
#     client = DataExtractor()
#     raw_data = client.extract_data(pages=2)
    
#     data_transformer = DataTransformer()
#     data_loader = DataLoader()

#     df = data_transformer.transform_data(raw_data)
    
#     data_loader.load_data(df)