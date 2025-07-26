# streamlit_app.py

import streamlit as st
import requests

st.set_page_config(page_title="Smart City Assistant", layout="wide")
st.title("🏙️ Sustainable Smart City Assistant")

tab1, tab2, tab3, tab4 = st.tabs(["City Health Summary", "Feedback", "Forecasting", "Chat Assistant"])

API_URL = "http://localhost:8000/chat/"

import time

def call_backend(query):
    try:
        start = time.time()
        print("Sending request...")
        r = requests.post(API_URL, json={"query": query}, timeout=300)
        duration = time.time() - start
        print(f"Response time: {duration:.2f}s")
        r.raise_for_status()
        return r.json().get("response", "⚠️ No response from backend.")
    except requests.exceptions.RequestException as e:
        return f"❌ Error: {str(e)}"

with tab1:
    st.subheader("📋 Document Summarization")
    text = st.text_area("Paste a city report to summarize", height=200)
    if st.button("Summarize"):
        if text.strip():
            response = call_backend(f"Summarize this: {text}")
            st.write(response)
        else:
            st.warning("Please enter some text to summarize.")

with tab2:
    st.subheader("🗣️ Citizen Feedback Insight")
    feedback = st.text_area("Paste citizen feedback")
    if st.button("Analyze Feedback"):
        if feedback.strip():
            response = call_backend(f"Analyze feedback: {feedback}")
            st.write(response)
        else:
            st.warning("Please enter feedback to analyze.")

with tab3:
    st.subheader("📊 KPI Forecasting / Anomaly Detection")
    kpi = st.text_input("Enter KPI name (e.g., traffic, pollution)")
    if st.button("Forecast KPI"):
        if kpi.strip():
            response = call_backend(f"Forecast and detect anomaly in {kpi} levels over the next month")
            st.write(response)
        else:
            st.warning("Please enter a KPI name.")

with tab4:
    st.subheader("💬 Chat with Assistant")
    user_query = st.text_input("Ask something about the city...")
    if st.button("Ask"):
        if user_query.strip():
            response = call_backend(user_query)
            st.write(response)
        else:
            st.warning("Please enter your query.")
