# Financial Document Analyzer (CrewAI Multi-Agent System)

## Overview

This project is a multi-agent financial document analysis system built using CrewAI and FastAPI.

The system analyzes uploaded financial PDFs and produces:
- Financial performance insights
- Investment recommendations
- Risk assessment

The application uses multiple AI agents collaborating sequentially to simulate a professional financial analysis workflow.

## Architecture

### Agents

**Financial Document Verifier**  
Validates uploaded financial documents.

**Financial Analyst**  
Extracts and analyzes company financial performance.

**Investment Advisor**  
Generates investment recommendations.

**Risk Assessment Expert**  
Identifies financial and market risks.

### Workflow

PDF Upload
↓
Verifier Agent
↓
Financial Analyst
↓
Investment Advisor
↓
Risk Assessment Agent
↓
Final Report

## Bugs Found & Fixes (IMPORTANT SECTION)

**Bug 1 — Only One Task Executed**

Problem:  
Crew executed only analyze_financial_document.

Fix:  
Added full sequential task pipeline:

tasks=[
verify_document,
analyze_financial_document,
investment_analysis,
risk_analysis
]

**Bug 2 — Incorrect CrewAI kickoff format**

Problem:  
Inputs passed as positional dictionary.

Fix:  
crew.kickoff(inputs={...})

**Bug 3 — Tools Not Producing Real Output**

Problem:  
Investment and Risk tools returned placeholder strings.

Fix:  
Implemented keyword-based analysis logic for insights and risk detection.

**Bug 4 — PDF Re-read Multiple Times**

Problem:  
Performance inefficiency.

Fix:  
CrewAI caching enabled automatically.

## Setup Instructions

1. Clone Repository  
git clone <repo-link>
cd Financial-Document-Analyzer

2. Create Virtual Environment  
python -m venv venv
venv\Scripts\activate

3. Install Dependencies  
pip install -r requirements.txt

4. Environment Variables  
Create .env file:  
OPENAI_API_KEY=your_key
SERPER_API_KEY=your_key

5. Run API  
uvicorn main:app --reload

Open: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## API Documentation

**POST /analyze**  
Uploads a financial document for analysis.

**Request**  
file: PDF document  
query (optional): analysis request

**Response**  
{
"status": "success",
"query": "...",
"analysis": "...",
"file_processed": "document.pdf"
}

## Technologies Used

CrewAI  
FastAPI  
LangChain  
Python  
PyPDFLoader

## Future Improvements (Bonus)

Queue-based async processing  
Database storage  
Structured JSON output

**.env.example (Very Important)**  
Create:  
OPENAI_API_KEY=
SERPER_API_KEY=

Never upload real keys.

## Conclusion

The Financial Document Analyzer demonstrates how a multi-agent architecture using CrewAI can simulate a real-world financial analysis workflow through collaborative AI agents. By combining document verification, financial analysis, investment recommendation, and risk assessment into a sequential pipeline, the system produces structured and meaningful insights from financial PDF documents through a simple API interface.

The project emphasizes debugging, system design, and practical AI orchestration by resolving execution issues, improving tool behavior, optimizing document processing, and ensuring stable API functionality. The final implementation provides a working, extensible foundation that can be further enhanced with asynchronous processing, queue-based workers, and database integration for scalability and production readiness.

Overall, this system showcases how agent-based AI systems can be applied to automate complex analytical tasks while maintaining modularity, clarity, and real-world applicability.