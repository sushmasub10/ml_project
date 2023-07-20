import sys
import os
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

# no need to define class variable
@dataclass
# any input required for data ingestion, i do though data ingestion config.
class DataIngestionConfig:
    # it'll save train csv in artifacts
    train_data_path:str = os.path.join('artifacts', "train.csv")
    test_data_path:str = os.path.join('artifacts', "test.csv")
    raw_data_path:str = os.path.join('artifacts', "data.csv")

class DataIngestion :
    def __init__(self):
        # all the three paths will get stored inside this variable
        self.ingestion_config = DataIngestionConfig()

    def initiate_dataingestion(self):
        logging.info("Entered into data ingestion component")
        try:
            df = pd.read_csv("notebook/data/stud.csv")
            logging.info("Read the dataset as dataframe")
            # train data path creation
            print(self.ingestion_config.train_data_path)
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info("train test split initiated")
            # creating train and test
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=32)
            # save train data to same artifacts
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info("ingestion of data is completed")
            return (self.ingestion_config.train_data_path,
                    self.ingestion_config.test_data_path,
            )
        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    
    Myobj = DataIngestion()
    Myobj.initiate_dataingestion()

