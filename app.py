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
    
elif user_selection == 'Overall Analysis' : 
    no_of_editions = data['Year'].unique().shape[0]-1 #Subtracting 1 because Olympics 1906 was Nullified
    no_of_cities = data['City'].unique().shape[0] #No. of Cities
    no_of_sports = data['Sport'].unique().shape[0] # No. of Sports Played in Olympics
    no_of_events = data['Event'].unique().shape[0] # No. of Events 
    No_of_athletes = data['Name'].unique().shape[0] # No. of athletes 
    no_of_countries = data['region'].unique().shape[0] # No. of Countries participated
    
    st.title("Summary")
    
    col1,col2,col3 = st.columns(3)
    with col1 :
        st.header('Editions')
        st.title(no_of_editions)
    with col2:
        st.header('Hosts')
        st.title(no_of_cities)
    with col3:
        st.header('Sports')
        st.title(no_of_sports)
        
    col1,col2,col3 = st.columns(3)
    with col1:
        st.header('Events')
        st.title(no_of_events)
    with col2:
        st.header('Nations')
        st.title(no_of_countries)
    with col3:
        st.header('Athletes')
        st.title(No_of_athletes)
        
    nations_over_the_years = helper.data_wrt_time(data,'region')
    fig = px.line(nations_over_the_years,x='Year',              y='count',
        labels={
        'Year':'Year',
        'count' : 'No. of Countries'
        },
        title="Participating countries over the Years")
    fig.update_layout(font=dict(size=18))
    st.plotly_chart(fig)
    
    
    events_over_the_years = helper.data_wrt_time(data,'Event')
    fig1 = px.line(events_over_the_years,x='Year',y='count',
        labels={
        'Year' : 'Year',
        'count' : 'No. of Events'
        },
        title="Events Played over the Years")
    fig1.update_layout(font=dict(size=18))
    st.plotly_chart(fig1)
    
    
    athletes_over_the_years = helper.data_wrt_time(data,'Name')
    fig2 = px.line(athletes_over_the_years,x='Year',y='count',
        labels={
        'Year' : 'Year',
        'count' : 'No. of Athletes'
        },
        title="Athletes Participated over the Years")
    fig2.update_layout(font=dict(size=18))
    st.plotly_chart(fig2)
    
    
    st.header("No. of Events over time(Every Sport)")
    fig,ax = plt.subplots(figsize = (18,18))
    
    x = data.drop_duplicates(['Year','Sport','Event'])

    ax = sns.heatmap(x.pivot_table(index = 'Sport' , columns = 'Year' , values = 'Event', aggfunc='count').fillna(0).astype(int),annot=True)
    st.pyplot(fig)
    
    st.header("Most Successful Athletes")
    sports = data['Sport'].unique().tolist()
    sports.sort()
    sports.insert(0,'OverAll')
    selected_sport = st.selectbox('Select a Sport',options=sports)
    x = helper.athlete_success(data,selected_sport) 
    st.table(x)