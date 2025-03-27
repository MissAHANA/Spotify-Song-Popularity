import streamlit as st
import pandas as pd
import joblib

# Load Model & Scaler
model = joblib.load("song_popularity_model.pkl")
scaler = joblib.load("scaler.pkl")

# Load Dataset
df = pd.read_csv("Spotify most streamed.csv")

# Clean Data
df['Streams'] = df['Streams'].str.replace(',', '').astype(float)
df['Daily'] = df['Daily'].str.replace(',', '').astype(float)
df[['Artist', 'Title']] = df['Artist and Title'].str.split(' - ', n=1, expand=True)
df.drop(columns=['Artist and Title'], inplace=True)

# Streamlit UI
st.markdown("🎵 **Spotify Song Popularity Predictor**")
st.write("Enter details below to predict whether a song is a HIT (≥500M streams) or NOT.")

# Select Song from Dropdown
song_choice = st.selectbox("Choose a Song", df['Title'])

# Get Artist & Streams
selected_song = df[df['Title'] == song_choice].iloc[0]
artist = selected_song["Artist"]
streams = selected_song["Streams"]
daily_streams = selected_song["Daily"]

st.write(f"🎤 **Artist:** {artist}")
st.write(f"🎵 **Song:** {song_choice}")

# Predict Popularity
scaled_features = scaler.transform([[streams, daily_streams]])
prediction = model.predict(scaled_features)

# Display Prediction Result
if prediction[0] == 1:
    st.success(f"✅ **{song_choice} by {artist} is a HIT!** 🎉")
else:
    st.warning(f"❌ **{song_choice} by {artist} is NOT a hit.**")

# Show Distribution of Streams
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Create histogram
fig, ax = plt.subplots()
sns.histplot(df["Streams"], bins=50, kde=True, ax=ax)

# Display in Streamlit
st.pyplot(fig)




