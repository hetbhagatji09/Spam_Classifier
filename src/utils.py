from sklearn.metrics import accuracy_score
import sys,os
import dill
import pandas as pd
import numpy as np
import nltk
import warnings
warnings.filterwarnings("ignore")
from nltk import word_tokenize
from nltk.stem import PorterStemmer,WordNetLemmatizer
from nltk.corpus import stopwords

from src.exception import customException
def evaluate_score(y_test,y_pred):
    try:
        return accuracy_score(y_test,y_pred)
    except Exception as e:
        raise customException(e,sys)
def load_object(file_path):
    try:
        with open(file_path,'rb') as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        raise customException(e,sys)


def paragraph_list_format(sentence):
    try:
        ps=PorterStemmer()
        sentence=sentence.lower()
        words=word_tokenize(sentence)
        return [ps.stem(word) for word in words if word not in stopwords.words('english')]
        
    except Exception as e:
        raise customException(e,sys)
def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,'wb')as file_obj:
            dill.dump(obj,file_obj)
    except Exception as e:
        raise customException(e,sys)
    
def predict(text):
    model_path="artifacts\model.pkl"
    model=load_object(file_path=model_path)
    prediction=model.predict([text])
    if prediction[0]==1:
        return "Ham"
    else:
        return "Spam"
    # return prediction
    
    