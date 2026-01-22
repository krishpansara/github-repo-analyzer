# 🔍 GitHub Repo Analyzer - AI Based Repository Review & Summarization Tool (GitMate)


## 📌 Project Overview

**GitHub Repo Analyzer** is an AI-powered application that automatically **summarizes, reviews, and evaluates public GitHub repositories** to provide a clear and structured understanding of any codebase.

The system uses **AI agents and LLM workflows** to analyze repository structure, technologies, and code logic, helping developers, recruiters, and learners quickly understand unfamiliar projects.

Users only need to provide a GitHub repository URL (and optionally a short description). The application clones the repository, scans all files, and generates an intelligent project explanation and review.

---

## 🚀 Features

- 🤖 AI-based repository summarization  
- 🧠 Automatic code understanding and project explanation  
- 🏗️ Repository structure and tech stack detection  
- 📂 Auto cloning and file processing using GitPython  
- 📊 High-level project review and evaluation  
- 🖥️ Interactive Streamlit web interface  

---  

### 🔗 LangChain & LangGraph Integration
- Controlled execution of multiple AI agents  
- Multi-step reasoning for deep repository understanding  
- Structured workflows for summarization, review, and evaluation  
- Consistent and well-formatted analysis outputs  

### 📂 Automatic Repository Processing
- Automatically clones public GitHub repositories using GitPython  
- Scans and processes all project files  
- Identifies and prioritizes important source code and configuration files  
- Prepares repository data for intelligent review and evaluation  

### 🧠 Context-Aware Analysis
- Supports optional project descriptions to enhance analysis  
- Improves:
  - Repository summaries  
  - Architectural understanding  
  - Code review quality  
  - Overall project evaluation  

### 🖥️ Interactive Streamlit Frontend
- Simple UI for repo URL input  
- Real-time analysis visualization  
- Beginner-friendly interface  

---

## 🧰 Tech Stack

**Core Language**
- Python  

**Frontend**
- Streamlit  

**AI / Agents**
- LangChain  
- LangGraph  
- Large Language Models (LLMs)  

**Repository Handling**
- GitPython  

---

## ⚙️ Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/krishpansara/github-repo-analyzer.git
cd github-repo-analyzer
```


### 2️⃣ Create virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Setup environment variables (if applicable)
```bash
OPENAI_API_KEY=your_api_key
# or any other LLM provider keys
```


---

## ▶️ Usage

### Start Streamlit frontend
```bash
streamlit run app.py
```

### Open in browser:
```bash
(http://localhost:8501)
```

- How it works

1. Enter a public GitHub repository URL

2. (Optional) Add a short project description

3. Click analyze

4. The system:
   Clones the repository
   Reads all files
   Executes multi-agent workflows
   Displays structured project understanding

---

## 🏗️ Project Structure
```
github-repo-analyzer/
│
├── agents/
│   ├── structure_agent.py
│   ├── tech_stack_agent.py
│   ├── summarizer_agent.py
│   └── file_analysis_agent.py
│
├── workflows/
│   └── graph.py
│
├── utils/
│   └── repo_loader.py
│
├── app.py
├── requirements.txt
└── README.md
```

---


## 🔧 Configuration

- LLM provider can be changed in the config file
- Agent behavior can be customized for:
  Security review
  Code quality analysis
  Documentation generation
- GitHub access can be extended to private repositories using tokens

---
## 🎯 Use Cases

- Quickly summarize and review large or unfamiliar GitHub repositories  
- Evaluate project structure and overall code quality  
- Faster onboarding into open-source or company codebases  
- Recruiter-friendly technical project assessment  
- Student project feedback and learning support  
- Understanding real-world software architecture and design patterns  


## 👤 Author

**Krish Pansara**

🎓 B.Tech Computer Science Student

GitHub: https://github.com/krishpansara
