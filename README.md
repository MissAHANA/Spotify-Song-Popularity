
 # 🎵 Spotify Song Popularity Prediction

This project predicts whether a song on Spotify is a **hit or not** based on the number of streams and daily plays. It uses **Machine Learning (Random Forest Classifier)** and is deployed using **Streamlit**.

## 🚀 Live Demo
🔗 **Try the app here:** [Spotify Song Popularity Predictor](https://spotify-song-popularity-xcqcta4xcctmzlftiqdbd9.streamlit.app/)

---
## 📌 Project Overview
### 🎯 Goal:
Predict whether a song is a **hit (≥500M streams)** or not based on Spotify streaming data.

### 🛠️ Tech Stack:
- **Python** (Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn)
- **Machine Learning** (Random Forest Classifier)
- **Streamlit** (for web deployment)
- **GitHub** (for version control)
- **Streamlit Cloud** (for hosting)

---
## 📊 Dataset
- **Dataset Name:** `Spotify most streamed.csv`
- **Columns Used:**
  - `Artist` (Name of the artist)
  - `Title` (Song title)
  - `Streams` (Total number of streams)
  - `Daily` (Daily streams)
- **Target Variable:**
  - `Hit` (1 if `Streams` ≥ 500M, else 0)

---
## ⚙️ Installation & Setup
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/MissAHANA/spotify-song-popularity.git
cd spotify-song-popularity
```

### **2️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3️⃣ Run Locally**
```bash
streamlit run app.py
```

---
## 🔍 Machine Learning Model
### **📌 Steps:**
1. **Data Cleaning & Preprocessing**
   - Removed commas in numerical columns
   - Split `Artist and Title` column
   - Handled missing values
2. **Feature Selection**
   - Used `Streams` and `Daily` as input features
3. **Train-Test Split**
   - 80% training, 20% testing
4. **Feature Scaling**
   - Standardized numerical features
5. **Model Training**
   - Random Forest Classifier
6. **Model Evaluation**
   - Accuracy Score, Classification Report

### 📈 **Visualization**
- **Streams Distribution** (Histogram Plot)

---
## 🚀 Deployment on Streamlit
### **1️⃣ Upload to GitHub**
- Ensure `app.py` and `song_popularity_model.pkl` are in your repository.

### **2️⃣ Deploy to Streamlit Cloud**
1. Go to [Streamlit Cloud](https://share.streamlit.io/)
2. Click **New App**
3. Select your **GitHub Repository**
4. Set the file path to **app.py**
5. Click **Deploy** 🚀

---
## 🏆 Results & Accuracy
- **Model Accuracy:** ~90%
- **Predictions:** Classifies songs as **hit** or **not hit** based on stream count.

---
## 📂 File Structure
```
📂 spotify-song-popularity
├── 📄 app.py              # Streamlit Web App
├── 📄 model_training.py   # ML Model Training
├── 📄 song_popularity_model.pkl  # Trained Model
├── 📄 scaler.pkl         # Standard Scaler
├── 📄 requirements.txt   # Python Dependencies
├── 📄 README.md          # Project Documentation
└── 📂 dataset
    └── 📄 Spotify most streamed.csv  # Raw Data
```

---
## 📢 Contributing
Feel free to **fork** this repository, submit issues, or contribute improvements! 🚀

---
## 📞 Contact
💬 **LinkedIn:** www.linkedin.com/in/ahana-mukhopadhyay-27803622b 


