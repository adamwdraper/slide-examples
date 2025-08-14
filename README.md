# Slide Examples

This repository contains example implementations using Slide's AI agent frameworks: **Tyler**, **Lye**, and **Narrator**.

## Overview

These examples demonstrate how to build AI agents using Slide's ecosystem:

- **[Tyler](https://github.com/slide-agi/tyler)** - The core agent framework for building conversational AI assistants
- **[Lye](https://github.com/slide-agi/lye)** - Tool library providing web search, file operations, image processing, and more
- **[Narrator](https://github.com/slide-agi/narrator)** - Persistence layer for managing conversation threads and file storage

## Examples

### 1. Basic Agent (`agent.py`)
A complete example showing:
- Thread-based conversation management
- Tool integration (web, image, and file tools)
- Persistent storage with Narrator
- Weave tracking for observability

```bash
python agent.py
```

### 2. Streaming Agent (`agent_streaming.py`)
Demonstrates real-time streaming responses:
- Event-based streaming output
- Token-by-token response handling
- Simplified setup without tools

```bash
python agent_streaming.py
```

### 3. Wandb Inference Examples
Examples configured to use Weights & Biases infrastructure:
- `agent_wandb_inference.py` - Basic agent with Wandb API
- `agent_streaming_wandb_inference.py` - Streaming agent with Wandb API

These examples use your `WANDB_API_KEY` as the OpenAI API key for seamless integration with W&B's proxy.

### 4. Tyler Chat CLI Configuration
The `tyler-chat-config.yaml` file shows how to configure the Tyler CLI chat interface with:
- Custom agent identity and purpose
- Model parameters
- Tool selection and configuration

## Installation

This project uses `uv` for Python package management:

```bash
# Clone the repository
git clone https://github.com/adamwdraper/slide-examples.git
cd slide-examples

# Install dependencies with uv
uv sync
```

## Environment Setup

Create a `.env` file with your API keys:

```bash
# For OpenAI
OPENAI_API_KEY=your_openai_api_key

# For Wandb examples (optional)
WANDB_API_KEY=your_wandb_api_key

# For Narrator persistence (optional)
NARRATOR_DATABASE_URL=your_database_url
```

## Project Structure

```
slide-examples/
├── agent.py                           # Full-featured agent example
├── agent_streaming.py                 # Streaming response example
├── agent_wandb_inference.py           # Wandb-integrated agent
├── agent_streaming_wandb_inference.py # Wandb streaming agent
├── tyler-chat-config.yaml             # Tyler CLI configuration
├── pyproject.toml                     # Project dependencies
└── README.md                          # This file
```

## Key Features Demonstrated

- **Conversation Management**: Thread-based conversations with message history
- **Tool Integration**: Web search, file operations, and image processing capabilities
- **Streaming Responses**: Real-time token streaming for responsive interactions
- **Persistence**: Store conversations and files with Narrator
- **Observability**: Weave integration for tracking and debugging
- **Flexible Configuration**: YAML-based configuration for the Tyler CLI

## Dependencies

- Python 3.12+
- slide-tyler ≥ 1.3.0
- slide-lye ≥ 0.3.0
- slide-narrator ≥ 1.0.1
- python-dotenv (for environment variables)

## Contributing

Feel free to submit issues or pull requests if you have suggestions for improving these examples or adding new ones.

## License

This project is open source and available under the MIT License.

## Related Links

- [Tyler Documentation](https://github.com/slide-agi/tyler)
- [Lye Tools Documentation](https://github.com/slide-agi/lye)
- [Narrator Documentation](https://github.com/slide-agi/narrator)
- [Weights & Biases](https://wandb.ai/)