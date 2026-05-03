# 💼 Career Ideas – Click Here to Open the App!

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Tests](https://img.shields.io/badge/Tests-Pytest-green)
![Coverage](https://img.shields.io/badge/Coverage-60%25+-brightgreen)

Career Ideas is an interactive Streamlit web app that helps users explore careers based on education level, salary expectations, and skill set.

It combines:
- 🕸️ Web scraping from the U.S. Bureau of Labor Statistics (BLS)
- 🌐 Public API integration (BLS Quit Rate data)
- 🗄️ SQLite database storage
- 📊 Data visualizations
- 🤖 AI-powered career assistant using Azure OpenAI (ChatGPT)

---

# 📦 Features

- 🕸️ Scrapes real job data from BLS Occupational Outlook Handbook
- 🌐 Uses BLS Public API for quit rate statistics
- 🗄️ Stores structured job data in SQLite database
- 🔍 Smart job matching system based on:
  - Education level
  - Salary expectations
  - Top 3 skills
- 📊 Interactive charts (skills + labor trends)
- 🤖 AI career assistant powered by Azure OpenAI
- 🎯 Streamlit multi-tab interface with navigation system
- 🧪 Fully tested with pytest + mocking

---

# 🤖 ChatGPT Integration

This project uses Azure OpenAI (ChatGPT) to provide career guidance.

The AI can:
- Explain job matches
- Give salary insights
- Recommend careers based on skills
- Help users understand education requirements

User data (education, salary, skills, and job results) is sent as context to the model and responses are streamed in the Streamlit chat UI.

---

# 🛠️ Setup & Run Instructions

## 2️⃣ Create virtual environment
```bash
python -m venv venv
```

Activate:

```
# Mac/Linux
source venv/bin/activate
# Windows
venv\Scripts\activate
```

## 3️⃣ Install dependencies
```
pip install -r requirements.txt
```

## 4️⃣ Add API keys
Create a file:
```
.streamlit/secrets.toml
```

Then add:
```
AZURE_OPENAI_API_KEY = "your_api_key"
AZURE_OPENAI_ENDPOINT = "your_endpoint"
AZURE_OPENAI_MODEL = "your_model"
```

## ▶️ Run the app
```
streamlit run app.py
```
---

# 🧪 Testing

This project uses pytest with mocking to test scraping, API handling, database logic, and core filtering.

## ✔ What is tested:
- Web scraping functions
- API responses (mocked)
- SQLite database creation & queries
- Core job-matching logic

## ▶ Run tests
```
pytest -v
```

## 📊 Run coverage
```
pytest --cov
```

---

# 📊 Data Sources

- U.S. Bureau of Labor Statistics (BLS)
- BLS Public API (Quit Rates)
- Occupational Outlook Handbook

---

# 🧠 Project Structure
```
Career-Ideas/
│
├── app.py              # Streamlit frontend
├── logic.py            # Job filtering logic
├── scrap.py            # Web scraping module
├── api.py              # API integration
├── db.py              # SQLite database setup
├── ai.py              # Azure OpenAI integration
│
├── test_scraper.py    # Database tests
├── test_api.py        # API tests (mocked)
├── test_logic.py      # Logic tests
│
├── job_list.db
└── requirements.txt
```
---

# 🚀 Deployment

Deploy on Streamlit Cloud:

1. Push repo to GitHub  
2. Go to https://streamlit.io/cloud  
3. Click "Create App"  
4. Select repository  
5. Set main file: app.py  
6. Add secrets in Advanced Settings  
7. Click Deploy  

---

# 🎯 What This Project Demonstrates

- Web scraping + data extraction
- API integration with error handling
- SQLite database design
- Streamlit interactive UI
- AI integration using LLMs
- Unit testing with mocks
- Data visualization

---

# 👨‍💻 Author

Miri Selengut
GitHub: https://github.com/miriselengut