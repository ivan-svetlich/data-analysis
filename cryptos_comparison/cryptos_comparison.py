# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 13:24:56 2021

@author: ivans
"""

import pandas as pd
import os

from datetime import datetime

import matplotlib.pyplot as plt
import matplotlib
plt.style.use('classic')
import streamlit as st

matplotlib.rcParams['figure.figsize'] = (12,8)

pd.options.mode.chained_assignment = None

df_dict = {}
directory = os.path.join(os.getcwd(), "data")
for root,dirs,files in os.walk(directory):
    for file in files:
       if file.endswith(".csv"):
        file_name = os.path.splitext(file)[0]
        file_path = os.path.join(directory, file_name)
        df_dict[file_name] = pd.read_csv(file_path + ".csv")
        
#Streamlit WebApp

st.write("""
# Cryptocurrencies Comparison App
""")

st.sidebar.header('User Input Parameters')

names = list(df_dict.keys())

def user_input_features():
    first = st.sidebar.selectbox('First currency',names)
    second = st.sidebar.selectbox('Second currency',names)
    
    first_latest = df_dict[first]['Price'].iloc[-1]
    second_latest = df_dict[second]['Price'].iloc[-1]
    data = {'Name': [first, second],
            'Current_Price': [first_latest, second_latest]
            }
    features = pd.DataFrame(data)
    return features


df = user_input_features()
	
st.subheader('Selected currencies')
st.write(df)

st.subheader('Exchange rate')

exchange_rate = float(df.iloc[0].Current_Price) / float(df.iloc[1].Current_Price)
str_first = '1 ' + df.Name[0] + ' equals ' + str(exchange_rate) + ' ' + df.Name[1]
str_second = '1 ' + df.Name[1] + ' equals ' + str((1/exchange_rate)) + ' ' +  df.Name[0]

st.text(str_first)
st.text(str_second)

st.subheader('Price evolution')

fig = plt.figure()
plt.title("Cryptocurrencies Price Evolution")
plt.xlabel("Year")
plt.ylabel("Price (USD)")
legends = []

selected_names = list(df.Name)
selected_cryptos = { name: df_dict[name] for name in selected_names }
for name, data in selected_cryptos.items():
    dates = []
    for date in data.Date:
        dates.append(datetime.strptime(date, '%Y-%m-%d'))
    legends.append(name)
    plt.plot(dates, data.Price)
    plt.gcf().autofmt_xdate()
plt.grid()    
plt.legend(legends)
st.write(fig)



