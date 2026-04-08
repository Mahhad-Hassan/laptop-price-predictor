import streamlit as st
import pickle
import numpy as np
import pandas as pd

# -------------------------------------------------------------------
# Page configuration
# -------------------------------------------------------------------
st.set_page_config(layout="wide", page_title="Laptop Price Predictor")
st.title("💻 Laptop Price Predictor")

# -------------------------------------------------------------------
# Load model and reference dataframe
# -------------------------------------------------------------------
try:
    pipe = pickle.load(open('pipe.pkl', 'rb'))
    df = pickle.load(open('df.pkl', 'rb'))
    st.success("✅ Model loaded successfully")
except FileNotFoundError as e:
    st.error(f"❌ Missing file: {e.filename}\n\nPlease run `train_model.py` first.")
    st.stop()
except Exception as e:
    st.error(f"❌ Failed to load model: {e}")
    st.stop()

# -------------------------------------------------------------------
# User inputs – all dropdowns use values from df.pkl
# -------------------------------------------------------------------
company = st.selectbox('Brand', df['Company'].unique())
type_name = st.selectbox('Type', df['TypeName'].unique())
ram = st.selectbox('RAM (in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])
weight = st.number_input('Weight (kg)', min_value=0.5, step=0.1, format="%.2f")

touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])
touchscreen_binary = 1 if touchscreen == 'Yes' else 0

ips = st.selectbox('IPS', ['No', 'Yes'])
ips_binary = 1 if ips == 'Yes' else 0

screen_size = st.slider('Screen size (inches)', 10.0, 18.0, 13.0, step=0.1)

resolution = st.selectbox('Screen Resolution', [
    '1920x1080', '1366x768', '1600x900', '3840x2160',
    '3200x1800', '2880x1800', '2560x1600', '2560x1440', '2304x1440'
])

cpu = st.selectbox('CPU', df['Cpu brand'].unique())
hdd = st.selectbox('HDD (in GB)', [0, 128, 256, 512, 1024, 2048])
ssd = st.selectbox('SSD (in GB)', [0, 8, 128, 256, 512, 1024])
gpu = st.selectbox('GPU', df['Gpu brand'].unique())
os = st.selectbox('OS', df['os'].unique())

# -------------------------------------------------------------------
# Prediction
# -------------------------------------------------------------------
if st.button('Predict Price'):
    try:
        # 1. Calculate PPI (pixels per inch)
        X_res = int(resolution.split('x')[0])
        Y_res = int(resolution.split('x')[1])
        ppi = ((X_res**2) + (Y_res**2)) ** 0.5 / screen_size

        # 2. Build a DataFrame with the exact column names used during training
        query_df = pd.DataFrame([[
            company, type_name, ram, weight,
            touchscreen_binary, ips_binary, ppi,
            cpu, hdd, ssd, gpu, os
        ]], columns=[
            'Company', 'TypeName', 'Ram', 'Weight',
            'Touchscreen', 'IPS', 'PPI',
            'Cpu brand', 'HDD', 'SSD', 'Gpu brand', 'os'
        ])

        # 3. Predict (log price) and convert back to original scale
        log_price = pipe.predict(query_df)[0]
        price = int(np.exp(log_price) / 92.34)

        # 4. Show result
        st.success(f"💰 **Predicted Price: ${price:,}**")

    except Exception as e:
        st.error(f"Prediction failed: {e}")