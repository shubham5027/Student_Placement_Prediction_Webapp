import streamlit as st
from predict_page import show_prediction
from explore_page import explore_graphs

st.sidebar.subheader('Explore or Predict')
explore_predict = st.sidebar.selectbox('Choose page to view', ['Predict', 'Explore'])
st.sidebar.write('Explore displays the data used')
st.sidebar.write('Predict is for the prediction page')

if explore_predict == 'Predict':
    show_prediction()
else:
    explore_graphs()