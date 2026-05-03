# Career-Ideas
💼 Career Ideas – AI-Powered Job Explorer
📌 Overview

Career Ideas is a full-stack Python + Streamlit web application that helps users explore careers based on education level, salary expectations, and skill sets.

The project combines:

🕸️ Web scraping from the U.S. Bureau of Labor Statistics (BLS)
🌐 Public API integration (BLS Quit Rate dataset)
🗄️ SQLite database for persistent job storage
📊 Data visualization (skills + labor trends)
🤖 AI-powered career assistant using Azure OpenAI (ChatGPT)

The goal is to provide users with personalized career recommendations and labor insights in an interactive dashboard.

🚀 Features
🔍 Job Matching System
Filter jobs by:
Education level
Salary expectation
Top 3 skills
Ranked job recommendations using a scoring algorithm

🕸️ Web Scraping
Scrapes data from:
U.S. Bureau of Labor Statistics Occupational Outlook Handbook
Extracts:
Job titles
Salary data
Education requirements
Skills
Job descriptions
Stores results in SQLite database

🌐 API Integration
Uses BLS Public API:
Quit rate time-series data
Includes:
Error handling
API failure fallback dataset
JSON parsing and transformation

🗄️ Database (SQLite)

The system supports persistent storage of job data with:

Job name
Salary
Education level
Skills
Job descriptions
Work environment

Database operations include:

Insert (load_db)
Query (filters + ranking)
Structured schema design

📊 Data Visualization

Two dynamic charts:

📊 Skill importance by education level (bar chart)
📉 Quit rate trends over time (scatter chart)

Both charts update based on user input.

🤖 AI Career Assistant (Azure OpenAI)

The app includes a ChatGPT-powered assistant that:

Explains job matches
Gives career advice
Interprets salary expectations
Analyzes user skills and education

The AI is context-aware and receives:

Selected education level
Salary goal
Chosen skills
Matched job dataset


🧠 AI Prompt Behavior

The assistant is restricted to career guidance only:

Career advice
Salary interpretation
Job recommendations
Education pathways

It avoids unrelated topics and redirects conversations back to career planning.


🧪 Testing

This project includes a full pytest test suite with mocking and database validation.

✔️ Test Coverage Includes:
🔹 Web Scraper / Database
Database creation validation
Data retrieval from SQLite
🔹 API (Mocked)
Valid API response parsing
Missing key handling
Invalid data structure handling
API limit fallback behavior
Edge case validation
🔹 Core Logic
Job filtering pipeline correctness
Skill weighting by education level
▶️ Run Tests
pytest
📊 Coverage Report
coverage run -m pytest
coverage report -m

Goal: ≥ 60% test coverage

📁 Project Structure
Career-Ideas/
│
├── app.py                 # Streamlit frontend
├── logic.py              # Core filtering & query logic
├── scrap.py              # Web scraping module
├── api.py                # BLS API integration
├── db.py                 # SQLite database setup
├── ai.py                 # Azure OpenAI integration
│
├── test_scraper.py       # Database + scraping tests
├── test_api.py           # API mock tests
├── test_logic.py         # Core logic tests
│
├── job_list.db           # SQLite database
├── requirements.txt
└── README.md
⚙️ Installation & Setup
1. Clone repository
git clone https://github.com/YOUR_USERNAME/Career-Ideas.git
cd Career-Ideas
2. Create virtual environment
python -m venv venv

Activate:

# Mac/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
🔑 Environment Variables (Secrets)

Create:
.streamlit/secrets.toml

Add:
AZURE_OPENAI_API_KEY = "your_key"
AZURE_OPENAI_ENDPOINT = "your_endpoint"
AZURE_OPENAI_MODEL = "your_model"

⚠️ Do NOT commit this file to GitHub.

▶️ Run the Application
streamlit run app.py
🌐 Deployment

The application is deployed on Streamlit Cloud:

👉 https://your-streamlit-app-link

📈 Key Technologies
Python
Streamlit
SQLite3
BeautifulSoup
Requests
Pandas
Azure OpenAI API
Pytest

📌 Future Improvements
Add full CRUD UI (update/delete jobs)
Improve scraping reliability
Expand API sources (Glassdoor / Indeed / etc.)
Improve recommendation algorithm (ML-based)
Increase test coverage beyond 60%
Add authentication system
👨‍💻 Author

Your Name
GitHub: https://github.com/YOUR_USERNAME

🏁 Summary
This project demonstrates:

Web scraping + structured data pipelines
API integration with error handling
SQL database design
Interactive Streamlit dashboards
AI integration using LLMs
Unit testing with mocks and edge cases