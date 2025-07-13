from typing import Union

import streamlit as st
import easyocr
import matplotlib.pyplot as plt
st.set_page_config(page_title="OCR App", page_icon=":mag_right:", layout="wide")
st.title("Multi-langual OCR ")
st.sidebar.title("Settings")
st.sidebar.markdown("### Language Selection")
language = st.sidebar.selectbox(
    "Select Language",
    options=["English", "Spanish", "French", "German",'japanese', 'Chinese'],
    index=0
)
st.sidebar.markdown("# Image Upload")
uploaded_file = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
if uploaded_file is not None:
    # Save the uploaded file to a temporary location
    with open("temp_image.png", "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.sidebar.success("Image uploaded successfully!")
else:
    st.sidebar.warning("Please upload an image file.")
# Initialize EasyOCR reader with the selected language
if language == "English":
    lang_code = 'en'
elif language == "Spanish":
    lang_code = 'es'
elif language == "French":
    lang_code = 'fr'
elif language == "German":
    lang_code = 'de'
elif language == "Japanese":
    lang_code = 'ja'
elif language == "Chinese":
    lang_code = 'ch_sim'
else:
    lang_code = 'en'

reader = easyocr.Reader([lang_code])
# Function to perform OCR on the uploaded image
def perform_ocr(image_path: str) -> Union[str, None]:
    try:
        results = reader.readtext(image_path)
        text = "\n".join([result[1] for result in results])
        return text
    except Exception as e:
        st.error(f"Error during OCR: {e}")
# Display the uploaded image and perform OCR
if uploaded_file is not None:
    text = perform_ocr("temp_image.png")
    if text:
        st.subheader("Extracted Text:")
        st.write(text)      
    else:
        st.subheader("Extracted Text:")
        st.write("No image uploaded yet. Please upload an image to perform OCR.")
#display the image

img= plt.imread(uploaded_file) if uploaded_file else plt.imread('abc.png')
plt.figure(figsize=(10, 6))
plt.axis('off')  # Hide axes
plt.imshow(img)  # Display the image
