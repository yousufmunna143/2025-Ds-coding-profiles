import streamlit as st
from openpyxl import load_workbook
import pandas as pd

st.set_page_config(page_title="2025 DS Leader board")
st.title("2025 DS Batch LeaderBoard")
data=pd.read_excel('scores.xlsx')
df=pd.DataFrame(data) 
st.dataframe(df, hide_index=True)
