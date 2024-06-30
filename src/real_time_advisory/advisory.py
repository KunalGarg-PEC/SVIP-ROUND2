import pandas as pd
from azure.ai.openai import OpenAIClient
from azure.identity import DefaultAzureCredential

# Initialize Azure OpenAI Client
client = OpenAIClient(credential=DefaultAzureCredential())

def generate_investment_strategy(customer_profile, market_conditions):
    """
    Generates a personalized investment strategy based on customer profile and market conditions.
    """
    prompt = (
        f"Customer Profile: {customer_profile}\n"
        f"Market Conditions: {market_conditions}\n"
        "Generate a tailored investment strategy for this customer."
    )
    
    response = client.text_completion(
        engine="gpt-4",
        prompt=prompt,
        max_tokens=500
    )
    
    return response.choices[0].text

def provide_real_time_advisory(customer_profile, market_data):
    """
    Provides real-time financial advisory by analyzing current market data and customer profile.
    """
    # Example customer profile and market conditions
    customer_profile_summary = customer_profile.describe()
    current_market_conditions = market_data.tail(1).to_dict(orient='records')[0]
    
    # Generate investment strategy
    strategy = generate_investment_strategy(customer_profile_summary, current_market_conditions)
    
    return strategy

# Sample data
customer_profile = pd.DataFrame({
    'Age': [30],
    'Income': [85000],
    'Investments': [40000]
})

market_data = pd.DataFrame({
    'Date': pd.date_range(start='1/1/2021', periods=100),
    'Price': [i for i in range(100)]
})

# Running the advisory function
real_time_advice = provide_real_time_advisory(customer_profile, market_data)
print("Real-Time Advisory:\n", real_time_advice)