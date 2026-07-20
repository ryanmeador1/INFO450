import streamlit as st
import pandas as pd
import plotly.express as px

project_df = pd.read_csv('cps_project_data.csv')

st.title('INFO 450 Final Project - Ryan Meador')

selected_year = st.slider('Year',min_value=2020,max_value=2025,value=2020)

project_df_year = project_df.loc[project_df['YEAR']==selected_year]
result = project_df_year['EARNWEEK2'].median()

st.write(f'Median Weekly Pay: ${result:.2f} for year {selected_year}')
