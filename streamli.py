import streamlit as st
import pandas as pd
import numpy as np
import requests

st.title('Simple Streamlit App')

st.write("Here's our first attempt at using Streamlit to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    st.line_chart(chart_data)


   # url = 'https://immo-hosting.onrender.com/hello'
   # response = requests.post(url)