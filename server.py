"""
AI for Skeptics - Flask Server
------------------------------
This file serves as the backend for the "AI for Skeptics" course platform.
It handles web routing using Flask and powers an intelligent AI assistant 
using LangChain, LangGraph, and Google Gemini.

To run this application:
1. Ensure all dependencies are installed: pip install -r requirements.txt
2. Create a .env file with GEMINI_API_KEY and TAVILY_API_KEY.
3. Run the server: python server.py
4. Access the site at http://localhost:8080
"""

import os
import json
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

# --- Environment Setup and API Key Loading ---
# Load variables from .env file into the environment
load_dotenv()

# Retrieve API keys for Gemini (LLM) and Tavily (Web Search)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

# --- LangChain and LangGraph Imports ---
# These libraries provide the framework for building the AI agents and orchestration logic
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.tools import tool
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.prebuilt import create_react_agent
from typing import Dict, Any
from tavily import TavilyClient

# Set API keys as environment variables for LangChain integrations to use internally
os.environ['GOOGLE_API_KEY'] = GEMINI_API_KEY
os.environ['TAVILY_API_KEY'] = TAVILY_API_KEY

# --- LLM and Search Client Initialization ---
# Initialize the Gemini 2.0 Flash model via Google GenAI
llm = init_chat_model(model='google_genai:gemini-2.5-flash')

# Initialize the Tavily client for performing real-time web searches
tavily_client = TavilyClient(api_key=TAVILY_API_KEY)

# --- Custom Tool Definitions ---
# These tools allow agents to perform specific actions like searching the web or calling other agents

@tool
def web_search(query: str) -> Dict[str, Any]:
    """
    Search the web for information using Tavily.
    Returns a dictionary containing search results, snippets, and URLs.
    """
    return tavily_client.search(query)

@tool
def source_finder(claim: str) -> str:
    """
    Finds trustworthy and verifiable sources for a specific claim.
    Uses the WebsiteAgent to filter out unreliable sources like blogs or Wikipedia.
    Returns a formatted string containing titles, URLs, and publishers.
    """
    response = WebsiteAgent.invoke(
        {"messages": [HumanMessage(content=claim)]}
    )
    return response["messages"][-1].content

@tool
def concept_tutor(topic: str) -> str:
    """
    Acts as an AI tutor to explain AI concepts thoroughly but simply.
    Uses the AIAgent to provide accurate and unbiased explanations.
    Returns a detailed explanation of the requested topic.
    """
    response = AIAgent.invoke(
        {"messages": [HumanMessage(content=topic)]}
    )
    return response["messages"][-1].content

# --- Agent Definitions ---
# Agents are specialized LLM configurations with specific roles, prompts, and tools.

# AIAgent: A specialized tutor for AI concepts, ethics, and technical workings.
# It uses an InMemorySaver for thread-based memory.
AIAgent = create_react_agent(
    model=llm,
    tools=[], # Operates based on its internal knowledge base
    prompt="You are a tutor at an accredited ivy league school in America. You are tasked with helping faculty with learning about AI, both in terms of the ethics of AI and the actual workings of it. Whenever you are asked a question, you make sure to give as comprehensive an answer as possible without getting bogged down in technical language or giving overly bloated answers. You are certainly a fan of AI, as in you can see its benefits. But you are also very aware of all the issues present with AI, and thus always give accurate, unbiased answers about AI.",
    checkpointer=InMemorySaver()
)

# WebsiteAgent: A research specialist focused on finding and verifying high-quality sources.
# It has access to the web_search tool.
WebsiteAgent = create_react_agent(
    model=llm,
    tools=[web_search],
    prompt="You are a systems AI designed to find verifiable and trustworthy sources for any claim. If you believe a claim is not supported very well, you will still attempt to find sources for it, but will make clear that you believe it is not well supported or that it is a controversial topic.",
    checkpointer=InMemorySaver()
)

# --- Configuration Setup ---
# Thread ID '1' is used to maintain a consistent conversation state across agent calls.
config = {"configurable": {"thread_id": "1"}}

