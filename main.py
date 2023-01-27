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
    
    fig = px.bar(df, x='Total Mobile (SIM) Subscriptions', y='PERIOD', )
    st.plotly_chart(fig)

    st.title("Mobile Subscriptions by Operator in quarterly basis")
    st.write("The data here views the subscrition by operator in quarterly basis from 2017 to 2022.")

    operators_df = df[[
                        'PERIOD', 
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


    period = st.selectbox("Select a period", operators_df['PERIOD'].unique())

    # create two columns
    

    
    operators_df_new = operators_df[operators_df['PERIOD'] == period]
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
        operators_df_new = operators_df[operators_df['PERIOD'].str.contains('October - December ' + year)]
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

    # Create a line chart of the columns: Safaricom PLC On-net, Safaricom PLC Off-net, Airtel Kenya On-net, Airtel Kenya Off-net, Telkom Kenya On-net, Telkom Kenya Off-net, Equitel On-net, Equitel Off-net
   
    # create line chart of the data

    st.title("Mobile on and off-net calls by Operator")
    st.write("You can view the data of how many on and off-net calls per year various operators had.")
   
    net_calls_df = df[[
                        'Safaricom PLC On-net',
                        'Airtel On-net',
                        'Telkom On-net',
                        'Equitel On-net',
                    ]]

    net_calls_df.set_index(df['PERIOD'], inplace=True)

     # reverse the index
    net_calls_df = net_calls_df.iloc[::-1]
        
    # create a line chart of the data with the index of df as the x axis
    fig3 = px.line(net_calls_df, labels={'value': 'Calls', 'variable': 'Operator', 'index': 'Period'}, 
                    title="On-net Calls by Operator")
    
    st.plotly_chart(fig3)

    offnet_calls_df = df[[
                        'Safaricom PLC Off-net',
                        'Airtel Off-net',
                        'Telkom Off-net',
                        'Equitel Off-net',
                    ]]

    offnet_calls_df.set_index(df['PERIOD'], inplace=True)

    # reverse the index
    offnet_calls_df = offnet_calls_df.iloc[::-1]
    # create a line chart of the data with the index of df as the x axis
    fig4 = px.line(offnet_calls_df, labels={'value': 'Calls', 'variable': 'Operator', 'index': 'Period'}, 
                    title="Off-net Calls by Operator")
    
    st.plotly_chart(fig4)
