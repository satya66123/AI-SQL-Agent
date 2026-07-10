# 🤖 AI SQL Agent

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-Database-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-Database-47A248?style=for-the-badge&logo=mongodb&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-LLM-000000?style=for-the-badge)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT-412991?style=for-the-badge&logo=openai&logoColor=white)
![Anthropic](https://img.shields.io/badge/Anthropic-Claude-191919?style=for-the-badge)

</p>

<p align="center">

![GitHub stars](https://img.shields.io/github/stars/satya66123/AI-SQL-Agent?style=social)
![GitHub forks](https://img.shields.io/github/forks/satya66123/AI-SQL-Agent?style=social)
![GitHub issues](https://img.shields.io/github/issues/satya66123/AI-SQL-Agent)
![GitHub last commit](https://img.shields.io/github/last-commit/satya66123/AI-SQL-Agent)
![License](https://img.shields.io/badge/License-MIT-blue.svg)

</p>

---

# 🚀 Overview

**AI SQL Agent** is an intelligent database assistant that converts **natural language** into executable **MySQL** and **MongoDB** queries using Large Language Models.

The application supports multiple AI providers, automatic query validation, SQL repair, MongoDB repair, dashboard analytics, data visualization, export capabilities, and AI-generated explanations.

---

# ✨ Features

## 🤖 AI Providers

- ✅ Ollama
- ✅ OpenAI
- ✅ Anthropic

---

## 🗄 Database Support

- ✅ MySQL
- ✅ MongoDB

---

## 💬 Natural Language Queries

Examples:

```
Show all employees

Show employees earning more than 70000

Show customers from Hyderabad

Show all products
```

AI automatically generates executable SQL or MongoDB queries.

---

## 🧠 AI Explanation

Every query includes:

- What the query does
- Why it was generated
- Result explanation

---

## 🛠 AI SQL Repair

Automatically repairs SQL errors like:

- Unknown column
- Unknown table
- SQL syntax errors

Then retries execution automatically.

---

## 🍃 MongoDB Repair

Automatically repairs:

- Invalid operators
- Invalid pipeline
- Mongo syntax errors

---

## 📊 Dashboard Analytics

Monitor:

- Total Queries
- MySQL Queries
- MongoDB Queries
- Success Rate
- Failed Queries
- Average Execution Time
- Provider Usage

---

## 📈 Data Visualization

Generate:

- 📊 Bar Chart
- 📈 Line Chart
- 📉 Area Chart

Automatic numeric column detection.

---

## 📄 Export

Export query results to:

- CSV
- Excel
- PDF Report

---

## 📜 Query History

Automatically stores:

- Question
- Database
- Generated Query
- Timestamp

---

## ⭐ Saved Queries

Save frequently used queries.

---

## 📝 Query Templates

Ready-made templates for:

- Employees
- Customers
- Departments
- Products
- Orders

---

## 💡 Smart Suggestions

One-click AI query suggestions.

---

## 🎨 Themes

- 🌙 Dark
- ☀️ Light
- 💙 Blue

---

# 🏗 Architecture

```text
                     User

                       │

                       ▼

                Streamlit UI

                       │

                       ▼

             Agent Orchestrator

       ┌──────────────┼──────────────┐

       ▼                              ▼

   SQL Agent                    Mongo Agent

       ▼                              ▼

 Optimizer                   Mongo Validator

       ▼                              ▼

 SQL Validator               Mongo Parser

       ▼                              ▼

 Execute SQL                Execute MongoDB

       ▼                              ▼

 SQL Repair              Mongo Repair Agent

       ▼                              ▼

      Explanation Agent

               ▼

         Streamlit Interface
```

---

# 📁 Project Structure

```text
AI-SQL-Agent

│

├── app.py

├── config/

├── logs/

├── src/

│   ├── agents/

│   ├── ai/

│   ├── analytics/

│   ├── database/

│   ├── history/

│   ├── parsers/

│   ├── prompts/

│   ├── saved_queries/

│   ├── suggestions/

│   ├── templates/

│   ├── ui/

│   ├── utils/

│   └── validators/

│

├── requirements.txt

└── README.md
```

---

# ⚙ Technologies

| Category | Technologies |
|-----------|--------------|
| Language | Python |
| UI | Streamlit |
| Database | MySQL, MongoDB |
| AI | Ollama, OpenAI, Anthropic |
| Charts | Streamlit Charts |
| Export | Pandas, OpenPyXL, ReportLab |
| Query Formatting | sqlparse |

---

# 🚀 Installation

Clone repository

```bash
git clone https://github.com/satya66123/AI-SQL-Agent.git
```

Go inside

```bash
cd AI-SQL-Agent
```

Create virtual environment

```bash
python -m venv .venv
```

Activate

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run application

```bash
streamlit run app.py
```

---

# 📸 Screenshots

```
screenshots/

home.png

chat.png

dashboard.png

history.png

pdf_report.png
```

---

# 📊 Current Project Status

| Phase | Progress |
|---------|----------|
| ✅ Phase 1 - Foundation | 100% |
| ✅ Phase 2 - AI Engine | 100% |
| ✅ Phase 3 - Professional Features | 100% |
| 🚀 Phase 4 - Enterprise Features | 95% |

---

# 🎯 Major Features

- ✅ Natural Language to SQL
- ✅ Natural Language to MongoDB
- ✅ SQL Validator
- ✅ Mongo Validator
- ✅ SQL Repair Agent
- ✅ MongoDB Repair Agent
- ✅ Dashboard Analytics
- ✅ Charts
- ✅ PDF Export
- ✅ CSV Export
- ✅ Excel Export
- ✅ Query History
- ✅ Saved Queries
- ✅ Query Templates
- ✅ Smart Suggestions
- ✅ AI Explanation

---

# 🔮 Future Roadmap

- User Authentication
- Multiple Database Connections
- REST API
- Docker Support
- Cloud Deployment
- Voice Commands
- AI Chat Memory
- Query Optimization Insights

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

### Satya Srinath Nekkanti

AI & Software Developer

GitHub: https://github.com/satya66123

---

<p align="center">

### ⭐ If you found this project useful, please consider giving it a Star ⭐

</p>