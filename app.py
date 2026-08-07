import streamlit as st
from PIL import Image
from prediction import predict

st.title("Steel Surface Defect Detection")

uploaded_file = st.file_uploader(
    "Upload steel image",
    type=["jpg","png"]
)


if uploaded_file:

    img = Image.open(uploaded_file)

    st.image(img)

    defect, confidence = predict(img)

    st.success(f"Defect: {defect}")

    st.write(
        f"Confidence: {confidence:.2f}"
    )