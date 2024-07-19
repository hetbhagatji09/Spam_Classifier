import pandas as pd
import numpy as np
import pickle
import streamlit as st
from src.utils import predict

from sklearn.metrics import accuracy_score
  
  

st.text("Spam Classifier");

label=st.text_input(label="Enter Email",value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, placeholder=None, disabled=False, label_visibility="visible")


if st.button("Check"):
    prediction=predict(label)

    st.text(prediction)



    
# y_pred=model.predict(["You won't believe it but it's true. It's Incredible Txts! Reply G now to learn truly amazing things that will blow your mind. From O2FWD only 18p/txt"])
