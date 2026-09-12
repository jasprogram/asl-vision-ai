import streamlit as st
from PIL import Image

def preprocess_image(image):
    resized_image = image.copy()
    resized_image.thumbnail((224, 224))
    resized_width, resized_height = resized_image.size
    horizontal_padding = (224 - resized_width) // 2
    vertical_padding = (224 - resized_height) // 2
    padded_image = Image.new("RGB", (224, 224), "white")
    padded_image.paste(resized_image, (horizontal_padding, vertical_padding))
    return padded_image

st.set_page_config(page_title="ASL Vision AI", page_icon="🤟")

st.title("ASL Vision AI")
st.write("Project 1: building toward visual ASL vocabulary recognition.")

uploaded_file = st.file_uploader(
    "Upload an image containing an ASL sign",
    type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    processed_image = preprocess_image(image)
    width, height = image.size
    processed_width, processed_height = processed_image.size
    center_pixel = processed_image.getpixel((112, 112))
    normalized_red = center_pixel[0] / 255
    st.write("Normalized red:", normalized_red)
    st.write("Center pixel RGB:", center_pixel)
    normalized_pixel = tuple(value / 255 for value in center_pixel)
    st.write("Normalized center pixel:", normalized_pixel)
    st.write("Original dimensions:", width, "×", height, "pixels")
    st.write("Processed dimensions:", processed_width, "×", processed_height, "pixels")
    st.image(processed_image, caption="Final 224 × 224 padded image")
    
    # Placeholder prediction.
    # A real computer-vision model will replace this in a later lesson.
    prediction = "MODEL NOT CONNECTED YET"
    
    st.subheader("Prediction")
    st.write(prediction)
else:
    st.info("Upload an image to test the first version of the pipeline.")
