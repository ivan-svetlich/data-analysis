# Cryptocurrencies' Price Comparison App
Basic Web App that compares price evolution of the most popular cryptocurrencies.

## Table of contents
* [General Info](#general-info)
* [Technologies](#technologies)
* [Appearance](#appearance)
* [Setup](#setup)

## General info
This app compares price evolution of two selected cryptocurrencies, among the top 50 cryptocurrencies up to 2021. 

Data source: [Kaggle - TOP 50 Cryptocurrencies Historical Prices](https://www.kaggle.com/odins0n/top-50-cryptocurrency-historical-prices)

## Technologies
### This project was created with:
* Python 3
* Streamlit
* pandas

## Appearance
![exchange_rate](https://github.com/ivan-svetlich/data-analysis/blob/main/cryptos_comparison/images/exchange_rate.png)

![price_evolution](https://github.com/ivan-svetlich/data-analysis/blob/main/cryptos_comparison/images/price_evolution.png)

## Setup
1. **cryptos_comparison.py** file and **data** folder must be in the same directory.
2. In Anaconda Navigator go to Enviroments > base (root) > Open Terminal.
4. Move to file location ```cd [file location path]```
5. Execute ```streamlit run cryptos_comparison.py```
6. The App should automatically open in browser. Otherwise, use the URL provided by Streamlit in the Terminal.
