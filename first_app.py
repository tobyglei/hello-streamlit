# Example app from
# https://docs.streamlit.io/en/stable/tutorial/create_a_data_explorer_app.html#let-s-put-it-all-together

import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamlit Example on 21YunBox -- Uber pickups in NY')

DATE_COLUMN = 'date/time'
# 原文件在 s3上
# DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
#             'streamlit-demo-data/uber-raw-data-sep14.csv.gz')
DATA_URL = 'https://21box-assets.oss-cn-beijing.aliyuncs.com/uber-raw-data-sep14.csv.gz'

@st.cache
def load_data(nrows):
    with open(filename, 'rb') as csvfile:
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Number of pickups by hour')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# Some number in the range 0-23
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)