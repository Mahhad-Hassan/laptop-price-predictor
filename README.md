# 💻 Laptop Price Predictor

A machine learning web app that predicts laptop prices based on specifications like brand, RAM, storage, CPU, GPU, screen size, and more.

## 🚀 Live Demo

*(if you deploy to Streamlit Cloud, add the link here)*

## 📊 Dataset

The model was trained on a dataset of 1300+ laptops with features such as:
- Company, Type, RAM, Weight, Touchscreen, IPS, PPI, CPU, HDD, SSD, GPU, OS

## 🧠 Model

- **Algorithm**: Decision Tree Regressor
- **Preprocessing**: One‑hot encoding for categorical features
- **Target**: Log‑transformed price, then exponentiated for final prediction

## 🛠️ How to run locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/laptop-price-predictor.git
   cd laptop-price-predictor