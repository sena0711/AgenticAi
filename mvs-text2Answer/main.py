import os  # Add this import
from dotenv import load_dotenv
import boto3
from langchain_aws import ChatBedrockConverse
from langchain_aws import ChatBedrock
# Load the .env file
load_dotenv()

# Get the AWS profile from the .env file
aws_profile = os.getenv("AWS_PROFILE")
aws_region = os.getenv("AWS_REGION")

# Create a boto3 session using the profile from .env
session = boto3.Session(profile_name=aws_profile)

# Claude 모델 이름 예시: anthropic.claude-3-sonnet-20240229-v1:0
bedrock_client = boto3.client("bedrock-runtime", region_name=aws_region) 


# Initialize the Claude model
llm = ChatBedrockConverse(
    model="anthropic.claude-3-haiku-20240307-v1:0",  # Change to desired Claude model
    temperature=0,
    client=bedrock_client,
)

# Define LangGraph state
class MyState(dict): pass

# Define the Claude node
def llm_node(state: MyState):
    prompt = state.get("input", "Hi Claude!")
    response = llm.invoke(prompt)  # Properly use `invoke` method
    return {"response": response}

# Build the graph
graph_builder = StateGraph(MyState)
graph_builder.add_node("claude", llm_node)
graph_builder.set_entry_point("claude")
graph_builder.set_finish_point("claude")
graph = graph_builder.compile()

# Invoke the graph
result = graph.invoke({"input": "Claude, AWS와 LangGraph에 대해 알려줘."})

# Print result
print(result["response"])