<p align="center">

# 🎨 AI SQL Agent - System Design

### Design Overview & Architecture

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

</p>

---

# 📖 Overview

AI SQL Agent is designed using a **modular and layered architecture** that separates the user interface, AI processing, database operations, validation, and utility modules. This design makes the application scalable, maintainable, and easy to extend.

---

# 🎯 Design Goals

- Clean and modular architecture
- Separation of concerns
- Easy maintenance
- Multi-AI provider support
- Multiple database support
- Reusable components
- Scalable and extensible design

---

# 🏗 High-Level Design

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
 ├── Optimizer Agent
 ├── Repair Agents
 └── Explanation Agent
 │
 ▼
Validators & Parser
 │
 ▼
Query Service
 │
 ▼
MySQL / MongoDB
```

---

# 📂 Layered Architecture

### Presentation Layer

- Home
- AI Chat
- Dashboard
- Schema Explorer
- Settings
- Logs
- About

### Business Layer

- Agent Orchestrator
- SQL Agent
- Mongo Agent
- Optimizer Agent
- Explanation Agent
- SQL Repair Agent
- Mongo Repair Agent

### Validation Layer

- SQL Validator
- Mongo Validator
- Mongo Parser

### Data Layer

- Query Service
- Schema Service
- MySQL
- MongoDB

---

# 🤖 AI Workflow

```text
User Question
      │
      ▼
AI Provider
      ▼
Generate Query
      ▼
Validate
      ▼
Execute
      ▼
Repair (If Needed)
      ▼
Explain
      ▼
Display Results
```

---

# 🗄 Database Workflow

### MySQL

```
Question → SQL → Validate → Execute → Repair → Result
```

### MongoDB

```
Question → Mongo Query → Validate → Parse → Execute → Repair → Result
```

---

# 🧩 Design Principles

- Modular Design
- Single Responsibility Principle
- Reusable Components
- Loose Coupling
- High Cohesion
- Provider Independence
- Database Independence

---

# 🚀 Future Enhancements

- PostgreSQL Support
- SQLite Support
- Docker Deployment
- REST API
- User Authentication
- Cloud Deployment
- Multi-Database Connections

---

# 📝 Conclusion

The AI SQL Agent architecture is designed to be simple, modular, and extensible. By separating the application into independent layers and reusable components, the system becomes easier to maintain, test, and enhance with new AI providers, databases, and enterprise features.