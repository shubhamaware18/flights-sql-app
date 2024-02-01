import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from dbhelper import DB

# creating a object of DB class
db = DB()


# create sidebar
st.sidebar.title("Flight's Analytics")

# Dropdown
user_option = st.sidebar.selectbox('Menu',['Select One', 'Check Flights', 'Analytics'])

# set condition
if user_option == 'Check Flights':
    st.title('Check Flights')
    
    col1, col2 = st.columns(2)
    
    city = db.fetch_city_names()
    with col1:
        source = st.selectbox('Source',sorted(city))

    with col1:
        destination = st.selectbox('Destination',sorted(city))

    # creating a Button
    if st.button('Search'):
        results = db.fetch_all_flights(source, destination)
        #st.dataframe(results)
        # Display column names
        st.write("### Flight Information")
        st.write("Airline, Route, Dep_time, Duration, Price")

        # Convert results to a DataFrame
        df = pd.DataFrame(results, columns=["Airline", "Route", "Dep_time", "Duration", "Price"])

        # Display DataFrame
        st.dataframe(df)

elif user_option == 'Analytics':
    st.title('Analytics')
    airline, frequency = db.fetch_airline_frequency()
    
    # ploting Graph
    fig = go.Figure(
        go.Pie(
            labels = airline,
            values = frequency,
            hoverinfo = 'label+percent',
            textinfo= 'value'
        )
    )
    st.header('Pie Chart')
    st.plotly_chart(fig)

else:
    st.title('About the Project')
