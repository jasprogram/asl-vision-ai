import streamlit as st
from PIL import Image

st.set_page_config(page_title="ASL Vision AI", page_icon="🤟")

st.title("ASL Vision AI")
st.write("Project 1: building toward visual ASL vocabulary recognition.")

uploaded_file = st.file_uploader(
    "Upload an image containing an ASL sign",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded image")

    # Placeholder prediction.
    # A real computer-vision model will replace this in a later lesson.
    prediction = "MODEL NOT CONNECTED YET"

    st.subheader("Prediction")
    st.write(prediction)
else:
    st.info("Upload an image to test the first version of the pipeline.")
