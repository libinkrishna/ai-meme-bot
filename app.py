import streamlit as st
from utils.meme_generator import generate_meme_caption
from PIL import Image

st.set_page_config(page_title="AI Meme Generator")
st.title("🤖 AI Meme Generator")
st.markdown("Upload an image and get a funny AI-generated meme caption!")

uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_image:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Generate Meme Caption"):
        caption = generate_meme_caption(image)
        st.success(f"💬 Meme Caption: **{caption}**")
