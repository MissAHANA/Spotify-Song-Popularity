import streamlit as st
import pandas as pd
import joblib

# Load model and scaler
model = joblib.load("song_popularity_model.pkl")
scaler = joblib.load("scaler.pkl")

# Load dataset to retrieve song names and artists
df = pd.read_csv("Spotify most streamed.csv")

# Preprocess dataset to extract song names
df['Streams'] = df['Streams'].str.replace(',', '').astype(float)
df['Daily'] = df['Daily'].str.replace(',', '').astype(float)
df[['Artist', 'Title']] = df['Artist and Title'].str.split(' - ', n=1, expand=True)

# Streamlit UI
st.title("🎵 Spotify Song Popularity Predictor")
st.write("Enter the details below to predict whether a song is a HIT (≥1B streams) or NOT.")

# User inputs
total_streams = st.number_input("Total Streams", min_value=0, value=20000000)
daily_streams = st.number_input("Daily Streams", min_value=0, value=2200000)

if st.button("Predict"):
    # Scale input
    input_data = scaler.transform([[total_streams, daily_streams]])
    
    # Make prediction
    prediction = model.predict(input_data)[0]
    
    # Find matching song details
    matching_song = df[(df["Streams"] == total_streams) & (df["Daily"] == daily_streams)]
    
    if not matching_song.empty:
        song_name = matching_song["Title"].values[0]
        artist_name = matching_song["Artist"].values[0]
    else:
        song_name = "Unknown Song"
        artist_name = "Unknown Artist"
    
    # Display result
    if prediction == 1:
        st.success(f"✅ **{song_name}** by **{artist_name}** is a **HIT!** 🎉")
    else:
        st.error(f"❌ **{song_name}** by **{artist_name}** is **NOT a HIT.**")

