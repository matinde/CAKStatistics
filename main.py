import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title('CAK Statistics: 2017 - Present')

# Load data
df = pd.read_csv('cakstats_clean.csv')

# Sidebar
st.sidebar.title("Navigation")
st.sidebar.write("Is this working?")
tab = "Mobile Subscriptions"
mobile_subs_button = st.sidebar.button("Mobile Subscriptions")
mobile_money_subs_button = st.sidebar.button("Mobile Money Subscriptions")
internet_subs_button = st.sidebar.button("Internet Subscriptions")

if mobile_subs_button:
    tab = "Mobile Subscriptions"
if mobile_money_subs_button:
    tab = "Mobile Money Subscriptions"
if internet_subs_button:
    tab = "Internet Subscriptions"




# Tab 1
if tab == "Mobile Subscriptions":
    st.header("Mobile Subscriptions")
    st.write("Total mobile subscriptions in the country. This corresponds to total of \
    all active mobile subscriptions in the country including both prepaid and postpaid subscriptions.")
    
    fig = px.bar(df, x='Total Mobile (SIM) Subscriptions', y='Unnamed: 0', )
    st.plotly_chart(fig)

    st.title("Mobile Subscriptions by Operator in quarterly basis")
    st.write("The data here views the subscrition by operator in quarterly basis from 2017 to 2022.")

    operators_df = df[[
                        'Unnamed: 0', 
                        'QUARTER',
                        'Safaricom SIM Subscription - Prepaid', 
                        'Safaricom SIM Subscription - Postpaid',
                        'Airtel Kenya SIM Subscription - Prepaid',
                        'Airtel Kenya SIM Subscription - Postpaid',
                        'Telkom Kenya SIM Subscription - Prepaid',
                        'Telkom Kenya SIM Subscription - Postpaid',
                        'Equitel SIM Subscription - Prepaid',
                        'Equitel SIM Subscription - Postpaid',
                    ]]


    period = st.selectbox("Select a period", operators_df['Unnamed: 0'].unique())

    # create two columns
    

    
    operators_df_new = operators_df[operators_df['Unnamed: 0'] == period]
    if operators_df_new.empty:
        st.error("No data found for the selected period.")
    else:
        operators_df_new = operators_df_new.T
        col_name = ['Subscriptions']*operators_df_new.shape[1]
        col_name = col_name[:operators_df_new.shape[1]]
        operators_df_new.columns = col_name
        operators_df_new = operators_df_new.iloc[1:]
        st.write(operators_df_new)

    
    st.title("Mobile Subscriptions by Operator Annually")
    st.write("You can view the data of how many subscription per year various operators had. Data for the current year, still awaiting release.")
    # create a slider of the period but by year only
    year = st.slider("Select a year", 2017, 2022)
    col1, col2 = st.columns(2)
    with col1:
        
        year = str(year)
        operators_df_new = operators_df[operators_df['Unnamed: 0'].str.contains('October - December ' + year)]
        if operators_df_new.empty:
            st.error("No data found for the selected year.")
        else:
            operators_df_new = operators_df_new.T
            col_name = []
            for i in range(operators_df_new.shape[1]):
                col_name.append(f"{year}")
            operators_df_new.columns = col_name
            operators_df_new = operators_df_new.iloc[1:]
            st.write(operators_df_new)

    with col2:
        fig = px.pie(operators_df_new, values=operators_df_new.iloc[:, 0], names=operators_df_new.index, hole=.3)
        st.plotly_chart(fig)

    #