import streamlit as st
import pickle
import numpy as np
import pandas as pd

st.title("Loading...")

try:
    pipe = pickle.load(open('pipe.pkl', 'rb'))
    df = pickle.load(open('df.pkl', 'rb'))
    st.success("Models loaded")
except Exception as e:
    st.error(f"Error: {e}")
    st.stop()

st.title("Laptop Price Predictor")
st.selectbox("Test dropdown", ["A", "B", "C"])