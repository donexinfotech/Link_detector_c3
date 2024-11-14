import streamlit as st
import pickle
import joblib  # Using joblib to load models if needed

# Load the vectorizer, model, and LabelEncoder
vectorizer = joblib.load("vectorizer.pkl")
link_detector = joblib.load("link_detector.pkl")
le = joblib.load("labelencoder.pkl")

# Define the prediction function
def is_malicious_link(link):
    # Transform the link using the vectorizer
    link_vector = vectorizer.transform([link])
    # Predict with the model
    prediction = link_detector.predict(link_vector)
    # Decode the prediction
    decoded_prediction = le.inverse_transform(prediction)
    return decoded_prediction[0]  # Return as string (e.g., "Malicious" or "Safe")

# Streamlit UI
st.title("Malicious Link Detector")
st.write("Enter a URL below to check if it is safe or malicious.")

# Text input for URL
user_link = st.text_input("Enter URL")

if st.button("Check Link"):
    if user_link:
        # Run the prediction function
        result = is_malicious_link(user_link)
        st.success(f"The link is **{result}**.")
    else:
        st.error("Please enter a valid URL.")
