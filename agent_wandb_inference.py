# uv add slide-tyler slide-lye

# Optional: If you're using a .env file for API keys, uncomment these lines
from dotenv import load_dotenv
load_dotenv()

import os
import asyncio
from tyler import Agent, Thread, Message
from lye import WEB_TOOLS, IMAGE_TOOLS, FILES_TOOLS

import weave
weave.init("wandb-designers/slide-examples")

# Set the OpenAI API key to the WANDB_API_KEY
os.environ["OPENAI_API_KEY"] = os.environ.get("WANDB_API_KEY")

async def main():
    # Create your agent
    agent = Agent(
        name="research-assistant",
        base_url="https://api.inference.wandb.ai/v1",
        model_name="openai/openai/gpt-oss-120b",  # Use openai/ prefix
        extra_headers={
            "OpenAI-Project": "wandb-designers/slide-examples"  # Required by wandb
        },
        purpose="To help with research and analysis tasks",
        tools=[
            *WEB_TOOLS,      # Can search and fetch web content
            *IMAGE_TOOLS,    # Can analyze and describe images
        ]
    )

    # Create a conversation thread
    thread = Thread()
    
    # Add your request
    message = Message(
        role="user",
        content="Why should I use https://slide.mintlify.app"
    )
    thread.add_message(message)
    
    # Let the agent work
    print("🤖 Agent is working...")
    result = await agent.go(thread)
    
    # Print the results
    print(f"\n💬 Assistant: {result.content}")

if __name__ == "__main__":
    asyncio.run(main())