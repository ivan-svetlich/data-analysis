# Titanic survival prediction App
Titanic's passenger survival prediction Web App. Inspired by Kaggle's [Titanic - Machine Learning from Disaster](https://www.kaggle.com/c/titanic) competition.


## Table of contents
* [General Info](#general-info)
* [Technologies](#technologies)
* [Appearance](#appearance)
* [Setup](#setup)

## General info
This Web App uses a Support-Vector Clustering (SVC) Machine Learning model to predict passenger survival based on the stats provided as paramaters.

## Technologies
### This project was created with:
* Python 3
* scikit-learn
* Streamlit

## Appearance

![app](https://github.com/ivan-svetlich/data-analysis/blob/main/titanic-webApp/images/titanic.png)

## Setup
1. **titanic_WebApp.py** and **train.csv** files must be in the same folder.
2. In Anaconda Navigator go to Enviroments > base (root) > Open Terminal.
3. If you haven't installed Streamlit yet, run ```pip install streamlit```
4. Execute ```streamlit run (path to file)/titanic_WebApp.py```
5. The App should automatically open in browser. Otherwise, use the URL provided by Streamlit in the Terminal.
