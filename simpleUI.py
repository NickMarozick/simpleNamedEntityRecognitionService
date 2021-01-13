import streamlit as st
import numpy as np
import pandas as pd
import os
import bs4 as bs
import urllib.request as url

st.title("Simple UI to Showcase Named Entity Recognition")

userInput= st.text_input('Input the text to be analyzed here:')

runService = st.button('Run Service!')

if runService:
  st.write("Service button pressed")

  source2= url.urlopen('http://localhost:8080/userInput')
  page_soup2= bs.BeautifulSoup(source2, 'html.parser')
  st.write(page_soup2)


expander = st.beta_expander("About")
expander.write("Simple UI built via streamlit to run a service and showcase Named Entity Recognition. Please add text to be analyzed in the box and click the 'Run Service' button to analyze and output the results")
