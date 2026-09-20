# BrainDump.exe

BrainDump.exe is a lightweight startup idea generator built with Streamlit and local LLM tooling. It turns a rough concept into a clearer product plan by simulating a small team of AI agents: one for planning, one for coding, one for testing, and one for review.

Think of it as a brainstorming partner for builders who want faster structure, sharper thinking, and a more actionable next step.

## What it does

- Takes a startup idea or app concept as input
- Breaks it into features, architecture, and implementation phases
- Drafts developer-ready Python code from the plan
- Reviews the code for bugs, edge cases, and improvements
- Presents everything in a clean, approachable UI

## Tech stack

- Python
- Streamlit
- LangChain Community
- Ollama
- Local LLM inference

## How it works

The app runs several prompt-based agents in sequence:

1. Planner Agent: transforms the idea into a structured roadmap
2. Developer Agent: writes code based on that roadmap
3. Tester Agent: looks for flaws and edge cases
4. Reviewer Agent: refines quality and best practices

## Run locally

1. Create and activate a virtual environment
2. Install dependencies
3. Start Ollama and ensure your model is available
4. Run the app

```bash
python -m venv venv
source venv/bin/activate
pip install streamlit langchain langchain-community ollama
streamlit run agent.py
```

If you are using Ollama locally, make sure the model is available, for example:

```bash
ollama pull llama3
```

## Project structure

```text
.
├── agent.py
├── .gitignore
├── README.md
└── venv/
```

## Notes

This project is designed for experimentation and rapid idea prototyping. It is useful for founders, builders, and students who want to quickly transform an idea into a more structured concept without starting from scratch.

