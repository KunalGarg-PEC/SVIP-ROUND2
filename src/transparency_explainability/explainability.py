from azure.ai.openai import OpenAIClient
from azure.identity import DefaultAzureCredential

# Initialize Azure OpenAI Client
client = OpenAIClient(credential=DefaultAzureCredential())

def generate_explainable_advice(advice, customer_profile, market_conditions):
    """
    Provides an explanation for the generated investment advice.
    """
    prompt = (
        f"Customer Profile: {customer_profile}\n"
        f"Market Conditions: {market_conditions}\n"
        f"Investment Advice: {advice}\n"
        "Explain the rationale behind this investment advice in simple terms."
    )
    
    response = client.text_completion(
        engine="gpt-4",
        prompt=prompt,
        max_tokens=500
    )
    
    return response.choices[0].text

# Example data
advice = "Invest 40% in stocks, 30% in bonds, and 30% in mutual funds."
customer_profile = {
    'Age': 30,
    'Income': 85000,
    'Investments': 40000
}
market_conditions = {
    'Date': '2021-03-01',
    'Price': 75
}

# Running the explainability function
explanation = generate_explainable_advice(advice, customer_profile, market_conditions)
print("Explanation:\n", explanation)