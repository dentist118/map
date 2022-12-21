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
url = "https://bgremoval.streamlit.app/~/+/media/c4e5367c557d51b94574671c91778cff53fb5aff96f31ed81ece3e63.jpg"
#caption = "hello!"

        
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

