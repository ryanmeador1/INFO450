import streamlit as st
import pandas as pd
import plotly.express as px

project_df = pd.read_csv('cps_project_data.csv')

project_df['EDUC_GROUP'] = 'No Diploma'
project_df.loc[project_df['EDUC'] == 73, 'EDUC_GROUP'] = 'High School'
project_df.loc[project_df['EDUC'] == 81, 'EDUC_GROUP'] = 'Some College'
project_df.loc[project_df['EDUC'] == 91, 'EDUC_GROUP'] = 'Associate Degree'
project_df.loc[project_df['EDUC'] == 92, 'EDUC_GROUP'] = 'Associate Degree'
project_df.loc[project_df['EDUC'] == 111, 'EDUC_GROUP'] = 'Bachelors Degree'
project_df.loc[project_df['EDUC'] >= 123, 'EDUC_GROUP'] = 'Graduate Degree'

st.title('INFO 450 Final Project - Ryan Meador')

selected_year = st.slider('Year',min_value=2020,max_value=2025,value=2020)

project_df_year = project_df.loc[project_df['YEAR']==selected_year]
result = project_df_year['EARNWEEK2'].median()

st.write(f'Median Weekly Pay: ${result:.2f} for year {selected_year}')

selected_stat = st.selectbox('Would you like mean or median?',['Mean','Median'])

if selected_stat == 'Mean':
  result = project_df.groupby('EDUC_GROUP')['EARNWEEK2'].mean().sort_values(ascending=False)
  result = result.reset_index()

if selected_stat == 'Median':
  result = project_df.groupby('EDUC_GROUP')['EARNWEEK2'].median().sort_values(ascending=False)
st.write(result)
