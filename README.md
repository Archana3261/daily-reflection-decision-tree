# 📊 Daily Job Preparation Reflection System

```mermaid
flowchart TD

A[Start] --> B{Applied to Job Today?}

B -->|Yes| C{Practiced Technical Skills?}
B -->|No| D{Studied/Learned Today?}

C -->|Yes| E{Learned Something New?}
C -->|No| F[Applied but lacking skill practice]

E -->|Yes| G[Excellent progress day 🚀]
E -->|No| H[Good, but add learning for growth]

C --> I{Updated Resume/LinkedIn?}
I -->|Yes| J[Strong preparation strategy]
I -->|No| K[Improve profile visibility]

D -->|Yes| L{Practiced Problems?}
D -->|No| M{Reason?}

L -->|Yes| N[Learning-focused day 👍]
L -->|No| O[Convert learning into practice]

M -->|Time Issue| P[Improve time management]
M -->|Low Motivation| Q[Set small daily goals]
M -->|Distraction| R[Reduce distractions]
```


## 🤖 AI Agent

This project includes a rule-based AI agent designed to simulate decision-making for daily job preparation evaluation.

The agent takes inputs such as job applications, learning, and practice, and provides meaningful feedback based on predefined logic.

The system ensures transparency and reliability by avoiding probabilistic outputs and relying on deterministic logic.

---

## 🛡️ Guardrails Implemented

- Input validation ensures only valid responses are accepted  
- Rule-based logic prevents AI hallucination  
- Outputs are predefined and controlled  
- No random or misleading responses  
- Handles missing or invalid inputs safely  

---

## ⚙️ How to Run

```bash
python agent.py
```

---

## 🧪 Example Output

Input:
Applied = No  
Studied = Yes  
Practiced = No  

Output:
Convert learning into practice 
