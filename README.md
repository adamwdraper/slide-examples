# AI Agent Examples

This repository contains implementations of a research assistant agent using four different AI agent frameworks:

1. **Pydantic AI** - A framework built on Pydantic for structured agent development
2. **OpenAI Agents Python** - OpenAI's official agent SDK
3. **CrewAI** - A framework for orchestrating role-playing AI agents
4. **AutoGen** - Microsoft's framework for building multi-agent conversational systems

## Installation

This project uses `uv` for package management. All required packages have been installed:

```bash
# Packages installed:
uv add pydantic-ai 'pydantic-ai-slim[openai]' httpx
uv add openai-agents duckduckgo-search
uv add crewai 'crewai[tools]'
uv add pyautogen 'pyautogen[tools]'
```

## Environment Setup

Create a `.env` file with your OpenAI API key:

```bash
OPENAI_API_KEY=your_api_key_here
```

## Running the Agents

Each agent implementation performs the same task: searching for information about the Mars Perseverance rover and creating a summary.

### 1. Pydantic AI Agent
```bash
python agent_pydantic.py
```
Features:
- Structured output using Pydantic models
- Web search using DuckDuckGo API
- Type-safe result handling

### 2. OpenAI Agents
```bash
python agent_openai.py
```
Features:
- Official OpenAI SDK integration
- Async function calling
- Web search tool integration

### 3. CrewAI
```bash
python agent_crewai.py
```
Features:
- Multi-agent collaboration (Researcher + Summarizer)
- Sequential task processing
- Role-based agent design

### 4. AutoGen
```bash
python agent_autogen.py
```
Features:
- Code execution capabilities
- Multi-turn conversations
- Function registration system

## Original Tyler Agent

The original implementation uses the Tyler framework:
```bash
python agent.py
```

## Streaming Example

There's also a streaming example available:
```bash
python agent_streaming.py
```

## Notes

- All agents are configured to use GPT-4o by default
- Web search is implemented using DuckDuckGo for consistency
- Each agent includes Weave tracking for observability
- The agents demonstrate different paradigms for building AI assistants

## Framework Comparison

| Framework | Strengths | Best For |
|-----------|-----------|----------|
| Pydantic AI | Type safety, structured outputs | Applications requiring validated responses |
| OpenAI Agents | Official support, simplicity | Quick prototypes with OpenAI models |
| CrewAI | Multi-agent orchestration | Complex workflows with specialized agents |
| AutoGen | Code execution, conversation flows | Interactive coding assistants |
