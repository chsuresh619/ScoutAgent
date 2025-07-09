from phi.agent import Agent
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.agent import RunResponse
from phi.model.groq import Groq
import markdown2
from datetime import datetime
import os
import boto3


def envsetup():
    api_key = os.getenv('GROQ_API_KEY')


def create_agent():
    agent = Agent(
        name="Top 5 Trending S&P 500 Stocks Analyzer",
        role="Analyze and rank top 5 S&P 500 stocks based on real-time market sentiment with detailed justifications.",
        model=Groq(id="llama3-8b-8192"),
        tools=[DuckDuckGo(), YFinanceTools(company_news=True)],
        instructions=[
            "Identify the top 5 trending S&P 500 stocks for today based on market sentiment.",
            "For each stock, assign a sentiment rating from 1 (very negative) to 10 (very positive).",
            "Provide detailed justifications for each rating, including references to specific news articles or data points.",
            "Ensure all data is up-to-date and relevant to the current trading day."
        ],
        show_tool_calls=True,
        markdown=True,
    )
    return agent


def response():
    agent = create_agent()
    response: RunResponse = agent.run("What are the top 5 trending S&P 500 stocks today based on market sentiment?", stream=False)
    md = response.content
    html_body = markdown2.markdown(md)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Convert the response to HTML format
    html_content = f"""
            <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Scout Agent</title>
  <link rel="stylesheet" href="https://unpkg.com/mvp.css">
  <style>
    body {{ max-width: 800px; margin: 2rem auto; }}
    header, footer {{ text-align: center; margin: 1.5rem 0; }}
    pre.query {{ background: #f4f4f4; padding: 1rem; border-radius: 5px; overflow-x: auto; }}
    .content {{ margin-top: 1rem; }}
  </style>
</head>
<body>
  <header><h1>🌐 Scout Agent</h1></header>
  <section>
    <h2>📝 Daily Top 5 Trending Stocks</h2>
  </section>
  <section>
    <article class="content">
      {html_body}
    </article>
  </section>
  <footer>
    <small>Generated on {now}</small>
  </footer>
</body>
</html>
            """

    # Save the HTML content to a file
    file_path = "/tmp/index.html"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_content)



def lambda_handler(event, context):
    envsetup()
    response()
    s3 = boto3.client('s3')
    s3.upload_file(
        Filename="/tmp/index.html",
        Bucket="bucket_name",
        Key="index.html"
    )
    return {
        'statusCode': 200,
        'body': 'HTML page uploaded to S3.'
    }