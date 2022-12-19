import streamlit as st
from PIL import Image
 
st.title("DR. MAHMOUD SITE.")

image = Image.open('https://cdn-images-1.medium.com/max/1024/1*u9U3YjxT9c9A1FIaDMonHw.png')
st.image(image,use_column_width=True)

n_words =st.number_input('Type the number of words you want to generate')
seed_text =st.text_input('Type the number of words you want to generate after')


if n_words or seed_text:
    st.warning("generate_text")
else:
    st.warning("Please input a word and a number")
