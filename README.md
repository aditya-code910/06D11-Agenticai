#  Multi-Agent Manufacturing System

An advanced **Agentic AI system** that leverages multiple intelligent agents to collaboratively generate structured manufacturing insights.

---

##  Overview

The **Multi-Agent Manufacturing System** demonstrates how modern AI systems can move beyond single-model limitations by using **multiple specialized agents** working together.

In traditional AI systems, a single model handles all tasks, often resulting in:
- Unstructured outputs
- Lack of specialization
- Inefficient workflows

This project solves these challenges using an **Agent-Based Architecture**, where each agent performs a specific role and collaborates to produce high-quality results.

---

##  Objectives

- Implement **multi-agent collaboration**
- Enable **task delegation and agent hand-off**
- Maintain **context sharing across agents**
- Generate **structured and meaningful manufacturing reports**
- Demonstrate real-world **Agentic AI workflows**


---

##  System Architecture

The system follows a layered architecture:


### 🔹 Core Components

- **Frontend Layer**
  - Captures user input
  - Displays generated output

- **Backend (Flask API)**
  - Handles requests
  - Triggers agent workflow
  - Aggregates responses

- **Agent Orchestrator (CrewAI / LangChain)**
  - Manages agent execution
  - Handles task flow and coordination

- **Agent Layer**
  - **Research Agent** → Collects manufacturing data
  - **Writer Agent** → Generates structured reports

- **AI Layer**
  - LLM APIs (OpenRouter / HuggingFace)
  - Provides intelligence to all agents

---

##  Workflow

1. User enters manufacturing prompt  
2. Request is sent to backend API  
3. Agent Orchestrator initializes workflow  
4. Research Agent gathers relevant insights  
5. Context is passed to Writer Agent  
6. Writer Agent generates structured report  
7. Final output is returned to user  

---

##  Tech Stack

| Technology | Purpose |
|----------|--------|
| Python | Core programming |
| Flask | Backend API |
| HTML/CSS/JS | Frontend UI |
| CrewAI / LangChain | Agent orchestration |
| OpenRouter | LLM API |
| HuggingFace | Model integration |

---

##  Key Features

- ✅ Multi-agent collaboration  
- ✅ Task specialization  
- ✅ Context-aware processing  
- ✅ Structured output generation  
- ✅ Modular and scalable design  

---

##  Results

The system successfully:
- Generates structured manufacturing reports  
- Demonstrates agent collaboration  
- Improves output clarity and accuracy  
- Simulates real-world AI workflows  

---

##  Key Concepts

- Agentic AI  
- Task decomposition  
- Inter-agent communication  
- Workflow orchestration  
- Stateless system design  

---

##  Future Scope

- Add advanced agents (Planner, Analyzer, Optimizer)  
- Implement Retrieval-Augmented Generation (RAG)  
- Integrate Vector Database (FAISS / ChromaDB)  
- Develop advanced UI (React + dashboards)  
- Add authentication and security layers  
- Enable report export (PDF/Docs)  

---

##  Conclusion

This project demonstrates how **Agentic AI systems** can transform traditional workflows by introducing **collaboration, specialization, and structured processing**.

By distributing tasks across multiple agents, the system achieves:
- Better accuracy  
- Improved scalability  
- Clear and structured outputs  

It serves as a strong foundation for building **next-generation intelligent systems**.

---

##  Team

- Aaditi Bhale  
- Abhigyan Singh Thakur  
- Aditya Purohit  
- Dhruv Jain  
- Divyansh Tyagi  

---

##  Acknowledgment

This project was developed as part of the **Agentic AI course at Medicaps University (Datagami Skill-Based Program)**.

---

##  How to Run

```bash
# Clone repository
git clone https://github.com/your-repo-link

# Install dependencies
pip install -r requirements.txt

# Run application
python app.py
