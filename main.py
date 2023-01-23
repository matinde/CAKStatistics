import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title('CAK Statistics: 2017 - Present')

# Load data
df = pd.read_csv('cakstats_clean.csv')

# show a bar plot of Period vs Total Mobile (SIM) Subcriptions


# create a three tabs in the main page
tab = st.sidebar.radio("Choose a tab", ["Mobile Subscriptions", "Tab 2", "Tab 3"])

# Tab 1
if tab == "Mobile Subscriptions":
    st.header("Mobile Subscriptions")
    st.write("Total mobile subscriptions in the country. This corresponds to total of \
    all active mobile subscriptions in the country including both prepaid and postpaid subscriptions.")
    
    fig = px.bar(df, x='Total Mobile (SIM) Subscriptions', y='Unnamed: 0', )
    st.plotly_chart(fig)


    operators_df = df[['Unnamed: 0', 'Safaricom SIM Subscription - Prepaid', 
                                     'Safaricom SIM Subscription - Postpaid',
                                     'Airtel Kenya SIM Subscription - Prepaid',
                                     'Airtel Kenya SIM Subscription - Postpaid',
                                     'Telkom Kenya SIM Subscription - Prepaid',
                                     'Telkom Kenya SIM Subscription - Postpaid',
                                     'Equitel SIM Subscription - Prepaid',
                                     'Equitel SIM Subscription - Postpaid',
                                        ]]

    # create a dropdown to select the period
    period = st.selectbox("Select a period", operators_df['Unnamed: 0'].unique())

    # filter the dataframe based on the selected period and display it as a Pandas Series
    operators_df_new = operators_df[operators_df['Unnamed: 0'] == period]
    operators_df_new = operators_df_new.T
    operators_df_new.columns = ['Subscriptions']
    operators_df_new = operators_df_new.iloc[1:]
    st.write(operators_df_new)
