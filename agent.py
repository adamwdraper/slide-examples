# uv add slide-tyler slide-lye

# Optional: If you're using a .env file for API keys, uncomment these lines
from dotenv import load_dotenv
load_dotenv()

import asyncio
import os
from tyler import Agent, Thread, Message
from narrator import ThreadStore, FileStore
from lye import WEB_TOOLS, IMAGE_TOOLS, FILES_TOOLS

import weave
weave.init("wandb-designers/slide-examples")

async def main():
    thread_store = await ThreadStore.create(os.environ.get('NARRATOR_DATABASE_URL'))
    
    file_store = await FileStore.create(base_path="./attachments")

    # Create your agent
    agent = Agent(
        name="research-assistant",
        model_name="o3",
        purpose="To help with research and analysis tasks",
        tools=[
            *WEB_TOOLS,      # Can search and fetch web content
            *IMAGE_TOOLS,    # Can analyze and describe images
        ],
        thread_store=thread_store,
        file_store=file_store
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