# --- Orchestrator Tool Definitions ---
# These tools wrap the specialized agents so they can be called by the main orchestration agent.

@tool
def call_AIAgent(topic: str, content: str) -> str:
    """
    Wrapper to call the AIAgent for explaining concepts or generating quizzes.
    Returns the agent's detailed response.
    """
    response = AIAgent.invoke(
        {"messages": [HumanMessage(content=f"{topic}: {content}")]},
        config
    )
    return response["messages"][-1].content

@tool
def call_WebsiteAgent(query: str) -> str:
    """
    Wrapper to call the WebsiteAgent for finding verifiable sources for a query.
    Returns the agent's research findings.
    """
    response = WebsiteAgent.invoke(
        {"messages": [HumanMessage(content=query)]},
        config
    )
    return response["messages"][-1].content

# --- Orchestration Agent ---
# The master agent that coordinates the workflow: first explaining a concept, then finding sources.
orchestration_agent = create_react_agent(
    model=llm,
    tools=[call_AIAgent, call_WebsiteAgent],
    prompt="You are an AI assistant for the AI for Skeptics course at William & Mary's Raymond A. Mason School of Business. For EVERY message you receive you must ALWAYS follow these two steps in order: Step 1 — call call_AIAgent to explain the concept or answer the question. Step 2 — call call_WebsiteAgent to find supporting sources for your response. You must always complete both steps before giving a final answer. Never answer directly from your own knowledge without calling both tools first."
)

# --- Flask Application Setup ---
app = Flask(__name__, static_folder='.', static_url_path='')

# --- Flask Routes: Page Navigation ---

@app.route('/')
def index():
    """Serves the Home Page (Landing Page)."""
    return render_template('index.html')

@app.route('/course')
def course():
    """Serves the Course Overview Page."""
    return render_template('course.html')

@app.route('/module/1')
def module1():
    """Serves Learning Module 1: Introduction to AI."""
    return render_template('module1.html')

@app.route('/module/2')
def module2():
    """Serves Learning Module 2: AI in Business."""
    return render_template('module2.html')

@app.route('/module/3')
def module3():
    """Serves Learning Module 3: AI Ethics and Risks."""
    return render_template('module3.html')

@app.route('/module/4')
def module4():
    """Serves Learning Module 4: The Future of AI."""
    return render_template('module4.html')

@app.route('/about')
def about():
    """Serves the About Us Page."""
    return render_template('about.html')

@app.route('/feedback')
def feedback():
    """Serves the Student Feedback Page."""
    return render_template('feedback.html')

@app.route('/assistant')
def assistant():
    """Serves the AI Assistant Chat Interface Page."""
    return render_template('assistant.html')

# --- Flask Route: Chat Functionality ---

@app.route('/chat', methods=['POST'])
def chat():
    """
    Handles incoming chat messages from the user.
    Receives JSON containing a 'message', processes it through the orchestration agent,
    and returns a JSON response containing the AI's answer and sources.
    """
    data = request.json
    message = data.get('message', '')
    if not message:
        return jsonify({'error': 'No message provided'}), 400
    
    # Invoke the orchestration agent with the user's message
    response = orchestration_agent.invoke({
        "messages": [HumanMessage(content=message)]
    })
    
    # Extract the text content from the agent's final response message
    last_message = response['messages'][-1]
    response_text = last_message.content
    
    # Helper logic to handle complex response formats (e.g., list of blocks vs simple string)
    if not isinstance(response_text, str):
        text_parts = []
        for part in response_text:
            if isinstance(part, dict) and 'text' in part:
                text_parts.append(part['text'])
            elif isinstance(part, str):
                text_parts.append(part)
        response_text = "".join(text_parts)

    return jsonify({'response': response_text})

# --- Server Entry Point ---
if __name__ == '__main__':
    # Get port from environment (standard for Cloud Run) or default to 8080
    port = int(os.environ.get("PORT", 8080))
    # Run the Flask app on all available interfaces (0.0.0.0)
    app.run(host='0.0.0.0', port=port)
