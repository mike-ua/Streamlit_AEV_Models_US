import streamlit as st
import pandas as pd
import plotly.express as px

st.subheader('Alternative Energy Vehicles (U.S.)')
st.write('Light Duty Vehicles, though July 17, 2024')

#col1, col2 = st.columns(2)

#with col1:
# Read and filter the dataframe
df = pd.read_csv('https://github.com/mike-ua/Streamlit-Data/blob/main/light-duty-vehicles-2024-07-17.csv?raw=true')
df = df[df['Fuel_Code'].isin(['ELEC', 'HYBR', 'PHEV'])]

# Convert 'Model_Year' to string for display
df['Model_Year'] = df['Model_Year'].astype(str)

# Group by 'Model_Year' and 'Fuel_Code', then count and reshape
grouped_df = df.groupby(['Model_Year', 'Fuel_Code']).size()
reshaped_df = grouped_df.unstack(level='Fuel_Code')

# Display the DataFrame with formatted 'Model_Year' column
st.dataframe(reshaped_df)

#with col2:
# Convert 'Model_Year' to numeric, round, and then 'Int64'
df['Model_Year'] = pd.to_numeric(df['Model_Year'], errors='coerce').astype('Int64')

# Group by 'Model_Year' and 'Fuel_Code', then sum
line_chart_df = df.groupby(['Model_Year', 'Fuel_Code']).size().unstack(level='Fuel_Code').fillna(0)

# Create a Plotly line chart
fig = px.line(line_chart_df, x=line_chart_df.index, y=line_chart_df.columns, title='Total MODELS of Electric Cars')

# Display the Plotly figure
st.plotly_chart(fig)

st.write('source: https://afdc.energy.gov/')


st.divider()

st.subheader('Data Analysis Tools Used')
st.markdown('**Dataset:** .csv file')
st.markdown('**Python:** create the basic script')
st.markdown('**Pandas:** data manipulation')
st.markdown('**Plotly:** create the main visualization')
st.markdown('**Streamlit:** Python framework to share the script, e.g. web app')
st.markdown('**Github:** developer platform for hosting the script and data file')


