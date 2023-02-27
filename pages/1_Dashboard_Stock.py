import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "stock.jpg")
DATA_PATH_SBI = os.path.join(dir_of_interest, "data", "SBIN.csv")
DATA_PATH_ITC = os.path.join(dir_of_interest, "data", "ITC.csv")
DATA_PATH_INFY = os.path.join(dir_of_interest, "data", "INFY.csv")


st.title("Dashboard - Stock Data")
st.subheader('Monthly Closing Data')

img = image.imread(IMAGE_PATH)
st.image(img)

SBI = pd.read_csv(DATA_PATH_SBI)
ITC = pd.read_csv(DATA_PATH_ITC)
INFY = pd.read_csv(DATA_PATH_INFY)

stock = st.selectbox("Select the Species:", ('SBI','ITC','INFY'))


if stock == 'SBI':
    st.dataframe(SBI)
    st.bar_chart(SBI['Close'])
    st.line_chart(SBI['Close'])

elif stock == 'ITC':
    st.dataframe(ITC)
    st.bar_chart(ITC['Close'])
    st.line_chart(ITC['Close'])

else:
    st.dataframe(INFY)
    st.bar_chart(INFY['Close'])
    st.line_chart(INFY['Close'])