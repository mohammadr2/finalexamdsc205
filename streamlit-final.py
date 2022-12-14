'''
DSC final project.  Imopact on EV's in CT 
''' 
import pandas as pd
import streamlit as st 
import matplotlib.pyplot as plt 
import seaborn as sns 
import folium

st.title('Impact on Electric Cars in CT')

st.subheader('EV Charging Stations Raw Dataset')
df = pd.read_csv('https://data.ct.gov/api/views/jfhb-ebu6/rows.csv?accessType=DOWNLOAD')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df)

#Pie Chart
st.subheader('Pie Chart Showing EV Model Registration')
labels = ['Tesla Model S', 'Chevy Bolt EV', ' Prius Plug-in',  'Tesla Model X', 'BMW i3', 'Nissan Leaf', 'Prius Prime', 'BMW X5']
sizes = [2323, 195, 1675, 437, 27, 595, 569, 204]
explode = [0.1, 0, 0, 0, 0, 0, 0, 0]

fig = plt.figure()
ax = fig.add_subplot()

ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax.set_title('2018 EVs Registered in CT')
ax.axis('equal')

st.pyplot(fig) 

#Bar Chart
st.subheader('Bar Chart Showing EV Charging Station Types')
plt.style.use('bmh')
fig = plt.figure()
ax = fig.add_subplot()

locations = ['Dealer Hrs', '24hr Tesla', '24hr Cust', '24hr PayLot', '6am-12pm ']
stations = [26, 19, 17, 11, 9]

ax.bar(locations, stations, color = 'red')
ax.set_title('EV Charging Station Types in CT')
ax.set_xlabel('Access Time')
ax.set_ylabel('# of Stations')

st.pyplot(fig)

#Pie Chart 
st.subheader('Pie Chart Showing the Towns with the Most EV Charging Stations')
labels = ['Stamford', 'Hartford', 'Fairfeild', 'New Haven', 'Danbury', 'East Haven']
sizes = [23, 21, 20, 13, 12, 5]
explode = [0.1, 0, 0, 0, 0, 0]

fig = plt.figure()
ax = fig.add_subplot()

ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax.set_title('Towns with the Most EV Stations')
ax.axis('equal') 

st.pyplot(fig)