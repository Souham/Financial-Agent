from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai

import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key=os.getenv("OPENAI_API_KEY")

## Web Search Agent

web_search_agent=Agent(
    name="Web Search Agent",
    role= "Search the web for information",
    model= Groq(id="llama-3.3-70b-versatile"),
    tools= [DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
    )

## Financial Agent

financial_agent=Agent(
    name="Financial Agent",
    role= "Analyze financial data",
    model= Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    instructions=["Use tables and bullet points for financial data"],
    show_tool_calls=True,
    show_instructions=True,
    markdown=True,
    )

multi_agent= Agent(
    team= [web_search_agent, financial_agent],
    name="Multi-Agent",
    role= "Search the web for information and analyze financial data",
    model= Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo(), YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    instructions=["Always include sources", "Use table to display financial data"],
    show_tool_calls=True,
    show_instructions=True,
    markdown=True,
)

multi_agent.print_response("Summarize the analyst recommendations, and stock fundamentals for Apple Inc. (AAPL).")