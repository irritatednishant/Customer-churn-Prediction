from dataclasses import dataclass
import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from src.logger import logging
from src.exception import CustomException
@dataclass
class DataIngestionConfig:
    raw_data_path: str = os.path.join("artifacts", "raw.csv")
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")

class DataIngestion:

    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        logging.info("Enterd the data ingestion component...")
        try:
            df = pd.read_excel("data/raw/Telco_customer_churn.xlsx")
            logging.info("Read the data as dataframe")

            os.makedirs("artifacts", exist_ok=True)
            df.to_csv(
                        self.ingestion_config.raw_data_path,
                        index=False,
                        header=True
                    )
            logging.info("Train test split initiated...")
            train_set, test_set = train_test_split(
                df,
                test_size=0.2,
                random_state=42
            )
            train_set.to_csv(
                    self.ingestion_config.train_data_path,
                    index=False,
                    header=True
                )

            test_set.to_csv(
                    self.ingestion_config.test_data_path,
                    index=False,
                    header=True
                )
            logging.info("Ingestion of data is complected..")
            return (
                    self.ingestion_config.train_data_path,
                    self.ingestion_config.test_data_path
                )
        except Exception as e:
            raise CustomException(e,sys)
