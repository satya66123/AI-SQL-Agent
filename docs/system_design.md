<p align="center">

# 🏛️ AI SQL Agent - System Design

### High-Level System Design Document

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)
![Architecture](https://img.shields.io/badge/Architecture-Modular-success?style=for-the-badge)

</p>

---

# 📖 Overview

AI SQL Agent is a modular AI-powered application that converts natural language into executable **MySQL** and **MongoDB** queries. The system integrates multiple AI providers, validates generated queries, executes them safely, repairs errors automatically, and displays results with analytics and visualizations.

---

# 🎯 System Objectives

- Convert natural language into SQL and MongoDB queries.
- Support multiple AI providers.
- Validate queries before execution.
- Automatically repair invalid queries.
- Execute queries safely.
- Display results with explanations and charts.
- Export reports in multiple formats.

---

# 🏗️ High-Level System Design

```text
                  User
                    │
                    ▼
             Streamlit UI
                    │
                    ▼
          Agent Orchestrator
        ┌──────────┴──────────┐
        ▼                     ▼
   SQL Agent            Mongo Agent
        │                     │
        ▼                     ▼
 SQL Validator       Mongo Validator
        │                     │
        ▼                     ▼
 Query Service       Mongo Parser
        │                     │
        ▼                     ▼
 MySQL Database      MongoDB Database
        │                     │
        └──────────┬──────────┘
                   ▼
         Explanation Agent
                   │
                   ▼
      Dashboard & Export Modules
```

---

# 🧩 System Components

## 🖥️ Presentation Layer

Handles all user interactions.

- Home
- AI Chat
- Database
- Schema Explorer
- Dashboard
- Logs
- Settings
- About

---

## 🤖 AI Layer

Responsible for AI processing.

Components:

- SQL Agent
- Mongo Agent
- Explanation Agent
- SQL Repair Agent
- Mongo Repair Agent
- Optimizer Agent

---

## ⚙️ Business Layer

Managed by the **Agent Orchestrator**, which:

- Routes requests
- Calls AI providers
- Validates queries
- Executes queries
- Repairs errors
- Generates explanations

---

## 🛡️ Validation Layer

Ensures safe execution.

Components:

- SQL Validator
- Mongo Validator
- Mongo Parser

---

## 🗄️ Data Layer

Communicates with databases.

- Query Service
- Schema Service
- MySQL
- MongoDB

---

# 🔄 System Workflow

```text
User Question
      │
      ▼
AI Provider
      ▼
Generate Query
      ▼
Validate Query
      ▼
Execute Query
      ▼
Repair if Required
      ▼
Generate Explanation
      ▼
Display Results
      ▼
Analytics & Export
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
│   ├── saved_queries/
│   ├── suggestions/
│   ├── templates/
│   ├── ui/
│   ├── utils/
│   └── validators/
└── docs/
```

---

# 📊 Key Features

- AI-powered SQL Generation
- AI-powered MongoDB Query Generation
- Multi-AI Provider Support
- SQL & Mongo Validation
- Automatic Query Repair
- AI Query Explanation
- Dashboard Analytics
- Execution Metrics
- Data Visualization
- CSV, Excel & PDF Export
- Query History
- Saved Queries
- Smart Suggestions

---

# 🔐 Security

The application allows only **read-only operations**.

Blocked SQL operations:

- DROP
- DELETE
- UPDATE
- INSERT
- ALTER
- TRUNCATE

Blocked MongoDB operations:

- deleteOne()
- deleteMany()
- updateOne()
- updateMany()
- insertOne()
- insertMany()
- drop()

This ensures database safety during AI-generated query execution.

---

# 📈 Scalability

The modular architecture allows future integration of:

- PostgreSQL
- SQLite
- Oracle Database
- SQL Server
- Docker
- REST API
- User Authentication
- Cloud Deployment
- Additional AI Providers

---

# 📝 Conclusion

AI SQL Agent follows a clean, modular system design that separates user interface, AI processing, validation, and database operations. This architecture improves maintainability, scalability, and extensibility while providing a secure and efficient AI-powered database querying experience.

---

<p align="center">

### 🚀 AI SQL Agent v1.0 — Modular • Scalable • Intelligent

</p>