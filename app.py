import pandas as pd
import numpy as np

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

text = st.text_area(label = 'Text input area',value='Input text here',height=300)

if text is not None:
    output = sc.gen_stylecloud(text,output_name='output.png',background_color='black',icon_name = 'fas fa-chart-pie')
    st.header('The word cloud from the text is:')
    st.image('output.png')
else:
    pass
