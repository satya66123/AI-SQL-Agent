<p align="center">

# 💼 AI SQL Agent - Frequently Asked Interview Questions

### Project-Based Interview Preparation

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)
![Interview](https://img.shields.io/badge/Interview-Preparation-success?style=for-the-badge)

</p>

---

# 📖 Overview

This document contains commonly asked interview questions related to the **AI SQL Agent** project. These questions cover project architecture, Python, AI integration, SQL, MongoDB, and system design.

---

# 🤖 Project Questions

### 1. What is AI SQL Agent?

An AI-powered application that converts natural language into executable SQL and MongoDB queries using Large Language Models (LLMs).

---

### 2. Why did you build this project?

To simplify database interactions, reduce manual query writing, and demonstrate AI integration with modern databases.

---

### 3. Which technologies did you use?

- Python
- Streamlit
- MySQL
- MongoDB
- Ollama
- OpenAI
- Anthropic
- Pandas
- SQLParse
- ReportLab
- OpenPyXL

---

### 4. Explain the project architecture.

The project follows a modular layered architecture consisting of:
- UI Layer
- Agent Layer
- Validation Layer
- Database Layer
- Utility Layer

---

### 5. What is the role of the Agent Orchestrator?

It coordinates the complete workflow by routing requests, validating queries, executing them, repairing errors, and generating AI explanations.

---

# 🐍 Python Questions

### 6. Why did you choose Python?

Because of its rich AI ecosystem, excellent database libraries, and rapid development capabilities.

### 7. What OOP concepts are used?

- Classes
- Objects
- Inheritance
- Encapsulation
- Polymorphism

### 8. Why did you use a modular project structure?

To improve maintainability, scalability, and code reusability.

---

# 🗄 SQL Questions

### 9. How do you validate SQL queries?

Using a custom SQL Validator that blocks unsafe operations and validates generated SQL before execution.

### 10. What is the SQL Repair Agent?

It uses AI to automatically fix common SQL errors and retries the query.

---

# 🍃 MongoDB Questions

### 11. How do you execute MongoDB queries?

Generated queries are validated, parsed into Python objects, and executed using PyMongo.

### 12. Why is a Mongo Parser required?

Because AI returns queries as strings, which must be converted into executable Python dictionaries or pipelines.

---

# 🤖 AI Questions

### 13. Which AI providers are supported?

- Ollama
- OpenAI
- Anthropic

### 14. Why support multiple AI providers?

To provide flexibility, reduce vendor dependency, and allow users to choose between local and cloud-based models.

### 15. What is Prompt Engineering?

The process of designing effective prompts to guide AI models toward accurate and reliable outputs.

---

# 📊 Feature Questions

### 16. What is Query History?

It stores previously executed queries along with timestamps and database information.

### 17. What are Saved Queries?

Frequently used queries that users can access later.

### 18. Why did you add Dashboard Analytics?

To monitor query execution, provider usage, execution time, and overall application performance.

### 19. What export formats are supported?

- CSV
- Excel
- PDF

### 20. What charts are supported?

- Bar Chart
- Line Chart
- Area Chart

---

# 🏗 System Design Questions

### 21. Why use layered architecture?

It separates responsibilities, making the application easier to maintain and extend.

### 22. How can this project scale?

By adding new databases, AI providers, REST APIs, Docker support, and cloud deployment without major architectural changes.

---

# 💡 Best Interview Tip

When explaining this project:

- Start with the problem statement.
- Explain the architecture.
- Walk through the query execution flow.
- Highlight AI integration.
- Discuss challenges and how you solved them.
- Mention future enhancements.

---

# 🎯 Conclusion

AI SQL Agent demonstrates practical knowledge of **Python, AI integration, SQL, MongoDB, Streamlit, software architecture, and system design**. It is an excellent portfolio project and provides strong discussion points during technical interviews.