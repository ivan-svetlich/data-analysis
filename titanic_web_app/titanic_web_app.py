import streamlit as st
import pandas as pd
import numpy as np
import os

pd.options.mode.chained_assignment = None
# reading in the data from csv
BASE_DIR = os.getcwd()
csv_path = "train.csv"
df_train = pd.read_csv(os.path.join(BASE_DIR, csv_path))

#drop columns that won't be used for training the model
df_x_train = df_train.drop(['PassengerId', 'Survived', 'Name', 'Ticket','Cabin'], axis=1)
#'Survived' column is the target
y_train = df_train["Survived"]

#filling in the missing data
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy="median")
df_num = df_x_train.select_dtypes(include=[np.number])
imputer.fit(df_num)

X_train = imputer.transform(df_num)
df_tr = pd.DataFrame(X_train, columns=df_num.columns, index=df_x_train.index)

#Categorical features
df_cat = df_x_train.select_dtypes(exclude=[np.number])

#Filling in missing data with 'None'
df_cat = df_cat.fillna("None")

#Encoding categorical data
from sklearn.preprocessing import OrdinalEncoder

ordinal_encoder = OrdinalEncoder()
df_cat_encoded = ordinal_encoder.fit_transform(df_cat)

from sklearn.preprocessing import OneHotEncoder

cat_encoder = OneHotEncoder(sparse=False)
df_cat_1hot = cat_encoder.fit_transform(df_cat)

from sklearn.base import BaseEstimator, TransformerMixin

class DataFrameSelector(BaseEstimator, TransformerMixin):
    def __init__(self, attribute_names):
        self.attribute_names = attribute_names
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        return X[self.attribute_names]
    
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

num_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy="median")),
        ('std_scaler', StandardScaler()),
    ])

df_num_tr = num_pipeline.fit_transform(df_num)

from sklearn.compose import ColumnTransformer

num_attribs = list(df_num)
cat_attribs = list(df_cat)

full_pipeline = ColumnTransformer([
        ("num", num_pipeline, num_attribs),
        ("cat", OneHotEncoder(), cat_attribs),
    ])

df_prepared = full_pipeline.fit_transform(df_x_train)

from sklearn.svm import SVC

svm_clf = SVC(gamma="auto", probability=True)
svm_clf.fit(df_prepared, y_train)


#Streamlit WebApp

st.write("""
# Passenger Survival Prediction App
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    p_class = st.sidebar.selectbox('Class', ('1', '2', '3'))
    sex = st.sidebar.selectbox('Sex', ('male', 'female'))
    age = st.sidebar.number_input('Age', step=1)
    sib_sp = st.sidebar.number_input('SibSp', step=1)
    par_ch = st.sidebar.number_input('ParCh', step=1)
    fare = st.sidebar.number_input('Fare')
    embarked = st.sidebar.selectbox('Embarked', ('C', 'Q', 'S'))
    data = {'Pclass': int(p_class),
            'Sex': sex,
            'Age': int(age),
            'SibSp': int(sib_sp),
            'Parch': int(par_ch),
            'Fare': float(fare),
            'Embarked': embarked}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()
df_prepared = full_pipeline.transform(df)

st.subheader('Selected parameters')
st.write(df)


prediction = svm_clf.predict_proba(df_prepared)

st.subheader('Prediction')

survived = "Survived: {:.2f}%".format(100 * (prediction[0])[1])
not_survived = "Not Survived: {:.2f}%".format(100 * (prediction[0])[0])
st.write(survived)
st.write(not_survived)
