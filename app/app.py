import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

st.title("CIFAR-10 Image Classifier")

st.write("Upload an image and the CNN model will predict its class.")

# Load model
model = tf.keras.models.load_model("model/cifar10_cnn_model.h5")

# Class names
class_names = [
    "Airplane","Automobile","Bird","Cat","Deer",
    "Dog","Frog","Horse","Ship","Truck"
]

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg","png","jpeg"])

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Preprocess image
    image = image.resize((32,32))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)

    # Prediction
    prediction = model.predict(image)

    predicted_index = np.argmax(prediction)
    predicted_class = class_names[predicted_index]
    confidence = prediction[0][predicted_index]

    st.success(f"Prediction: {predicted_class}")
    st.write(f"Confidence: {confidence*100:.2f}%")

    # Top 3 predictions
    st.subheader("Top Predictions")

    top3 = np.argsort(prediction[0])[-3:][::-1]

    for i in top3:
        st.write(f"{class_names[i]} : {prediction[0][i]*100:.2f}%")
