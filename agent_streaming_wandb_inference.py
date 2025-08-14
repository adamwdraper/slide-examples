# Optional: If you're using a .env file for API keys, uncomment these lines
from dotenv import load_dotenv
load_dotenv()

import os
import asyncio
import weave
from tyler import Agent, Thread, Message, EventType

weave.init("wandb-designers/slide-examples")

# Set the OpenAI API key to the WANDB_API_KEY
os.environ["OPENAI_API_KEY"] = os.environ.get("WANDB_API_KEY")

agent = Agent(
    name="streaming-assistant",
    base_url="https://api.inference.wandb.ai/v1",
    model_name="openai/openai/gpt-oss-120b",  # Use openai/ prefix
    extra_headers={
        "OpenAI-Project": "wandb-designers/slide-examples"  # Required by wandb
    },
    purpose="To provide real-time responses"
)

async def stream_response():
    thread = Thread()
    message = Message(role="user", content="Tell me a story about space exploration")
    thread.add_message(message)
    
    print("🤖 Assistant: ", end="", flush=True)
    
    async for event in agent.go(thread, stream=True):
        if event.type == EventType.LLM_STREAM_CHUNK:
            print(event.data.get("content_chunk", ""), end="", flush=True)
    
    print()  # New line at the end

asyncio.run(stream_response())