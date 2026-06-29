from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langgraph.prebuilt import create_react_agent as _create_agent
from tools import tools

# Defined at module level — accessible everywhere
SYSTEM_PROMPT = """You are a helpful, honest and concise AI assistant.
You have access to tools for web search, Wikipedia, date/time, and calculations.

IMPORTANT RULES:
- For any science, history, geography, or factual question — ALWAYS use Wikipedia or web search tool first
- Never answer factual questions from memory alone
- Only use your own knowledge for casual conversation or simple definitions
- If unsure, search first, then answer

Give clear, direct answers based on tool results."""


def build_agent():
    llm = ChatOllama(
        model="llama3.2",
        temperature=0.3,
    )
    agent = _create_agent(
        model=llm,
        tools=tools,
        prompt=SYSTEM_PROMPT
    )
    return agent


def chat(agent, user_input, history):
    messages = [SystemMessage(content=SYSTEM_PROMPT)]

    for human, ai in history:
        messages.append(HumanMessage(content=human))
        messages.append(AIMessage(content=ai))

    messages.append(HumanMessage(content=user_input))

    response = agent.invoke({"messages": messages})
    return response["messages"][-1].content


