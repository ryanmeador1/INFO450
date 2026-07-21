
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

project_df['SEX_LABEL'] = 'Male'
project_df.loc[project_df['SEX']==2,'SEX_LABEL'] = 'Female'

st.title('INFO 450 Final Project - Ryan Meador')
st.markdown('This dashboard is to help answer 3 questions.')
st.markdown('1. How do weekly earnings differ by education level?')
st.markdown('2. Have median weekly earnings changed from 2022 to 2025?')
st.markdown('3. Is there a difference in weekly earnings between men and women? Does it persist within education levels?')

selected_year = st.slider('Year',min_value=2020,max_value=2025,value=2020)

project_df_year = project_df.loc[project_df['YEAR']==selected_year]
result = project_df_year['EARNWEEK2'].median()

st.write(f'Median Weekly Pay: ${result:.2f} for year {selected_year}')

project_df_desc = project_df[['AGE','UHRSWORKT','EARNWEEK2']].loc[project_df['YEAR']==selected_year].describe()
project_df_desc = project_df_desc.reset_index()
st.dataframe(project_df_desc)

selected_stat = st.selectbox('Would you like mean or median?',['Mean','Median'])

if selected_stat == 'Mean':
  result = project_df.groupby('EDUC_GROUP')['EARNWEEK2'].mean().sort_values(ascending=False)
  result = result.reset_index()
  result_sex = project_df.groupby(['EDUC_GROUP','SEX_LABEL'])['EARNWEEK2'].mean().unstack()
  result_sex = result_sex.reset_index()
  
if selected_stat == 'Median':
  result = project_df.groupby('EDUC_GROUP')['EARNWEEK2'].median().sort_values(ascending=False)
  result = result.reset_index()
  result_sex = project_df.groupby(['EDUC_GROUP','SEX_LABEL'])['EARNWEEK2'].median().unstack()
  result_sex = result_sex.reset_index()

fig = px.bar(result,x='EDUC_GROUP',y='EARNWEEK2',title=f'{selected_stat} Weekly Pay by Education Level')
st.plotly_chart(fig)

fig2 = px.bar(result_sex,x='EDUC_GROUP',y=['Female','Male'],title=f'{selected_stat} Weekly Pay by Gender and Education Level',barmode='group')
st.plotly_chart(fig2)

