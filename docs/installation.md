<p align="center">

# ⚙️ AI SQL Agent Installation Guide

### Setup & Configuration

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

</p>

---

# 📋 Prerequisites

Before installing AI SQL Agent, ensure you have:

- Python 3.11 or later
- Git
- MySQL Server
- MongoDB Server
- Ollama (optional for local AI models)
- Internet connection (for OpenAI/Anthropic)

---

# 📥 Clone the Repository

```bash
git clone https://github.com/satya66123/AI-SQL-Agent.git

cd AI-SQL-Agent
```

---

# 🐍 Create a Virtual Environment

```bash
python -m venv .venv
```

### Activate the Virtual Environment

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

---

# 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install streamlit pandas pymysql pymongo sqlparse openpyxl reportlab python-dotenv requests
```

---

# ⚙️ Configure Environment

Create a `.env` file in the project root.

```env
# AI Providers
OLLAMA_HOST=http://localhost:11434
OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key

# MySQL
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DATABASE=your_database

# MongoDB
MONGO_URI=mongodb://localhost:27017/
MONGO_DATABASE=your_database
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open in your default browser at:

```
http://localhost:8501
```

---

# ✅ Verify Installation

Check the following:

- Application launches successfully
- MySQL connection is established
- MongoDB connection is established
- AI provider loads correctly
- Natural language queries execute successfully

---

# 🛠 Troubleshooting

### Missing Module

```bash
pip install -r requirements.txt
```

### MySQL Connection Error

- Ensure MySQL Server is running.
- Verify host, username, password, and database name.

### MongoDB Connection Error

- Ensure MongoDB Server is running.
- Verify `MONGO_URI` and database name.

### Ollama Connection Error

Start Ollama:

```bash
ollama serve
```

Verify available models:

```bash
ollama list
```

---

# 🎉 Installation Complete

Your AI SQL Agent is now ready to generate AI-powered SQL and MongoDB queries.