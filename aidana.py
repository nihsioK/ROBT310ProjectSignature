import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
import subprocess
import os
from glob import glob
import pandas as pd


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


def run_processing_pipeline(uploaded_file):

    # remove signatures folder
    if os.path.exists("signatures"):
        for file in os.listdir("signatures"):
            os.remove(os.path.join("signatures", file))
    else:
        os.makedirs("signatures")

    temp_input_path = "uploaded_image.png"
    with open(temp_input_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    try:
        result = subprocess.run(["python", "main.py", temp_input_path], check=True, text=True, capture_output=True)
        st.write("Processing completed successfully.")
        st.write(result.stdout)
    except subprocess.CalledProcessError as e:
        st.error("Error occurred during processing.")
        st.error(e.stderr)
        return False

    return True


CLASS_NAMES = ["Fake", "Real"]

st.title("Signature Classification")

uploaded_file = st.file_uploader("Upload an Unprocessed Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    st.write("Processing the image through the pipeline...")
    if run_processing_pipeline(uploaded_file):
        signatures_folder = "signatures"
        signature_files = glob(os.path.join(signatures_folder, "*.png"))

        if len(signature_files) == 0:
            st.error("No signatures were detected. Please check the uploaded image.")
        else:
            st.write("Classifying detected signatures...")
            results = []

            for signature_path in signature_files:
                signature_name = os.path.basename(signature_path)
                signature_image = Image.open(signature_path)
                preprocessed_signature = preprocess_image(signature_image)
                class_idx, confidence = predict(preprocessed_signature)
                class_name = CLASS_NAMES[class_idx]
                results.append(
                    {"Signature": signature_name, "Prediction": class_name, "Confidence": f"{confidence:.2f}"}
                )

            results_df = pd.DataFrame(results)

            st.write("Classification Results:")
            st.table(results_df)
