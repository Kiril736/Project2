import streamlit as st
import numpy as np
from PIL import Image
import joblib
import requests
import io

st.set_page_config(page_title="Handwritten Digit Recognition")
st.tilte("Handwrittem Digit Recognition")
st.write("Upload a handwritten digit image and AI will try to recognize it.")

@st.cache_resource
def load_model():
  try:
    from sklearn.datasets import load_digits
    from sklearn.nerual_network import MLPClassifier
    from sklearn.model_selection import train_test_split

    digit = load_digit()
    X = digits.images.reshape((len(digit.images), -1)) / 16.0
    y = digits.target
    X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)

model = MLPClassifier(
  hidden_layer_sizes=(100,),
  max_tier=100
  random_state=42
  )
model.fit(X_train, y_train)
return model
except Exception as e:
    st.error(f"Model loading error: {e}")
    return None
