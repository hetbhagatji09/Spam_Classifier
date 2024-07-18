import os
import sys
from src.exception import customException
from src.logger import logging
import pandas as pd
import numpy as np
from src.utils import paragraph_list_format,save_object
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
import dill
from sklearn.naive_bayes import BernoulliNB
class Model_Trainer_Config:
    model_trainer_path=os.path.join("artifacts","model.pkl")

class Model_Trainer():
    def __init__(self):
        self.model_trainer_config=Model_Trainer_Config()
        
    def initiate_model_trainer(self,train_data,test_data):
        try:
            logging.info("Entered in the initiate_model_trainer part")
            train_df=pd.read_csv(train_data)
            test_df=pd.read_csv(test_data)
            X_train=train_df['message']
            X_test=test_df.drop('label',axis=1)
            y_train=pd.get_dummies(train_df['label'])
            y_train=y_train.iloc[:,0]
            y_test=pd.get_dummies(test_df['label'])
            y_test=y_test.iloc[:,0]
            
            cv=CountVectorizer(tokenizer=paragraph_list_format)
            classifier=BernoulliNB()
            model=Pipeline([
                ('vectorizer',cv),
                ('classifier',classifier)
            ])
            model.fit(X_train,y_train)
            save_object(
                self.model_trainer_config.model_trainer_path,
                obj=model
            )
            
            
            
            
            
        except Exception as e:
            raise customException(e,sys)