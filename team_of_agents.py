
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

load_dotenv()

web_agent = Agent(
    name="Web Agent",
    model=Groq(id='llama-3.3-70b-versatile'),
    tools=[DuckDuckGo()],
    instructions=["Include all the sources"],
    show_tool_calls=True,
    markdown=True,
)


finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=Groq(id='llama-3.3-70b-versatile'),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    show_tool_calls=True,
    markdown=True,
    instructions=["Use tables to display data."]
)

agent = Agent(
    team=[web_agent, finance_agent],
    model=Groq(id='llama-3.3-70b-versatile'),
    instructions=["Include all the sources", "Use tables to display data."],
    show_tool_calls=True,
    markdown=True,
)

agent.print_response("Compare and summarize the analyst recommendations and share the latest for NVDA", stream=True)
