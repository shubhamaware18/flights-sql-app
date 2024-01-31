import streamlit as st
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
        st.selectbox('Source',sorted(city))

    with col1:
        st.selectbox('Destination',sorted(city))

    # creating a Button
    if st.button('Search'):
        pass
    
elif user_option == 'Analytics':
    st.title('Analytics')
else:
    st.title('About the Project')
