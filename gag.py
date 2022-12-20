import streamlit as st
from PIL import Image
st.title("DR. MAHMOUD SITE.")

image = Image.open("https://user-images.githubusercontent.com/82735653/208552069-b074e6f4-d569-428d-9b59-40cadd5474a9.jpg")
st.image(image,use_column_width=True)


n_words =st.number_input('Type the number of words you want to generate')
seed_text =st.text_input('Type the number of words you want to generate after')


if n_words or seed_text:
    st.warning("generate_text")
else:
    st.warning("Please input a word and a number")

