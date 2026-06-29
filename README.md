# LLaMA 3 AI Chatbot 

A ReAct-based AI chatbot built using **LLaMA 3.2**, **LangChain**, **LangGraph**, and **Streamlit**. The chatbot intelligently chooses between multiple tools such as **Wikipedia**, **DuckDuckGo Search**, **Calculator**, and **Date & Time** to answer user queries accurately. It runs completely locally using **Ollama** and maintains conversation history throughout the session.

---

## Features

- ReAct-based AI agent using LangGraph
- Local inference with LLaMA 3.2 through Ollama
- Interactive chat interface built with Streamlit
- Automatic tool selection based on user queries
- Wikipedia integration for factual information
- DuckDuckGo Search for current events and recent updates
- Calculator for arithmetic and mathematical expressions
- Current date and time utility
- Session-based conversation history
- Clean and responsive user interface

---

## Tech Stack

- Python
- Streamlit
- LangChain
- LangGraph
- Ollama
- LLaMA 3.2
- DuckDuckGo Search
- Wikipedia API

---

## Project Structure

```text
.
├── app.py                  # Streamlit frontend
├── chatbot_agent.py        # Agent creation and conversation logic
├── tools.py                # Custom tools
├── requirements.txt
└── README.md
```

---

## Architecture

```
User
 │
 ▼
Streamlit UI  (app.py)
 │   session_state: agent, history, is_thinking
 │
 ▼
LangGraph ReAct Agent  (chatbot_agent.py)
 │   Thought → Action → Observation → repeat
 │
 ├──► ChatOllama → Ollama → LLaMA 3.2 (local)
 │
 └──► Tools
       ├── DuckDuckGo search
       ├── Wikipedia
       ├── Date & time
       └── Calculator

Memory: full HumanMessage + AIMessage history on every call
```

### Workflow

1. The user enters a query through the Streamlit interface.
2. The query and previous conversation history are passed to the LangGraph ReAct agent.
3. The LLaMA 3.2 model reasons about the query.
4. If required, the agent invokes one of the available tools:
   - Wikipedia
   - DuckDuckGo Search
   - Calculator
   - Date & Time
5. The selected tool returns the result.
6. The LLM generates the final response using the tool output.
7. The conversation history is updated and displayed in the chat interface.

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repository.git

cd your-repository
```

### 2. Create a virtual environment

**Windows**

```bash
python -m venv venv

venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv

source venv/bin/activate
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

---

## Install Ollama

Download and install Ollama from:

https://ollama.com

Pull the LLaMA 3.2 model:

```bash
ollama pull llama3.2
```

Start the Ollama server:

```bash
ollama serve
```

---

## Run the Application

```bash
streamlit run app.py
```

The application will be available at:

```
http://localhost:8501
```

---

## Available Tools

| Tool | Purpose |
|------|---------|
| Wikipedia | Factual knowledge and general information |
| DuckDuckGo Search | Recent news and live information |
| Calculator | Arithmetic and mathematical expressions |
| Date & Time | Current local date and time |

---

## Example Queries

```
Who is APJ Abdul Kalam?

Explain quantum computing.

What is today's date?

Calculate 23% of 85000.

Latest AI news.

Who won the latest FIFA World Cup?
```

---
