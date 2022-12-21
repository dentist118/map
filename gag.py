import streamlit as st
import pathlib
from pathlib import Path
from PIL import Image ,ImagePath
st.title("DR. MAHMOUD SITE.")
#if st.checkbox('checkbox'):
   # st.image('medo1.png')
url = "https://bgremoval.streamlit.app/~/+/media/e41ef1cefe668882972d74a560811abe2134ebe7cdf41d69e50f5ae8.png"
caption = "ahoy!"

        
st.image([url] * 1, caption=[caption] * 1)
st.image(
            imgs,
            caption=["some caption"] * 1,
            width=200,
            use_column_width=True,
            clamp=True,
            
        )

n_words =st.number_input('Type the number of words you want to generate')
seed_text =st.text_input('Type the number of words you want to generate after')


if n_words or seed_text:
    st.warning("generate_text")
else:
    st.warning("Please input a word and a number")

