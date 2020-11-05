import pandas as pd
import numpy as np

import wikipedia

import re

import datetime as dt

import altair as alt

from bs4 import BeautifulSoup
import requests
from requests import get

import streamlit as st

import stylecloud as sc

st.set_page_config('Word cloud app',layout='wide')

st.title('Word cloud generator app')


col1, col2, col3 = st.beta_columns(3)

with col1:
    st.image('https://images.unsplash.com/photo-1457369804613-52c61a468e7d?ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80',use_column_width=True)
with col2:
    st.image('https://images.unsplash.com/photo-1569428034239-f9565e32e224?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',use_column_width=True)
with col3:
    st.image('https://images.unsplash.com/photo-1457369804613-52c61a468e7d?ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80',use_column_width=True)


st.header('Word cloud from text input')

text = st.text_area(label = 'Text input area',value='Input text here',height=300)

if text is not None:
    output = sc.gen_stylecloud(text,output_name='output.png',background_color='black',icon_name = 'fas fa-brain')
    st.subheader('The word cloud from the text is:')
    st.image('output.png')
else:
    pass


st.header('Word cloud from Wikipedia summary')

wiki = st.text_input(label='Search Wikipedia',value = 'LinkedIn')

if wiki is not None:
    sc.gen_stylecloud(text=wikipedia.content(wiki),output_name='wiki.png',background_color='black')
    st.subheader('The word cloud from the Wiki search is:')
    st.image('wiki.png')
    with st.beta_expander('Show Wikipedia article'):
        st.write(wikipedia.content(wiki))
