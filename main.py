# import libraries
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import matplotlib.pyplot as plt
import seaborn as sns
import json

# read data
sorted_person_link = "json/general_PERSON.json"
sorted_norp_link =  "json/general_NORP.json"
sorted_org_link =  "json/general_ORG.json"
sorted_gpe_link =  "json/general_GPE.json"
sorted_loc_link =  "json/general_LOC.json"

fox_person_link =  "json/fox_PERSON.json"
fox_norp_link =  "json/fox_NORP.json"
fox_org_link =  "json/fox_ORG.json"
fox_gpe_link =  "json/fox_GPE.json"
fox_loc_link =  "json/fox_LOC.json"

cnn_person_link =  "json/cnn_PERSON.json"
cnn_norp_link =  "json/cnn_NORP.json"
cnn_org_link =  "json/cnn_ORG.json"
cnn_gpe_link =  "json/cnn_GPE.json"
cnn_loc_link =  "json/cnn_LOC.json"

aljazeera_person_link =  "json/aljazeera_PERSON.json"
aljazeera_norp_link =  "json/aljazeera_NORP.json"
aljazeera_org_link =  "json/aljazeera_ORG.json"
aljazeera_gpe_link =  "json/aljazeera_GPE.json"
aljazeera_loc_link =  "json/aljazeera_LOC.json"

@st.cache
def read_data(name):
    with open(name) as json_file:
        data = json.load(json_file)
    return data
    
def plot(dictionary, sd):
    names = list(dictionary.keys())[:20]
    values = list(dictionary.values())[:20]
    fig = plt.figure(figsize=(14, 7))
    st.subheader(sd)
    sns.barplot(x=names, y = values)
    plt.xticks(rotation=40) 
    st.pyplot(fig)
    
def sorting(x):
    a = dict(sorted(x.items(), key=lambda item: item[1], reverse=True))
    return a
    
#Setting up our homepage window of Streamlit app
def main():
    page = st.sidebar.selectbox(
        "Select a Page",
        [
            "Homepage",
            "All NER and Analysis",
            "Al Jazeera NER and Analysis",
            "CNN NER and Analysis",
            "FOX NER and Analysis",
            "World Map",
            "Ukraine Map",
        ]
    )
    #First Page
    if page == "Homepage":
        homepage()
    #First Page
    if page == "All NER and Analysis":
        all_news()
    #Al Jazeera NER and Analysis Page
    if page == "Al Jazeera NER and Analysis":
        al_jazeera()
    #CNN NER and Analysis Page
    if page == "CNN NER and Analysis":
        cnn_news()
    #FOX NER and Analysis Page
    if page == "FOX NER and Analysis":
        fox_news()
    #World Map Page
    if page == "World Map":
        world()
    #Ukraine Map Page
    if page == "Ukraine Map":
        ukraine()    
    # general variables

def homepage():
    st.write("""
        # Building Visual Apps to Explore Current World Events from News Sources using Data Science
        ###### Team members: Yerke Bauyrzhanov , Saurabh Dasgupta, Michael Fienberg, Soumeya Kerrar, Vu Truong Si , Jiayi Xu 
        """)   

def all_news():
    sorted_person = sorting(read_data(sorted_person_link))
    sorted_norp = sorting(read_data(sorted_norp_link))
    sorted_org =  sorting(read_data(sorted_org_link))
    sorted_gpe =  sorting(read_data(sorted_gpe_link))
    sorted_loc =  sorting(read_data(sorted_loc_link))
    
    # All news
    st.header("All distribution")
    sd = st.selectbox(
        "Select a Plot", #Drop Down Menu Name
        [
            "Top 20 mentioned PERSON", #First option in menu
            "Top 20 mentioned NORP",   #Second option in menu
            "Top 20 mentioned ORG",
            "Top 20 mentioned GPE",
            "Top 20 mentioned LOC",            
        ]
    )
    if sd == "Top 20 mentioned PERSON":
        plot(sorted_person,sd)
      
    if sd == "Top 20 mentioned NORP":
        plot(sorted_norp,sd)
    
    if sd == "Top 20 mentioned ORG":
        plot(sorted_org,sd)
        
    if sd == "Top 20 mentioned GPE":
        plot(sorted_gpe,sd)
        
    if sd == "Top 20 mentioned LOC":
        plot(sorted_loc,sd)

def al_jazeera():
    aljazeera_person = sorting(read_data(aljazeera_person_link))
    aljazeera_norp = sorting(read_data(aljazeera_norp_link))
    aljazeera_org =  sorting(read_data(aljazeera_org_link))
    aljazeera_gpe =  sorting(read_data(aljazeera_gpe_link))
    aljazeera_loc =  sorting(read_data(aljazeera_loc_link))
    # Al jazeera news
    st.header("All distribution")
    sd = st.selectbox(
        "Select a Plot", #Drop Down Menu Name
        [
            "Top 20 mentioned PERSON", #First option in menu
            "Top 20 mentioned NORP",   #Second option in menu
            "Top 20 mentioned ORG",
            "Top 20 mentioned GPE",
            "Top 20 mentioned LOC",            
        ]
    )
    if sd == "Top 20 mentioned PERSON":
        plot(aljazeera_person,sd)
      
    if sd == "Top 20 mentioned NORP":
        plot(aljazeera_norp,sd)
    
    if sd == "Top 20 mentioned ORG":
        plot(aljazeera_org,sd)
        
    if sd == "Top 20 mentioned GPE":
        plot(aljazeera_gpe,sd)
        
    if sd == "Top 20 mentioned LOC":
        plot(aljazeera_loc,sd)

