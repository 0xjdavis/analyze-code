from langchain_community.llms import Together
import os

llm = Together(
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",
    together_api_key=os.getenv("TOGETHER_API_KEY"),
    temperature=0.1,
    max_tokens=50
)

try:
    response = llm.invoke("Please provide only the capital of France, nothing else.")
    print("Response:", response)
except Exception as e:
    print("Error:", e)
