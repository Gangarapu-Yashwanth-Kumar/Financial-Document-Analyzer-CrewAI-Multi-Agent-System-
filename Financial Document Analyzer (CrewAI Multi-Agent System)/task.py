## Importing libraries and files
from crewai import Task
from agents import (
    financial_analyst,
    verifier,
    investment_advisor,
    risk_assessor
)

from tools import pdf_tool, search_tool, investment_tool, risk_tool

analyze_financial_document = Task(
    description=(
        "Analyze the financial document located at {path} and answer the user query: {query}.\n"
        "Provide insights about company performance, revenue trends, profitability, "
        "and overall financial health."
    ),

    expected_output=(
        "Provide a structured financial analysis including:\n"
        "- Key financial insights\n"
        "- Revenue and profitability discussion\n"
        "- Market observations\n"
        "- Overall financial summary"
    ),

    agent=financial_analyst,
    tools=[pdf_tool, search_tool, investment_tool, risk_tool],
    async_execution=False,
)

verify_document = Task(
    description=(
        "Verify that the uploaded file located at {path} is readable "
        "and appears to be a financial document."
    ),

    expected_output=(
        "Confirmation stating whether the document is readable and "
        "contains financial information."
    ),

    agent=verifier,
    tools=[pdf_tool],
    async_execution=False,
)

investment_analysis = Task(
    description=(
        "Based on the financial analysis already performed, provide an "
        "investment recommendation for the company."
    ),

    expected_output=(
        "Investment recommendation including BUY, HOLD, or SELL decision "
        "with reasoning based on financial performance."
    ),

    agent=investment_advisor,
    tools=[investment_tool],
    async_execution=False,
)

risk_analysis = Task(
    description=(
        "Identify financial, operational, and market risks associated "
        "with the company using the analyzed financial information."
    ),

    expected_output=(
        "Detailed risk assessment including potential financial and "
        "macroeconomic risks."
    ),

    agent=risk_assessor,
    tools=[risk_tool],
    async_execution=False,
)