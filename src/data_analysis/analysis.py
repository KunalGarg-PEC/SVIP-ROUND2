import pandas as pd
import numpy as np
from azure.ai.openai import OpenAIClient
from azure.identity import DefaultAzureCredential

# Initialize Azure OpenAI Client
client = OpenAIClient(credential=DefaultAzureCredential())

def analyze_customer_data(customer_data):
    """
    Analyzes customer financial data and generates insights.
    """
    # Sample analysis: Calculate summary statistics
    summary_stats = customer_data.describe()
    
    # Example: Generating a simple analysis report using OpenAI
    response = client.text_completion(
        engine="gpt-4",
        prompt=f"Analyze the following financial data and provide key insights: {summary_stats}",
        max_tokens=500
    )
    
    return summary_stats, response.choices[0].text

def get_market_trends(market_data):
    """
    Analyzes market trends and generates insights.
    """
    # Sample analysis: Calculate moving average
    market_data['Moving_Average'] = market_data['Price'].rolling(window=7).mean()
    
    # Example: Generating a market trend report using OpenAI
    response = client.text_completion(
        engine="gpt-4",
        prompt=f"Analyze the following market data and provide key insights: {market_data.tail(30)}",
        max_tokens=500
    )
    
    return market_data, response.choices[0].text

# Sample data
customer_data = pd.DataFrame({
    'Age': [25, 45, 35, 50, 23],
    'Income': [50000, 100000, 75000, 120000, 45000],
    'Investments': [20000, 50000, 30000, 70000, 15000]
})

market_data = pd.DataFrame({
    'Date': pd.date_range(start='1/1/2021', periods=100),
    'Price': np.random.rand(100) * 100
})

# Running the analysis functions
customer_summary, customer_insights = analyze_customer_data(customer_data)
market_trends, market_insights = get_market_trends(market_data)

print("Customer Summary:\n", customer_summary)
print("Customer Insights:\n", customer_insights)
print("Market Trends:\n", market_trends)
print("Market Insights:\n", market_insights)