def cnn_news():
    cnn_person = sorting(read_data(cnn_person_link))
    cnn_norp = sorting(read_data(cnn_norp_link))
    cnn_org =  sorting(read_data(cnn_org_link))
    cnn_gpe =  sorting(read_data(cnn_gpe_link))
    cnn_loc =  sorting(read_data(cnn_loc_link))
    # cnn news
    st.header("All distribution")
    sd = st.selectbox(
        "Select a Plot", #Drop Down Menu Name
        [
            "Top 20 mentioned PERSON", #First option in menu
            "Top 20 mentioned NORP",   #Second option in menu
            "Top 20 mentioned ORG",
            "Top 20 mentioned GPE",
            "Top 20 mentioned LOC",            
        ]
    )
    if sd == "Top 20 mentioned PERSON":
        plot(cnn_person,sd)
      
    if sd == "Top 20 mentioned NORP":
        plot(cnn_norp,sd)
    
    if sd == "Top 20 mentioned ORG":
        plot(cnn_org,sd)
        
    if sd == "Top 20 mentioned GPE":
        plot(cnn_gpe,sd)
        
    if sd == "Top 20 mentioned LOC":
        plot(cnn_loc,sd)
    
def fox_news():
    fox_person = sorting(read_data(fox_person_link))
    fox_norp = sorting(read_data(fox_norp_link))
    fox_org =  sorting(read_data(fox_org_link))
    fox_gpe =  sorting(read_data(fox_gpe_link))
    fox_loc =  sorting(read_data(fox_loc_link))
    # fox news
    st.header("All distribution")
    sd = st.selectbox(
        "Select a Plot", #Drop Down Menu Name
        [
            "Top 20 mentioned PERSON", #First option in menu
            "Top 20 mentioned NORP",   #Second option in menu
            "Top 20 mentioned ORG",
            "Top 20 mentioned GPE",
            "Top 20 mentioned LOC",            
        ]
    )
    if sd == "Top 20 mentioned PERSON":
        plot(fox_person,sd)
      
    if sd == "Top 20 mentioned NORP":
        plot(fox_norp,sd)
    
    if sd == "Top 20 mentioned ORG":
        plot(fox_org,sd)
        
    if sd == "Top 20 mentioned GPE":
        plot(fox_gpe,sd)
        
    if sd == "Top 20 mentioned LOC":
        plot(fox_loc,sd)

def world():
    DATE_COLUMN = 'date'
    DATA_URL = ('world_map.csv')
    @st.cache
    def load_data():
        data = pd.read_csv(DATA_URL)
        lowercase = lambda x: str(x).lower()
        data.rename(lowercase, axis='columns', inplace=True)
        data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
        return data
    data_load_state = st.text('Loading data...')
    data = load_data()
    data_load_state.text("Done! (using st.cache)")
    st.subheader('Choose day')
    date_to_filter = st.slider('date', 1, 31, 1)
    filtered_data = data[data[DATE_COLUMN].dt.day == date_to_filter]
    st.subheader('The World map on 03-%s-22' % date_to_filter)
    st.map(filtered_data)
    if st.checkbox('Show World data'):
        st.subheader('World data')
        st.write(filtered_data)
        
def ukraine():
    DATE_COLUMN = 'date'
    DATA_URL = ('ukraine_map.csv')
    @st.cache
    def load_data():
        data = pd.read_csv(DATA_URL)
        lowercase = lambda x: str(x).lower()
        data.rename(lowercase, axis='columns', inplace=True)
        data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
        return data
    data_load_state = st.text('Loading data...')
    data = load_data()
    data_load_state.text("Done! (using st.cache)")
    st.subheader('Choose day')
    date_to_filter = st.slider('date', 1, 31, 1)
    filtered_data = data[data[DATE_COLUMN].dt.day == date_to_filter]

    st.pydeck_chart(pdk.Deck(
         map_style='mapbox://styles/mapbox/light-v9',
         initial_view_state=pdk.ViewState(
             latitude=48.3794,
             longitude=31.1656,
             zoom=4.5,
             pitch=33,
         ),
         layers=[
             pdk.Layer(
                'HexagonLayer',
                data=filtered_data,
                get_position='[lon, lat]',
                radius=300,
                elevation_scale=4,
                elevation_range=[0, 100],
                pickable=True,
                extruded=True,
             ),
             pdk.Layer(
                 'ScatterplotLayer',
                 data=filtered_data,
                 get_position='[lon, lat]',
                 get_color='[200]',
                 get_radius=15000,
             ),
         ],
     ))
    if st.checkbox('Show Ukraine data'):
        st.subheader('Ukraine data')
        st.write(filtered_data)

#driver code
if __name__ == "__main__":
    main()
