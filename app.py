import streamlit as st
import pandas as pd
import preprocessor,helper
import numpy as np


data = preprocessor.preprocess()

st.sidebar.title("Olympics Analysis")

user_selection = st.sidebar.radio(
                'Select Options',
                ('Medal Tally','Overall Analysis','Country-wise Analysis','Athlete-wise Analysis'))

if user_selection == 'Medal Tally':
    st.sidebar.header('Medal Tally')
    years,country = helper.year_country(data)
    selected_year = st.sidebar.selectbox("Select Year",years)
    selected_country = st.sidebar.selectbox("Select Country",country)
    medals = helper.fetch_medal_tally(data,selected_year,selected_country)
    if selected_year == 'OverAll' and selected_country == 'OverAll':
        st.title('OverAll Medals Tally')
    elif selected_year != 'OverAll' and selected_country == 'OverAll':
        st.title('Medals Tally in '+ str(selected_country)+' Olympics')
    elif selected_year == 'OverAll' and selected_country != 'OverAll':
        st.title(str(selected_country )+'OverAll Performance')
    elif selected_country != 'OverAll' and selected_year != 'OverAll':
        st.title(selected_country + " performance in "+ str(selected_year)+ " Olympics")
    st.table(medals)
    
    