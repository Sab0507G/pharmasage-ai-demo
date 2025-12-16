
Right now VS Code is treating it as plain text.

---

## ✅ EXACT FIX — COPY & PASTE THIS (NO CHANGES)

### Open `architecture.md`
### Delete everything
### Paste **this exactly**:

```mermaid
flowchart LR
    User[R&D Researcher] --> UI[Web UI<br/>Streamlit Dashboard]

    UI --> API[FastAPI Backend]

    API --> ORCH[Orchestrator Agent<br/>LangGraph / CrewAI]

    ORCH --> LIT[Literature Agent<br/>PubMed]
    ORCH --> CLIN[Clinical Trials Agent<br/>ClinicalTrials.gov]
    ORCH --> PAT[Patent Intelligence Agent]
    ORCH --> MKT[Market Intelligence Agent]

    LIT --> VDB[Vector DB<br/>FAISS / Chroma]
    CLIN --> VDB
    PAT --> VDB
    MKT --> VDB

    VDB --> INTEL[Central Intelligence Layer<br/>LLM Reasoning]

    INTEL --> REPORT[Ranked Evidence-backed Report]

    REPORT --> UI
