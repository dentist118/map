import streamlit as st
#import pathlib
#from pathlib import Path
from PIL import Image 
st.title("DR. MAHMOUD SITE.")
#if st.checkbox('checkbox'):
   # st.image('medo1.png')
   
   
   def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2019/04/24/11/27/flowers-4151900_960_720.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 

#url = "https://raw.githubusercontent.com/danielgatis/rembg/master/examples/animal-3.jpg"
#st.image(
         #   [url],
          #  caption=["congrats"] ,
       # )
          

#caption = "hello!"
#image = Image.open('url')

n_words =st.number_input('Type the number of words you want to generate')
seed_text =st.text_input('Type the number of words you want to generate after')


if n_words or seed_text:
    st.warning("generate_text")
else:
    st.warning("Please input a word and a number")

