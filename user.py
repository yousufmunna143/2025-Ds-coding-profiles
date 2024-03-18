import streamlit as st
import pandas as pd
st.set_page_config(page_title="2025 DS Leader board",
                   layout="wide")
st.title("LeaderBoard of Coding Profiles")
data=pd.read_excel('scores.xlsx')
df=pd.DataFrame(data) 
st.dataframe(df, use_container_width=True, hide_index=True)
