
import streamlit as st
import pandas as pd
import plotly.express as px

project_df = pd.read_csv('cps_project_data.csv')

st.title('INFO 450 Final Project - Ryan Meador')

mean_pay_educ = project_df.groupby('EDUC_GROUP')['EARNWEEK2'].mean().sort_values(ascending=False).reset_index()

fig = px.bar(mean_pay_educ,x='EDUC_GROUP',y='EARNWEEK2',title='Mean Weekly Pay')

st.plotly_chart(fig)
