from phi.agent import Agent
import phi.api
from phi.model.openai import OpenAIChat
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
import openai

import os
import phi
from phi.playground import Playground, serve_playground_app
#Load environment variables from .env file
load_dotenv()

phi.api=os.getenv("phi-ZB-7FGtg1FZQOFIci2R3tg43F3NaALgLm8LTEqHTA4g")

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

app=Playground(agents=[web_search_agent, financial_agent]).get_app

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)