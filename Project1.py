import streamlit as st
import pandas as pd
import plotly.express as px


xls_file = st.file_uploader('uploading excel file')
if xls_file:
    print('data uploaded')
    st.write("data uploaded")
    st.write("Debug")


