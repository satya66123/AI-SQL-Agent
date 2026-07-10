<p align="center">

# 🔌 AI SQL Agent API Documentation

### Internal Module API Reference

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

</p>

---

# 📑 Table of Contents

- Overview
- Agent APIs
- AI Provider APIs
- Database APIs
- Validation APIs
- Parser APIs
- Utility APIs
- Analytics APIs
- History APIs
- Saved Query APIs
- UI APIs
- Error Handling

---

# 📖 Overview

AI SQL Agent follows a modular architecture where each component exposes a small, well-defined API. These APIs are internal project modules rather than HTTP REST endpoints.

The application is divided into:

- Agent Layer
- Database Layer
- Validation Layer
- Utility Layer
- UI Layer

Each layer communicates through Python classes and methods.

---

# 🤖 Agent APIs

## AgentOrchestrator

**Location**

```text
src/agents/orchestrator.py
```

### Methods

```python
process(question)

process_sql(question)

process_mongo(question, collection)

execute_mongo_operation(collection, parsed)
```

### Responsibility

- Routes requests
- Executes SQL workflow
- Executes Mongo workflow
- Repairs queries
- Generates explanations

---

## SQLAgent

**Location**

```text
src/agents/sql_agent.py
```

### Methods

```python
generate_sql(question)

process(question)
```

### Responsibility

- Build SQL prompt
- Call AI provider
- Generate SQL

---

## MongoAgent

**Location**

```text
src/agents/mongo_agent.py
```

### Methods

```python
generate_query(question)

process(question)
```

### Responsibility

- Build Mongo prompt
- Generate MongoDB query

---

## OptimizerAgent

```python
optimize(sql)
```

Improves generated SQL before validation.

---

## ExplanationAgent

```python
explain(
    question,
    query,
    rows
)
```

Returns an AI explanation describing:

- Query purpose
- Query logic
- Result summary

---

## RepairAgent

```python
repair(
    sql,
    error
)
```

Repairs invalid SQL using AI.

---

## MongoRepairAgent

```python
repair(
    query,
    error
)
```

Repairs invalid MongoDB queries using AI.

---

# 🧠 AI Provider APIs

## ProviderManager

**Location**

```text
src/ai/provider.py
```

### Methods

```python
set_provider(provider)

get_provider()

set_model(model)

get_model()
```

---

## ModelManager

```python
get_models(provider)
```

Returns available models for the selected AI provider.

---

# 🗄 Database APIs

## QueryService

Responsible for executing database operations.

### SQL

```python
execute_sql(sql)
```

### MongoDB

```python
execute_mongo(collection, query)

execute_mongo_find_one(collection, query)

execute_mongo_aggregate(collection, pipeline)
```

---

## SchemaService

Responsible for schema discovery.

### Methods

```python
get_tables()

describe_table(table)

build_schema()

get_collections()

sample_document(collection)

build_mongo_schema()
```

---

# ✅ Validation APIs

## SQLValidator

```python
validate(sql)
```

Performs:

- SQL validation
- Dangerous statement detection
- Read-only enforcement

---

## MongoValidator

```python
clean(query)

validate(query)
```

Performs:

- Markdown removal
- Dangerous operation detection
- Read-only validation

---

# 📄 Parser APIs

## MongoParser

Responsible for converting Mongo query strings into executable Python objects.

### Methods

```python
parse(query)

parse_find(query)

parse_find_one(query)

parse_aggregate(query)
```

---

# 🛠 Utility APIs

## QueryFormatter

```python
format_sql(sql)

format_mongo(query)
```

Formats generated queries for display.

---

## ExecutionMetrics

```python
start()

stop()

elapsed()
```

Tracks execution duration.

---

## ChartGenerator

```python
show(dataframe)
```

Creates:

- Bar Charts
- Line Charts
- Area Charts

---

## PDFExport

```python
create(
    question,
    database,
    query,
    explanation,
    rows,
    execution_time
)
```

Generates downloadable PDF reports.

---

# 📊 Analytics APIs

## Analytics

```python
add(
    database,
    provider,
    execution_time,
    success
)

get()
```

Tracks:

- Query count
- Success rate
- Execution time
- Provider usage

---

# 📜 History APIs

## QueryHistory

```python
add(
    question,
    database,
    query
)

get()

clear()
```

Stores executed queries.

---

# ⭐ Saved Queries API

## SavedQueries

```python
save(
    question,
    database,
    query
)

get()

clear()
```

Stores bookmarked queries.

---

# 🖥 UI APIs

The UI layer contains independent pages.

```text
Home

AI Chat

AI Provider

Database

Schema Explorer

Logs

Settings

About
```

Each page exposes one entry function:

```python
show_home()

show_ai_chat()

show_provider()

show_database()

show_schema()

show_logs()

show_settings()

show_about()
```

---

# ⚠ Error Handling

Every module follows a common response structure.

## Success

```python
{
    "success": True,
    "result": ...
}
```

## Failure

```python
{
    "success": False,
    "error": "Description"
}
```

This consistent format simplifies communication between modules.

---

# 🔄 Internal API Flow

```text
User
 │
 ▼
AI Chat
 │
 ▼
Agent Orchestrator
 │
 ├── SQL Agent
 │
 └── Mongo Agent
 │
 ▼
Validator
 │
 ▼
Database
 │
 ▼
Repair Agent (if needed)
 │
 ▼
Explanation Agent
 │
 ▼
Analytics
 │
 ▼
Charts / Export / History
```

---

# 🚀 Future API Enhancements

Planned additions include:

- REST API
- Authentication API
- Multi-Database API
- Plugin API
- Webhook Support
- Cloud Deployment API
- Docker Integration
- Streaming AI Responses

---

# 📝 Summary

The AI SQL Agent API is organized into independent, reusable modules following a clean architecture. Each component has a single responsibility, making the project easy to maintain, test, and extend.

This modular design allows new AI providers, databases, validators, and utilities to be integrated with minimal changes to the existing codebase.