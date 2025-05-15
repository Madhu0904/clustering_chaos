import streamlit as st
import pandas as pd

st.title("🏥 MedBill Shield – Hospital Billing Fraud Detector")

uploaded_file = st.file_uploader("Upload Hospital Billing CSV", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("Uploaded Data")
    st.dataframe(df)

    # Simple anomaly rules
    df['Overbilling'] = df['ProcedureCost'] > df['StandardCost']
    df['DuplicateFlag'] = df.duplicated(subset=['PatientID', 'VisitDate', 'ProcedureCode'], keep=False)
    df['HighCost'] = df['ProcedureCost'] > 1000

    df['FraudRisk'] = df[['Overbilling', 'DuplicateFlag', 'HighCost']].any(axis=1)

    st.subheader("🔍 Fraud Risk Detection")
    st.dataframe(df[['PatientID', 'ProcedureCode', 'ProcedureCost', 'FraudRisk']])
