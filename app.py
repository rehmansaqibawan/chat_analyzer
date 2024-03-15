import streamlit as st
from preprocessor import preprocess
import matplotlib.pyplot as plt
import seaborn as sns

st.sidebar.title("WhatsApp Chat Analyser")
uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocess(data)
    print(df)

# fetch unique users
user_list = df['user'].unique().tolist()
user_list.remove('group_notification')
user_list.sort()
user_list.insert(0,"Overall")

selected_user = st.sidebar.selectbox("Show analysis wrt",user_list)

#if st.sidebar.button("Show Analysis"):