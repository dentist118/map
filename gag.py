import streamlit as st
from PIL import Image
st.title("DR. MAHMOUD SITE.")

image = Image.open("https://daanbio-printai-printai-yny7c6.streamlit.app/~/+/media/f1488d35dd3509cd93a1a7c2e7e787e91ba09d577cbd9130913aa507.jpg")
st.image(image,use_column_width=True)


n_words =st.number_input('Type the number of words you want to generate')
seed_text =st.text_input('Type the number of words you want to generate after')


if n_words or seed_text:
    st.warning("generate_text")
else:
    st.warning("Please input a word and a number")

