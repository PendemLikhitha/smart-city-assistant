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

<img width="2879" height="1707" alt="Screenshot 2025-07-26 130642" src="https://github.com/user-attachments/assets/071dacf9-7341-40db-9235-f735bd57792a" />

<img width="2872" height="1696" alt="Screenshot 2025-07-26 130820" src="https://github.com/user-attachments/assets/371ffe75-8cf5-4bc5-8edf-0cb0931b36f1" />

<img width="2879" height="1697" alt="Screenshot 2025-07-26 131132" src="https://github.com/user-attachments/assets/11a2d6e6-11c0-4fa6-94c7-0a60508e229f" />

<img width="2879" height="1702" alt="Screenshot 2025-07-26 131949" src="https://github.com/user-attachments/assets/892b7dc9-17e0-4a4e-9236-2b2de37fc39b" />


