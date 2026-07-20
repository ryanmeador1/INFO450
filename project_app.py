
import streamlit as st
import pandas as pd
import plotly.express as px

project_df = pd.read_csv('cps_project_data.csv')

st.title('INFO 450 Final Project - Ryan Meador')

# Creates a new column to categorize the codes for education
project_df['EDUC_GROUP'] = 'No Diploma'
project_df.loc[project_df['EDUC'] == 73, 'EDUC_GROUP'] = 'High School'
project_df.loc[project_df['EDUC'] == 81, 'EDUC_GROUP'] = 'Some College'
project_df.loc[project_df['EDUC'] == 91, 'EDUC_GROUP'] = 'Associate Degree'
project_df.loc[project_df['EDUC'] == 92, 'EDUC_GROUP'] = 'Associate Degree'
project_df.loc[project_df['EDUC'] == 111, 'EDUC_GROUP'] = 'Bachelors Degree'
project_df.loc[project_df['EDUC'] >= 123, 'EDUC_GROUP'] = 'Graduate Degree'
mean_pay_educ = project_df.groupby('EDUC_GROUP')['EARNWEEK2'].mean().sort_values(ascending=False).reset_index()

fig = px.bar(mean_pay_educ,x='EDUC_GROUP',y='EARNWEEK2',title='Mean Weekly Pay', labels={
  'EDUC_GROUP':'Education Level',
  'EARNWEEK2': 'Median Weekly Pay'
})

st.plotly_chart(fig)
