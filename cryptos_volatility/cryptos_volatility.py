# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 10:46:10 2021

@author: ivans
"""

import pandas as pd
import numpy as np
import os
from datetime import datetime

import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (12,8)

import streamlit as st

pd.options.mode.chained_assignment = None

df_dict = {}
directory = (r'C:\Users\ivans\Documents\Data Analysis\Crypto')
for root,dirs,files in os.walk(directory):
    for file in files:
       if file.endswith(".csv"):
        file_name = os.path.splitext(file)[0]
        file_path = r'C:\Users\ivans\Documents\Data Analysis\Crypto\\' + file
        df_dict[file_name] = pd.read_csv(file_path)
        
#Streamlit WebApp

st.write("""
# Cryptocurrencies' Volatility Visualization
""")

st.sidebar.header('User Input Parameters')

names = list(df_dict.keys())

selected_crypto = st.sidebar.selectbox('Currency',names)

df_selected = df_dict[selected_crypto]
df_selected_date = pd.to_datetime(df_selected.Date, infer_datetime_format=True)  
year_range = pd.date_range(str(df_selected_date.min()),str(df_selected_date.max()),freq='Y').strftime("%Y").tolist()
year_range.append(str(df_selected_date.max().year))

selected_year = st.sidebar.selectbox('Year',year_range)

selected_measure = st.sidebar.selectbox('Measure', ["Standard deviation", "Coefficient of variation"])

if selected_year is not None:
    df_selected['Date'] = df_selected_date
    
    mask = df_selected['Date'].dt.year == int(selected_year)
    df_year = df_selected[mask]
    df_year['Date'] = pd.to_datetime(df_year.Date, infer_datetime_format=True)  
    months = df_year.groupby(pd.Grouper(key='Date', freq='M'))
    df_year_months = [group for _,group in months]
    
    measure = []
    for month in df_year_months:
        avg = (month.Price).mean()
        std_dev = np.sqrt(sum(((month.Price - avg) ** 2)) / len(month.Price))
        if selected_measure == "Coefficient of variation":
            measure.append(std_dev /avg)
        elif selected_measure == "Standard deviation":
            measure.append(std_dev)
        
    start_date = selected_year + '-01-01'
    end_date = selected_year + '-' + str(len(measure)) + '-01'
    month_range = (pd.date_range(start_date,end_date,freq='MS')).strftime("%Y-%b").tolist()
    month_range = [datetime.strptime(x, '%Y-%b') for x in month_range]
    
    
    df_selected['Date'] = pd.to_datetime(df_selected.Date, infer_datetime_format=True)  
    
    dates = df_selected['Date'].tolist()
    # for date in df_selected.Date:
    #     dates.append(datetime.strptime(date, '%Y-%m-%d'))
    
    st.subheader('Price Evolution')
    fig1 = plt.figure()
    plt.title("{} Price Evolution".format(selected_crypto))
    plt.xlabel("Year")
    plt.ylabel("Price (USD)")
    plt.plot(dates, df_selected.Price)
    plt.gcf().autofmt_xdate()
    st.write(fig1)
    
    if selected_measure is not None:
        st.subheader(selected_measure)
        fig2 = plt.figure()
        plt.title(r"{}'s price monthly {} ({})".format(selected_crypto,selected_measure,selected_year))
        plt.xlabel("Month")
        plt.ylabel("Coefficient of variation")
        plt.plot(month_range, measure)
        plt.gcf().autofmt_xdate()
        st.write(fig2)
