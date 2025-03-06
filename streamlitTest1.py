import streamlit as st
from joblib import load
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_excel('BCI backup.xlsx', sheet_name='Dummy leads')
df = df.fillna('None')
def checkRows(row):
    row['Booking_Lead_Time'] = int(row['Booking_Lead_Time'].replace(' days', ''))
    row['Add_Ons'] = len(row['Add_Ons'].replace(' ', '').split(';'))
    return row

df = df.apply(checkRows, axis=1)
age_labels = ['KID', 'YOUNG', 'OLD']
df['Age'] = pd.cut(df['Age'], bins=3, labels=age_labels)
other_labels = ['LOW', 'MEDIUM', 'HIGH']
df_filtered = df.select_dtypes(include=['int64', 'float64', 'datetime64[ns]'])
for i in df_filtered.columns:
    df[i] = pd.cut(df[i], bins=3, labels=other_labels)

unwanted_columns = ['Lead_ID', 'Booking_ID', 'Customer name', 'Location']
df = df.drop(unwanted_columns, axis=1)



to_predicted = df.iloc[0]
customercolumns = ['Lead_Source', 'First_Time_Buyer', 'Age', 'Gender', 'Income', 'OEM_Loyalty_Program']

customermodel = load('bcimodels.pkl')
model1values = to_predicted[customercolumns]
df_customermodel = customermodel['customer']['model']
predictedcustomer = df_customermodel.predict(model1values).to_numpy()[0]
exp1 = customermodel['customer']['explainer']
breakdown = exp1.predict_parts(to_predicted[customercolumns], type='break_down', label='Customer Profile')
st.write(f"Prediction: {predictedcustomer * 100}")
st.table(breakdown.result)
fig = breakdown.plot(show=False, title='Aditi Joshi')
st.plotly_chart(fig)

