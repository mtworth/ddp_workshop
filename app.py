import pandas as pd
import streamlit as st

st.write("This is our data app.")
st.title("Change to app.")

df = pd.read_csv("Film_Locations_in_San_Francisco_20250423.csv")

st.dataframe(df)
