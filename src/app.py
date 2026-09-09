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
    width, height = image.size
    # Resize the image while preserving its original aspect ratio.
    resized_image = image.copy()
    resized_image.thumbnail((224, 224))
    resized_width, resized_height = resized_image.size
    horizontal_padding = (224 - resized_width) // 2
    vertical_padding = (224 - resized_height) // 2
    # Center the resized image on a 224 × 224 canvas.
    padded_image = Image.new("RGB", (224, 224), "white")
    padded_image.paste(resized_image, (horizontal_padding, vertical_padding))
    st.image(padded_image, caption="Final 224 × 224 padded image")
    padded_width, padded_height = padded_image.size
    st.write("Original dimensions:", width, "×", height, "pixels")
    st.write("Processed dimensions:", padded_width, "×", padded_height, "pixels")
    st.image(image, caption="Uploaded image")

    # Placeholder prediction.
    # A real computer-vision model will replace this in a later lesson.
    prediction = "MODEL NOT CONNECTED YET"

    st.subheader("Prediction")
    st.write(prediction)
else:
    st.info("Upload an image to test the first version of the pipeline.")
