# ScoutAgentAI: Daily Top 5 Stock Report
This project deploys an AI Agent built in Python using AWS Lambda. The agent runs every morning at 8 AM via Amazon EventBridge, analyzes the top 5 stocks based on market sentiment, and generates an HTML report stored in an S3 bucket. The report is hosted via a custom domain using Amazon CloudFront and Route 53.

# Architecture Overview


![ScoutAgent Architecture](https://github.com/user-attachments/assets/f63b6abb-e23d-41d9-ae18-785e591fdbf6)


# Components

**AWS Lambda**: Hosts the Python AI agent.

**Amazon EventBridge**: Triggers the Lambda function daily at 8 AM.

**Python AI Agent**: Analyzes market sentiment and generates an HTML report of top 5 stocks.

**Amazon S3**: Stores the generated HTML report.

**Amazon CloudFront**: Distributes the static HTML page globally.

**Amazon Route 53**: Hosts the custom domain for web access.


## 🚀 Features

- 🔧 **phi.agent** for conversational AI
- 🦙 **Groq Llama** model (e.g., `llama-3.3-70b-versatile`) for fast LLM performance
- 🌐 **DuckDuckGo** web search integration
- 📈 **YFinanceTools** to fetch stock price, fundamentals, analyst recommendations, company info, and news  
- ✅ Markdown output with organized tables and source citations

---
# Output

![sample_output](https://github.com/user-attachments/assets/28c6b172-8d27-4043-8cfc-4628a7006c5f)

## 📦 Requirements

Install the required libraries:
```bash
pip install phidata groq duckduckgo-search yfinance markdown2 python-dotenv




