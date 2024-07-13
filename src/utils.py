from sklearn.metrics import accuracy_score
def evaluate_score(y_test,y_pred):
    return accuracy_score(y_test,y_pred)
    