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
import nltk
import textblob

from textblob import TextBlob

from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

st.set_page_config('Word cloud app',layout='wide')

st.title('Word cloud and sentiment analysis app')


col1, col2, col3 = st.beta_columns(3)

with col1:
    st.image('https://images.unsplash.com/photo-1457369804613-52c61a468e7d?ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80',use_column_width=True)
with col2:
    st.image('https://images.unsplash.com/photo-1569428034239-f9565e32e224?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',use_column_width=True)
with col3:
    st.image('https://images.unsplash.com/photo-1457369804613-52c61a468e7d?ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80',use_column_width=True)


st.header('Word cloud from text')

col1,col2 = st.beta_columns(2)

with col1:
    st.subheader('Input text')
    text = st.text_area(label = ' ',value='This is really a great wonderful place',height=435)
with col2:
    if text is not None:
        output = sc.gen_stylecloud(text,output_name='output.png',background_color='black',icon_name = 'fas fa-brain')
        st.subheader('The word cloud from the text is:')
        st.image('output.png',use_column_width=True)
    else:
        pass

st.header('Sentiment analysis')
phrase = TextBlob(text)

polarity = phrase.sentiment.polarity
subjectivity = phrase.sentiment.subjectivity

st.markdown('The positivity level of the text is '+str('{:.2%}'.format(polarity)))
st.markdown('The subjectivity level of the text is '+str('{:.2%}'.format(subjectivity)))

df = pd.DataFrame([[polarity,subjectivity,0.5,0]])
df.columns=['Polarity','Subjectivity','Horizontal','Vertical']


highlight = alt.selection(type='interval',bind='scales',encodings=['x','y'])

line = alt.Chart(df).mark_circle(size=200).encode(alt.X('Polarity:Q',axis=alt.Axis(format='%'),scale=alt.Scale(domain=[-1,1])),alt.Y('Subjectivity:Q',axis=alt.Axis(format='%'),scale=alt.Scale(domain=[0,1])),tooltip=[
      {"type": "quantitative", "field": "Polarity",'format':',.2%'},
      {"type": "quantitative", "field": "Subjectivity",'format':',.2%'}]).add_selection(highlight)

rule1 = alt.Chart(df).mark_rule().encode(alt.Y('Horizontal:Q',title='Subjectivity'),size=alt.value(1),color=alt.value('red'))
rule2 = alt.Chart(df).mark_rule().encode(alt.X('Vertical:Q',title='Polarity'),size=alt.value(1),color=alt.value('red'))

st.altair_chart(line+rule1+rule2,use_container_width=True)



st.header('Word cloud from Wikipedia article')

col1,col2 = st.beta_columns(2)

with col1:
    st.subheader('Wikipedia search')
    wiki = st.text_input(label=' ',value = 'LinkedIn')
    with st.beta_expander('Show Wikipedia article'):
        st.write(wikipedia.page(wiki).content)
with col2:
    if wiki is not None:
        sc.gen_stylecloud(text=wikipedia.page(wiki).content,output_name='wiki.png',background_color='black')
        st.subheader('The word cloud from the Wiki search is:')
        st.image('wiki.png')
