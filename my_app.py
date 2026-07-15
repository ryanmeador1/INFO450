
import streamlit as st
import pandas as pd
import plotly.express as px

df=pd.read_csv("Advertising_F.csv")

st.title("Advertising Effectivness Ryan")
st.sidebar.header("Filters")
x_var=st.sidebar.selectbox("X-Axis",["TV","radio","newspaper"])

fig=px.scatter(df,x=x_var,y="sales")
st.plotly_chart(fig)

#dataframe 
st.write('### This is the data')
st.dataframe(df)

# Show Map 
fig = px.scatter_mapbox(df,lat='latitude',lon='longitude',size='sales',hover_name='City')
fig.update_layout(mapbox_style='carto-positron')
st.plotly_chart(fig)
