import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf


@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("my_model.h5")
    return model


model = load_model()


def preprocess_image(image):
    image = image.resize((224, 224))
    image_array = np.array(image)
    if image_array.shape[-1] != 3:
        image_array = np.stack([image_array] * 3, axis=-1)
    image_array = image_array / 255.0
    image_array = np.expand_dims(image_array, axis=0)
    return image_array


def predict(image_array):
    predictions = model.predict(image_array)
    class_idx = np.argmax(predictions, axis=1)[0]
    confidence = np.max(predictions)
    return class_idx, confidence


CLASS_NAMES = ["FAKE", "REAL"]

st.title("Image Classification with VGG16")

uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    st.write("Processing image...")
    preprocessed_image = preprocess_image(image)

    class_idx, confidence = predict(preprocessed_image)

    st.write(f"Prediction: **{CLASS_NAMES[class_idx]}**")
    st.write(f"Confidence: **{confidence:.2f}**")
