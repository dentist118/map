import streamlit as st
#import tensorflow
#from tensorflow import keras
#from tensorflow.keras.preprocessing.text import Tokenizer
#from tensorflow.keras.models import model_from_json
#from tensorflow.keras.preprocessing.sequence import pad_sequences
from PIL import Image

#import model
#json_file =open('./model.json','r')
#loaded_json_model = json_file.read()
#json_file.close()

#loaded_model = model_from_json(loaded_json_model)

#load weights
#loaded_model.load_weights("./model.h5")

#with open('./bart-chalkboard-data.txt','r',encoding='utf-8') as file:
  #  data = file.read()
  
#def generate_text(model,tokenizer,max_length,seed_text,n_words):
    #text_generated = seed_text
    #for i in range(n_words):
        #encoded = tokenizer.texts_to_sequences([text_generated])[0]

        #encoded = pad_sequences([encoded],maxlen=max_length,padding='pre')

        #yhat=model.predict_classes(encoded,verbose=0)

        #predicted_word =''
        #for word,index in tokenizer.word_index.items():
         #   if index == yhat:
          #      predicted_word =word
           #     break

        #text_generated +=' '+ predicted_word
    #return text_generated
#tokenizer = Tokenizer()
#tokenizer.fit_on_texts([data])


max_length =14

st.title("DR. MAHMOUD SITE.")

image = Image.open('C:/Users/md/Pictures/MEmu Photo/FB_IMG_1622378606612.jpg')
st.image(image,use_column_width=False)

n_words =st.number_input('Type the number of words you want to generate')
seed_text =st.text_input('Type the number of words you want to generate after')


if n_words or seed_text:
    st.warning("generate_text")
else:
    st.warning("Please input a word and a number")
