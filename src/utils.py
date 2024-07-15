from sklearn.metrics import accuracy_score
import sys
from src.exception import customException
try:
    def evaluate_score(y_test,y_pred):
        return accuracy_score(y_test,y_pred)
except Exception as e:
    raise customException(e,sys)
    