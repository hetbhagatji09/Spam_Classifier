from src.exception import customException
import os,sys
import pandas as pd
from src.logger import logging
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
@dataclass
class DataIngestionConfig:
    train_data_path=os.path.join("artifacts","train.csv")
    test_data_path=os.path.join("artifacts","test.csv")
    raw_data_path=os.path.join("artifacts","raw.csv")
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
    def initiate_data_config(self):
        logging.info("Entered in Data Ingetion initialization method")
        try:
            df=pd.read_csv('notebook/data/SMSSpamCollection',sep='\t',names=['label','message'])
            logging.info('read the dataset')
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info("Train and test data initiaed")
            
            train_data,test_data=train_test_split(df,random_state=42,test_size=0.22)
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            train_data.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            
            os.makedirs(os.path.dirname(self.ingestion_config.test_data_path),exist_ok=True)
            test_data.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            
            logging.info("Ingestion is Completed now")
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )            
        except Exception as e:
            raise customException(e,sys)
        
if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_config()
            
    