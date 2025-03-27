import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from sklearn.preprocessing import StandardScaler

# Load the trained model and scaler
model = joblib.load("song_popularity_model.pkl")
scaler = joblib.load("scaler.pkl")

# Streamlit UI
st.title("🎵 Spotify Song Popularity Predictor")
st.write("Enter the details below to predict whether a song is a HIT (≥2B streams) or NOT.")

# User Inputs
streams = st.number_input("Total Streams", min_value=0, step=1000000, format="%d")
daily = st.number_input("Daily Streams", min_value=0, step=100000, format="%d")

# Prediction Logic
if st.button("Predict"):
    if streams == 0 or daily == 0:
        st.warning("Please enter valid stream numbers!")
    else:
        # Scale inputs
        scaled_input = scaler.transform([[streams, daily]])
        prediction = model.predict(scaled_input)[0]
        
        # Display Result
        if prediction == 1:
            st.success("🎉 This song is a HIT! (≥2B Streams)")
        else:
            st.error("🚀 This song is NOT a hit yet!")

# Data Visualization
st.subheader("🔍 Distribution of Streams")
df = pd.read_csv("Spotify most streamed.csv")
df['Streams'] = df['Streams'].str.replace(',', '').astype(float)
df['Daily'] = df['Daily'].str.replace(',', '').astype(float)

fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(df['Streams'], bins=50, kde=True, ax=ax)
ax.set_title("Distribution of Streams")
ax.set_xlabel("Streams")
ax.set_ylabel("Count")
st.pyplot(fig)
