## Importing libraries
import os
from dotenv import load_dotenv
load_dotenv()

from crewai_tools import SerperDevTool
from crewai.tools import BaseTool
from langchain_community.document_loaders import PyPDFLoader

search_tool = SerperDevTool()

# PDF Reader Tool
class FinancialDocumentTool(BaseTool):
    name: str = "Financial Document Reader Tool"
    description: str = "Reads and extracts full content from a financial PDF document."

    def _run(self, path: str = "data/sample.pdf") -> str:
        """Reads PDF file and returns cleaned text"""

        try:
            loader = PyPDFLoader(path)
            docs = loader.load()
        except Exception as e:
            return f"Error reading PDF: {str(e)}"

        full_report = ""

        for data in docs:
            content = data.page_content

            # Remove extra newlines
            while "\n\n" in content:
                content = content.replace("\n\n", "\n")

            full_report += content + "\n"

        return full_report


pdf_tool = FinancialDocumentTool()

# Investment Analysis Tool
class InvestmentTool(BaseTool):
    name: str = "Investment Analysis Tool"
    description: str = "Analyzes financial document data for investment insights."

    def _run(self, financial_document_data: str) -> str:

        insights = []
        text = financial_document_data.lower()

        if "revenue" in text:
            insights.append("Revenue growth detected in report.")

        if "net income" in text:
            insights.append("Company profitability discussed.")

        insights.append(
            "Investment Outlook: HOLD — based on available financial signals."
        )

        return "\n".join(insights)


investment_tool = InvestmentTool()

# Risk Assessment Tool
class RiskTool(BaseTool):
    name: str = "Risk Assessment Tool"
    description: str = "Creates a risk assessment based on financial document data."

    def _run(self, financial_document_data: str) -> str:

        risks = []
        text = financial_document_data.lower()

        if "debt" in text:
            risks.append("Potential leverage risk detected.")

        if "loss" in text:
            risks.append("Profitability risk observed.")

        risks.append("Macroeconomic and market volatility risks present.")

        return "\n".join(risks)


risk_tool = RiskTool()