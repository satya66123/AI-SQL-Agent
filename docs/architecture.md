<p align="center">

# 🏗 AI SQL Agent Architecture

### System Architecture Documentation

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

</p>

---

# 📖 Overview

AI SQL Agent follows a **modular layered architecture** that separates the user interface, business logic, database operations, and AI providers. Each module has a single responsibility, making the application scalable, maintainable, and easy to extend.

---

# 🏛 High-Level Architecture

```text
                 User
                   │
                   ▼
            Streamlit UI
                   │
                   ▼
         Agent Orchestrator
          │             │
          ▼             ▼
     SQL Agent     Mongo Agent
          │             │
          ▼             ▼
   SQL Validator   Mongo Validator
          │             │
          ▼             ▼
     Query Service (Database)
          │
          ▼
   MySQL / MongoDB
          │
          ▼
 Explanation Agent
          │
          ▼
   Results & Dashboard
```

---

# 📂 Architecture Layers

## 1. Presentation Layer

Responsible for the user interface.

Modules:

- Home
- AI Chat
- AI Provider
- Database
- Schema Explorer
- Logs
- Settings
- About

---

## 2. Business Layer

Handles the application's core logic.

Components:

- Agent Orchestrator
- SQL Agent
- Mongo Agent
- Optimizer Agent
- Explanation Agent
- SQL Repair Agent
- Mongo Repair Agent

---

## 3. Validation Layer

Ensures only safe queries are executed.

Modules:

- SQL Validator
- Mongo Validator
- Mongo Parser

---

## 4. Database Layer

Communicates with the databases.

Components:

- Query Service
- Schema Service
- MySQL
- MongoDB

---

## 5. AI Layer

Responsible for interacting with AI models.

Supported Providers:

- Ollama
- OpenAI
- Anthropic

---

# 🔄 SQL Workflow

```text
User Question
      │
      ▼
SQL Agent
      ▼
Optimizer
      ▼
SQL Validator
      ▼
Execute SQL
      ▼
Repair (If Required)
      ▼
Explanation
      ▼
Results
```

---

# 🍃 MongoDB Workflow

```text
User Question
      │
      ▼
Mongo Agent
      ▼
Mongo Validator
      ▼
Mongo Parser
      ▼
Execute Query
      ▼
Repair (If Required)
      ▼
Explanation
      ▼
Results
```

---

# 📊 Analytics Flow

```text
Execute Query
      │
      ▼
Execution Metrics
      ▼
Analytics
      ▼
Dashboard
      ▼
Charts
```

---

# 📁 Project Structure

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
└── README.md
```

---

# 🎯 Design Principles

The architecture is based on the following principles:

- Modular Design
- Separation of Concerns
- Single Responsibility Principle
- Clean Architecture
- Easy Maintenance
- Reusable Components
- Scalable Design
- AI Provider Independence

---

# 🚀 Future Architecture

The current architecture is designed to support future enhancements such as:

- PostgreSQL
- Oracle Database
- SQLite
- REST API
- Docker
- Cloud Deployment
- User Authentication
- Multiple Database Connections

---

# 📝 Conclusion

AI SQL Agent uses a modular and layered architecture that separates the user interface, AI processing, validation, and database operations. This design makes the application easy to understand, maintain, and extend with additional databases, AI providers, and enterprise features.