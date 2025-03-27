import streamlit as st
import joblib
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load trained model and scaler
model = joblib.load("song_popularity_model.pkl")
scaler = joblib.load("scaler.pkl")

# Streamlit UI
st.title("🎵 Spotify Song Popularity Predictor")
st.write("Enter the details below to predict whether a song is a HIT (≥2B streams) or NOT.")

# **NEW INPUT: Artist Name**
artist_name = st.text_input("Artist Name", "")

# Input fields for streams
total_streams = st.number_input("Total Streams", min_value=0, value=20000000, step=100000)
daily_streams = st.number_input("Daily Streams", min_value=0, value=2200000, step=100000)

# Predict button
if st.button("Predict"):
    # Scaling input data
    input_data = scaler.transform([[total_streams, daily_streams]])
    prediction = model.predict(input_data)[0]
    
    # Display result
    if prediction == 1:
        st.success(f"🎉 {artist_name}'s song is predicted to be a **HIT**! 🔥")
    else:
        st.warning(f"❌ {artist_name}'s song is **NOT a hit** yet.")

# **Add Distribution of Streams Visualization**
st.subheader("📊 Distribution of Streams")
df = pd.read_csv("Spotify most streamed.csv")
df['Streams'] = df['Streams'].str.replace(',', '').astype(float)
plt.figure(figsize=(8, 5))
sns.histplot(df['Streams'], bins=50, kde=True)
st.pyplot(plt)
