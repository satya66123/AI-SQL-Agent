<p align="center">

# 📘 AI SQL Agent Documentation

### Project Documentation

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

</p>

---

# 📖 Overview

AI SQL Agent is an AI-powered database assistant that converts natural language into executable **MySQL** and **MongoDB** queries. It supports multiple AI providers, validates generated queries, executes them safely, and presents results with explanations, analytics, and export options.

---

# ✨ Key Features

- Natural Language to SQL
- Natural Language to MongoDB
- Multi-AI Provider Support
- SQL & MongoDB Validation
- SQL & MongoDB Repair Agents
- AI Query Explanation
- Dashboard Analytics
- Query History & Saved Queries
- Smart Suggestions & Query Templates
- CSV, Excel & PDF Export
- Data Visualization

---

# 🏗 Project Architecture

```text
User
 │
 ▼
Streamlit UI
 │
 ▼
Agent Orchestrator
 │
 ├── SQL Agent
 ├── Mongo Agent
 ├── Validators
 ├── Repair Agents
 └── Explanation Agent
 │
 ▼
Query Service
 │
 ▼
MySQL / MongoDB
```

---

# 📂 Project Structure

```text
AI-SQL-Agent/

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
│   ├── ui/
│   ├── utils/
│   └── validators/
└── README.md
```

---

# ⚙ Technology Stack

| Category | Technology |
|-----------|------------|
| Language | Python |
| UI | Streamlit |
| Databases | MySQL, MongoDB |
| AI Providers | Ollama, OpenAI, Anthropic |
| Data Processing | Pandas |
| Export | OpenPyXL, ReportLab |
| Query Formatting | SQLParse |

---

# 🔄 Application Workflow

```text
User Question
      │
      ▼
Generate Query
      ▼
Validate
      ▼
Execute
      ▼
Repair (If Required)
      ▼
Generate Explanation
      ▼
Display Results
      ▼
Export & Analytics
```

---

# 🚀 Future Enhancements

- PostgreSQL Support
- SQLite Support
- Docker Deployment
- REST API
- User Authentication
- Cloud Deployment
- Multiple Database Connections

---

# 📝 Conclusion

AI SQL Agent is a modular and extensible AI-powered database assistant that simplifies database interactions using natural language. It combines AI, database technologies, analytics, and reporting into a single application, providing an efficient and user-friendly experience for developers, students, and database professionals.