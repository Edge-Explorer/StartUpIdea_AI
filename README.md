<div align="center">

# 🚀 StartupIdea AI Validator

### *Because every great startup begins with the right question: "Is this actually a good idea?"*

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)](https://python.org)
[![CrewAI](https://img.shields.io/badge/CrewAI-Multi--Agent-orange?style=for-the-badge)](https://crewai.com)
[![Gemini](https://img.shields.io/badge/Gemini-2.0%20Flash-green?style=for-the-badge&logo=google)](https://deepmind.google/technologies/gemini/)
[![LlamaIndex](https://img.shields.io/badge/LlamaIndex-RAG-purple?style=for-the-badge)](https://www.llamaindex.ai/)
[![uv](https://img.shields.io/badge/uv-Package%20Manager-red?style=for-the-badge)](https://docs.astral.sh/uv/)

**Built by [Karan](https://github.com/Edge-Explorer)**

</div>

---

## 🧠 What Is This?

**StartupIdea AI Validator** is a multi-agent AI system that takes any startup idea as an input and returns a comprehensive, data-driven analysis across five dimensions — powered by **Google Gemini 2.0 Flash** and orchestrated by **CrewAI**.

Instead of guessing whether your idea is good, you now have **five specialized AI agents** working together like a consulting firm to give you the verdict.

### 💡 Example

> **Input:** `"I want to build an AI fitness app for busy professionals"`

> **Output:**
> - 📊 Market demand & TAM (Total Addressable Market)
> - 🏢 Competitor landscape with strengths & weaknesses
> - 💰 Business model & monetization strategy
> - ⚠️ Risks (legal, technical, market)
> - ✅ Final verdict: **GO** or **NO-GO**

---

## 🤖 Agent Architecture

This project uses a **sequential multi-agent pipeline**. Each agent is an expert in its domain and passes its findings to the next.

```
User Idea → [Agent 1] → [Agent 2] → [Agent 3] → [Agent 4] → [Agent 5] → Final Report
```

| # | Agent | Role | Output |
|---|-------|------|--------|
| 1️⃣ | **Market Research Agent** | Analyzes demand, trends, and target audience | Market Analysis Report |
| 2️⃣ | **Competitor Analyst Agent** | Maps the competitive landscape; finds gaps | SWOT-style Competitor Report |
| 3️⃣ | **Business Strategist Agent** | Proposes monetization models and scaling plans | Business Strategy Document |
| 4️⃣ | **Risk Analyst Agent** | Identifies legal, technical, and market risks | Risk Assessment Report |
| 5️⃣ | **Final Decision Agent** | Synthesizes all reports into one final verdict | ✅ GO / ❌ NO-GO Verdict |

---

## 🏗️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **CrewAI** | Multi-agent orchestration |
| **Google Gemini 2.0 Flash** | LLM backbone for all agents |
| **LangChain (Google GenAI)** | LLM interface layer |
| **LlamaIndex** | RAG (Retrieval-Augmented Generation) for data-backed insights |
| **uv** | Lightning-fast Python dependency management |
| **python-dotenv** | Secure environment variable management |

---

## 📁 Project Structure

```
StartupIdea_AI/
├── src/
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── market_researcher.py      # 📊 Market Research Agent
│   │   ├── competitor_analyst.py     # 🏢 Competitor Analyst Agent
│   │   ├── business_strategist.py    # 💰 Business Strategist Agent
│   │   ├── risk_analyst.py           # ⚠️  Risk Analyst Agent
│   │   └── final_decision.py         # ✅ Final Decision Agent
│   ├── tools/
│   │   ├── __init__.py
│   │   └── rag_tool.py               # 📚 LlamaIndex RAG Tool (Advanced)
│   ├── tasks.py                      # Task definitions for each agent
│   └── main.py                       # 🚀 Entry point - runs the Crew
├── .env.example                      # Template for environment variables
├── .gitignore
├── pyproject.toml                    # uv-managed dependencies
└── README.md
```

---

## ⚡ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Edge-Explorer/StartUpIdea_AI.git
cd StartUpIdea_AI
```

### 2. Set Up Environment Variables

```bash
# Copy the example file
cp .env.example .env
```

Then open `.env` and add your **Google API Key**:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

> Get your free API key from [Google AI Studio](https://aistudio.google.com/apikey)

### 3. Install Dependencies with `uv`

```bash
# Install uv if you don't have it
pip install uv

# Install all project dependencies
uv sync
```

### 4. Run the Validator

```bash
uv run src/main.py
```

---

## 🔮 Roadmap

- [x] Multi-agent architecture with CrewAI
- [x] Gemini 2.0 Flash integration
- [ ] LlamaIndex RAG with market research datasets
- [ ] PDF upload for business plan analysis
- [ ] Web search tool for real-time competitor data
- [ ] Streamlit / Gradio UI for non-technical users
- [ ] Memory layer for cross-session idea tracking

---

## 🧑‍💻 Author

<div align="center">

**Made with ❤️ by Karan**

[![GitHub](https://img.shields.io/badge/GitHub-Edge--Explorer-black?style=for-the-badge&logo=github)](https://github.com/Edge-Explorer)

*AI Engineer | Building intelligent systems, one agent at a time.*

</div>

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

*If this project helped you validate your next big idea, give it a ⭐ star!*

</div>
