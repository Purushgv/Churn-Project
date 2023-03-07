# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pickle
import streamlit as st

# loading the trained model

#import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
pickle_in = open('C:\\Users\\Purushothama G V\\Documents\\DSP\\filename.pkl', 'rb')
model_df = pickle.load(pickle_in)

st.title('Model Deployment: Churn Prediction')

st.sidebar.header('User Input Parameters')

df = pd.read_csv("G:\\EXCELR\\PROJECT\\Problem Statement & Dataset\\Churn.csv")
y=df["churn"]
X=df.drop(df.columns[[0,1,-3]], axis = 1,inplace=True)

from sklearn.model_selection import train_test_split
Xtrain,Xtest,ytrain,ytest=train_test_split(X,y,test_size=0.3,random_state=42)

model_df =DecisionTreeClassifier(criterion="gini",random_state=42,max_depth=6,min_samples_leaf=8)

#Model Fitting
model_df.fit(Xtrain,ytrain)

y_pred=model_df.predict(Xtest)

def churn_prediction(account_length,voice_plan,voice_messages,intl_plan,intl_mins,intl_calls,intl_charge,day_mins,day_calls,day_charge,eve_mins,eve_calls,eve_charge,night_mins,night_calls,night_charge,customer_calls,churn):
    if voice_plan == "No":
        voice_plan = 0
    else:
        voice_plan = 1
    if intl_plan == "No":
        intl_plan = 0
    else:
        intl_plan = 1  
    prediction=model_df.predict(Xtrain)
    print(prediction)
    if prediction[0]==0:
        return("Customer will not churn")
    else:
        return("Customer will churn")

def main():
    st.title("Churn Prediction")
    account_length=st.sidebar.number_input("Enter the Account Length")
    voice_plan=st.sidebar.selectbox("Do you have a Voice plan",("No","Yes"))
    voice_messages=st.sidebar.number_input("Enter the number of voice messages")
    intl_plan=st.sidebar.selectbox("Do you have a international plan", ("No","Yes"))
    intl_mins=st.sidebar.number_input("Enter the total international mins")
    intl_calls=st.sidebar.number_input("Enter the number of international calls")
    intl_charge=st.sidebar.number_input("Enter the total INTL charge")
    day_mins=st.sidebar.number_input("Enter the total day mins")
    day_calls=st.sidebar.number_input("Enter the number of day calls")
    day_charge=st.sidebar.number_input("Enter the total day charge")
    eve_mins=st.sidebar.number_input("Enter the total evening mins")
    eve_calls=st.sidebar.number_input("Enter the number of Evening calls")
    eve_charge=st.sidebar.number_input("Enter the total evening charge")
    night_mins=st.sidebar.number_input("Enter the total night mins")
    night_calls=st.sidebar.number_input("Enter the number of Night calls")
    night_charge=st.sidebar.number_input("Enter the total night charge")
    customer_calls=st.sidebar.number_input("Enter the total customer calls")
    #international_mins=st.sidebar.number_input("Enter the total international mins")
    #customer_service_calls=st.sidebar.number_input("Enter the number of CS calls")
    #international_plan=st.sidebar.selectbox("Do you have a international plan", ("No","Yes"))
    #day_calls=st.sidebar.number_input("Enter the number of day calls")
    #day_charge=st.sidebar.number_input("Enter the total day charge")
    #evening_calls=st.sidebar.number_input("Enter the number of Evening calls")
    #evening_charge=st.sidebar.number_input("Enter the total evening charge")
    #night_calls=st.sidebar.number_input("Enter the number of Night calls")
    #night_charge=st.sidebar.number_input("Enter the total night charge")
    #international_calls=st.sidebar.number_input("Enter the number of INTL calls")
    #international_charge=st.sidebar.number_input("Enter the total INTL charge")
    #total_charge=st.sidebar.number_input("Enter the total charge")
    
    churn=''
    if st.button('Churn results web app'):
        churn=churn_prediction(account_length,voice_plan,voice_messages,intl_plan,intl_mins,intl_calls,intl_charge,day_mins,day_calls,day_charge,eve_mins,eve_calls,eve_charge,night_mins,night_calls,night_charge,customer_calls)
        st.success('the output is {}'.format(churn))

if __name__=='__main__': 
    main()
