# Zoe-AI
Zoe AI is a dynamic business agent integrating semantic retrieval, LoRA fine-tuned LLMs, Guardrails validation, and continuous evaluation to automate business queries, enhance customer support, and ensure compliance-safe outputs with scalable deployment.

---

## Features

- **Semantic Retrieval with Qdrant**: Retrieve contextually relevant information with high accuracy.
- **LoRA Fine-Tuning**: Efficient adaptation to domain-specific datasets with minimal resource cost.
- **Guardrails Validation**: Enforce safe, compliant, and reliable outputs.
- **Automated Evaluation**: Continuous model quality assessment using DeepEval and RAGAS.
- **FastAPI Backend**: Serve the agent through lightweight RESTful APIs.
- **CI/CD Pipelines**: Automated model testing, evaluation, and deployment.

---

## Tech Stack

- **Language**: Python 3.10+
- **Modeling**: Hugging Face Transformers, PEFT (LoRA)
- **Retrieval**: Qdrant Vector Database
- **Frameworks**: FastAPI, LangChain, Sentence Transformers
- **Guardrails**: Guardrails AI
- **Evaluation**: DeepEval, RAGAS
- **Deployment**: GitHub Actions, Docker (optional)

---

## Architecture

```mermaid
flowchart TD
    A[User Query] --> B[FastAPI Server]
    B --> C[Embed Query with Sentence Transformers]
    C --> D[Semantic Search in Qdrant]
    D --> E[Retrieve Relevant Context]
    E --> F[LoRA Fine-Tuned LLM]
    F --> G[Guardrails Output Validation]
    G --> H[Return Final Safe Response]
    G --> I[Log Evaluation Metrics (DeepEval, RAGAS)]
