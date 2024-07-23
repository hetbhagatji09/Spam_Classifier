import os
import pandas as pd
import numpy as np
import pickle
import streamlit as st
from src.utils import predict

from sklearn.metrics import accuracy_score

# Streamlit app
st.text("Spam Classifier")

label = st.text_input(label="Enter Email", value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, placeholder=None, disabled=False, label_visibility="visible")

if st.button("Check"):
    prediction = predict(label)
    st.text(prediction)

# Streamlit deployment setup
if __name__ == "__main__":
    os.system("streamlit run application.py --server.port $PORT --server.address 0.0.0.0")
