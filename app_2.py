import streamlit as st
import pandas as pd
import numpy as np
import transformers
from transformers import pipeline, AutoModelWithLMHead, AutoTokenizer
import torch 
#import boto3

#s3 = boto3.resource('s3')
#s3_object = s3.Bucket('nlp-gpt-models').Object('mod_v1.pth').get()



st.title('Patent Context Generation Tool-Development Stage..')
#model_path = s3_object
#model_path = 'https://nlp-gpt-models.s3.amazonaws.com/mod_v1.pth'
#model_path = 'https://drive.google.com/file/d/1-Dqk6fZzDiFKTqnnQ2yqW48uJk-CPqrB/view?usp=sharing'
propmt_title = st.text_input('Enter Your Title....', 'Biology...')

f1 = st.button('Generate')
if f1: 
    try:
        saved_model = torch.load(model_path)
        tokenizer = AutoTokenizer.from_pretrained("gpt2")
        generator = pipeline('text-generation', model = saved_model , tokenizer = tokenizer)
        def paraphrase(propmt_title):
            p = generator('<s>' + propmt_title + '</s>>>>><p>')
            return p[0]['generated_text'].split('</s>>>>>><p>')[0].split('</p>')[0].split('<p>')[1]    
        output= paraphrase(propmt_title) 
        st.text_area('paraphrased_titless', output ,False)
    except Exception as e:
        st.exception("Exception: %s\n" % e)    
        st.text_area('paraphrased_titless', st.exception("Exception: %s\n" % e) ,False)
           
propmt_title = st.text_input('Enter Your Paraphrased Title....', 'title context...')
f2 = st.form("my_form2")
f2.form_submit_button("Submit")

st.text_area('Generated Fields', '',False)


propmt_title = st.text_input('Enter Your Generated Field ....', 'Field context...')
f3 = st.form("my_form3")
f3.form_submit_button("Submit")

st.text_area('Generated Abstract', '',False)


propmt_title = st.text_input('Enter Your Generated Abstract ....', 'Abstract context...')
f4 = st.form("my_form4")
f4.form_submit_button("Submit")

st.text_area('Generated Background', '',False)



st.download_button(label="Download Full Patent (PDF file)",
                    data=propmt_title,
                    file_name="test.pdf",
                    mime='application/octet-stream')
