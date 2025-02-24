import os
import sys
from src.exceptions import CustomException
from dataclasses import dataclass
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from datetime import datetime

from src.components.data_transformation import DataTransformation,DataTransformationConfig

@dataclass
class DataIngestConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str= os.path.join('artifacts','test.csv')
    raw_data_path: str= os.path.join('artifacts','raw.csv')
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestConfig()
            
    def initiate_data_ingestion(self):
        logging.info("Enteres the Data Ingestion method or component")
        try:
            df = pd.read_csv("/Users/ushaswikurmala/Desktop/END_TO_END_ML_PROJECT/notebook/data/data.csv")
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info("Train test split initiated")
            train_set,test_set= train_test_split(df,test_size=0.2,random_state=42)
                
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
                
            logging.info('Data Ingestion is Completed')
                
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
                )
            
            
            
        except Exception as e :
            raise CustomException(e,sys)
                
                
               
            
            
if __name__ == "__main__":
    obj= DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

    
    
