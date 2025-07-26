# 🌆 Smart City Assistant

An interactive, AI-powered assistant designed to support sustainable smart city planning and citizen engagement. Built using **Streamlit**, **FastAPI**, and **vector search**, it enables users to analyze city KPIs, summarize policies, and submit citizen feedback.

## 🚀 Features

- 📄 **Policy Document Summarization**  
  Upload `.txt` or `.csv` policy documents to receive AI-generated summaries.

- 🔍 **Vector-Based Search**  
  Perform semantic search on uploaded documents using vector embeddings.

- 📊 **Real-time KPI Dashboard**  
  Monitor water usage, air quality, and energy consumption across cities.

- 💬 **Chat with AI**  
  Ask questions about uploaded policies or smart city strategies.

- 📝 **Citizen Feedback System**  
  Submit feedback with name, category, and message for civic engagement.

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit  
- **Backend**: FastAPI  
- **AI & NLP**: OpenAI / HuggingFace models (for summarization & chat)  
- **Vector Search**: FAISS / ChromaDB / other  
- **Data Handling**: Pandas, NumPy  
- **Deployment**: Docker (Optional), Render / Railway / HuggingFace Spaces

---

## 📂 Project Structure

smart-city-assistant/
├── main.py # Streamlit UI
├── backend.py # FastAPI backend API
├── policy_utils.py # Document parsing & vector handling
├── kpi_data/ # Real-time data for city KPIs
├── feedback_store.json # Stores citizen feedback
├── requirements.txt # Dependencies
└── README.md

---

## 🧪 How to Run Locally

1. **Clone the repo**
```bash
git clone https://github.com/PendemLikhitha/smart-city-assistant.git
cd smart-city-assistant
```
Install dependencies

```bash
pip install -r requirements.txt
```
Run the backend
```bash
uvicorn backend:app --reload
```

Run the Streamlit frontend
```bash
streamlit run main.py
```
