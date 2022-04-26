import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
#Setting up our homepage window of Streamlit app
def main():
    page = st.sidebar.selectbox(
        "Select a Page",
        [
            "Homepage",
            "World Map",
            "Ukraine Map",
        ]
    )
    #First Page
    if page == "Homepage":
        homepage()
    #World Map Page
    if page == "World Map":
        world()
    #Ukraine Map Page
    if page == "Ukraine Map":
        ukraine()    
    
def homepage():
    st.write("""
        # 5. Geolocation:
        Select a page to see a map
        """)   

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
    st.subheader('Select day')
    date_to_filter = st.slider('date', 12, 31, 12)
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
    st.subheader('Select day')
    date_to_filter = st.slider('date', 12, 31, 12)
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

