# Optional: If you're using a .env file for API keys, uncomment these lines
from dotenv import load_dotenv
load_dotenv()

import asyncio
import weave
from tyler import Agent, Thread, Message, EventType

weave.init("wandb-designers/slide-examples")

agent = Agent(
    name="streaming-assistant",
    model_name="gpt-4o",
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