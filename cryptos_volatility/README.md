# Cryptocurrencies Volatility Visualization App
Basic Web App that shows price evolution, standard deviation and coefficient of variation of the most popular cryptocurrencies.

## Table of contents
* [General Info](#general-info)
* [Technologies](#technologies)
* [Appearance](#appearance)
* [Setup](#setup)

## General info
This app displays price data of the top 50 cryptocurrencies up to 2021. User can select cryptocurrency name, year, and whether standard deviation or coefficient of variation (ratio of the standard deviation to the mean) is used to measure price dispersion.

Data source: [Kaggle - TOP 50 Cryptocurrencies Historical Prices](https://www.kaggle.com/odins0n/top-50-cryptocurrency-historical-prices)

## Technologies
### This project was created with:
* Python 3
* Streamlit
* pandas

## Appearance

![price](https://github.com/ivan-svetlich/data-analysis/blob/main/cryptos_volatility/images/price.png)

![standard_deviation](https://github.com/ivan-svetlich/data-analysis/blob/main/cryptos_volatility/images/standard_deviation.png)

![coefficient_of_variation](https://github.com/ivan-svetlich/data-analysis/blob/main/cryptos_volatility/images/coefficient_of_variation.png)

## Setup
1. **cryptos_volatility.py** file and **data** folder must be in the same directory.
2. In Anaconda Navigator go to Enviroments > base (root) > Open Terminal.
4. Move to file location ```cd [file location path]```
5. Execute ```streamlit run cryptos_volatility.py```
6. The App should automatically open in browser. Otherwise, use the URL provided by Streamlit in the Terminal.
