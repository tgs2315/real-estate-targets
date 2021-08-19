import streamlit as st
import pandas as pd
import numpy as np

"""
# Real Estate Targets
"""

df = pd.read_csv('targets.csv')
df.columns = map(str.lower, df.columns)

st.map(df.loc[:, ['latitude', 'longitude']])

df
