# 🚀 ApplyPilot AI

> **Your AI-powered Job Application Copilot**

ApplyPilot AI is an Agentic AI system that automates the repetitive parts of job applications while keeping the human in control.

Instead of manually reading job descriptions, selecting resumes, writing emails, and sending applications, ApplyPilot AI performs these tasks through multiple collaborating AI agents.

---

# ✨ Features

- 🤖 Multi-Agent Architecture using LangGraph
- 📄 Job Description Extraction
- 🧠 Semantic Resume Matching using PostgreSQL + pgvector
- 📊 Resume Analysis & ATS Evaluation
- ✉️ Personalized Email Generation
- 👤 Human-in-the-Loop Approval
- 📧 Gmail Integration for Sending Applications

---

# 🏗️ Current Workflow

```text
START
   │
   ▼
Planner Agent
   │
   ▼
Extractor Agent
   │
   ▼
Resume Matching Agent
(Postgres + pgvector)
   │
   ▼
Resume Analyzer
   │
   ▼
Human Approval
   │
   ▼
Email Writing Agent
   │
   ▼
Human Approval
   │
   ▼
Email Sending Agent
   │
   ▼
END
```

---

# 🧠 Agent Architecture

## 1. Planner Agent

Determines the input type.

Supported inputs

- LinkedIn Job URL
- Company Career URL
- Job Description PDF
- Plain Text Job Description

---

## 2. Extractor Agent

Extracts structured information.

Example

```json
{
  "company": "",
  "role": "",
  "skills": [],
  "experience": "",
  "location": "",
  "recruiter_email": ""
}
```

---

## 3. Resume Matching Agent

Uses semantic similarity search to retrieve the most relevant resume.

Workflow

Job Description

↓

Embedding

↓

PostgreSQL + pgvector

↓

Top Matching Resume

---

## 4. Resume Analyzer

Analyzes

- ATS Compatibility
- Missing Skills
- Matching Skills
- Resume Suitability

---

## 5. Human Approval

The user reviews

- Selected Resume
- ATS Score
- Recommendation

before continuing.

---

## 6. Email Writing Agent

Generates

- Personalized Subject
- Professional Email
- Signature

using the extracted job information.

---

## 7. Email Sending Agent

Sends the approved email through Gmail API.

---

# 🗄️ Tech Stack

## AI

- LangGraph
- LangChain
- Groq / Gemini
- HuggingFace Embeddings

## Backend

- FastAPI

## Database

- PostgreSQL
- pgvector

## Email

- Gmail API

## PDF Processing

- PyPDF

## Environment

- Python
- uv
- Docker (Upcoming)

---

# 📁 Project Structure

```
applypilot-ai/

│
├── app/
│   ├── agents/
│   ├── graph/
│   ├── prompts/
│   ├── services/
│   ├── tools/
│   ├── config.py
│   └── main.py
│
├── resumes/
├── uploads/
├── data/
│
├── .env
├── README.md
├── pyproject.toml
└── requirements.txt
```

---

# 🚀 Setup

Clone the repository

```bash
git clone <repo-url>
cd applypilot-ai
```

Create virtual environment

```bash
uv venv
```

Activate

Windows

```powershell
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
uv sync
```

Create `.env`

```env
GROQ_API_KEY=
GOOGLE_API_KEY=
DATABASE_URL=
```

Run

```bash
python app/main.py
```

---

# 🎯 Upcoming Features

- Resume Optimizer
- Cover Letter Generator
- Company Research Agent
- Application Tracker
- Follow-up Email Agent
- Calendar Integration
- Multi-Resume Management Dashboard

---

# ⭐ Why this project?

Unlike traditional automation scripts, ApplyPilot AI uses multiple specialized AI agents that collaborate to understand job descriptions, retrieve the best resume using semantic search, analyze compatibility, generate personalized application emails, and keep the user in control through Human-in-the-Loop approval.

This project demonstrates practical applications of Agentic AI, Retrieval-Augmented Workflows, Vector Databases, and LLM orchestration.

---

## 👨‍💻 Author

**Ronak Varshney**

If you found this project useful, consider giving it a ⭐ on GitHub.