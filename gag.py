import streamlit as st
#import pathlib
#from pathlib import Path
from PIL import Image 
st.title("DR. MAHMOUD SITE.")
#if st.checkbox('checkbox'):
   # st.image('medo1.png')
image = [
            Image.new("RGB", (64, 64), color="gray"),
            
        ]
url = "https://raw.githubusercontent.com/danielgatis/rembg/master/examples/animal-3.jpg"
caption = "hello!"

        
#image = Image.open('url')
st.image(
            [url],
            caption=["congrats"] ,
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

