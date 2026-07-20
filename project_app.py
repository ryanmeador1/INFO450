import streamlit as st
import pandas as pd
import plotly.express as px

project_df = pd.read_csv('cps_project_data.csv')

st.title('INFO 450 Final Project - Ryan Meador')

project_df['SEX_LABEL'] = 'Male'
project_df.loc[project_df['SEX']==2,'SEX_LABEL'] = 'Female'

st.sidebar.header('Filter')
filter_var = st.sidebar('Select filter',['EARNWEEK2','UHRSWORKT'])
