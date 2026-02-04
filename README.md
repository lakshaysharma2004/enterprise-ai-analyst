# Enterprise AI Knowledge Analyst

### Retrieval-Augmented Generation (RAG) System from Scratch

---

## 📌 Project Overview

**Enterprise AI Knowledge Analyst** is an end-to-end **Retrieval-Augmented Generation (RAG)** system built from scratch to answer user queries using external documents instead of relying solely on a language model’s internal knowledge.

The project demonstrates how large language models (LLMs) can be **grounded in enterprise knowledge bases** using semantic retrieval, reducing hallucinations and improving answer reliability.

This system is designed with **modular architecture**, **clear separation of concerns**, and **industry-aligned engineering practices**.

---

## 🎯 Problem Statement

Large Language Models (LLMs) often:

* hallucinate answers,
* lack access to private or up-to-date information,
* cannot explain where their answers come from.

This project solves that by:

* retrieving relevant knowledge from documents,
* injecting that knowledge into the LLM prompt,
* forcing the model to answer **only from retrieved context**.

---

## 🧠 Key Concept: Retrieval-Augmented Generation (RAG)

RAG combines two components:

1. **Retrieval** – Find relevant document chunks using semantic similarity
2. **Generation** – Generate an answer using only retrieved content

This approach:

* reduces hallucinations,
* improves trustworthiness,
* enables domain-specific knowledge access.

---

## 🏗️ System Architecture

```
Document
   ↓
Parser
   ↓
Chunker
   ↓
Embedder
   ↓
Vector Store
   ↓
Retriever
   ↓
Generator (LLM)
   ↓
Final Answer
```

Each stage is implemented as an **independent module**, making the system extensible and easy to reason about.

---

## 📁 Project Structure

```
enterprise-ai-analyst/
│
├── parsing/        # Document parsers (BaseParser, TextParser)
├── chunking/       # Chunking logic (BaseChunker, TextChunker)
├── core/           # Core data structures (Chunk)
├── embeddings/     # Embedding models
├── vectorstore/    # Vector storage & similarity search
├── retriever/      # Retrieval logic
├── generator/      # RAG-based answer generation
├── config/         # Reserved for future configuration
│
├── main.py         # Entry point
├── README.md       # Project documentation
└── .gitignore
```

> Note: `tests/`, `.env`, and `venv/` are intentionally excluded from version control.

---

## 🧩 Implementation Stages

### Stage 1: Parsing

* Converts raw documents into structured text.
* Current support: plain text files.

### Stage 2: Chunking

* Splits documents into fixed-size chunks.
* Preserves metadata like source file and page number.

### Stage 3: Embedding

* Converts text chunks into semantic vectors.
* Uses sentence-level transformer embeddings.

### Stage 4: Vector Storage & Retrieval

* Stores embeddings in an in-memory vector store.
* Uses cosine similarity for semantic search.

### Stage 5: Generation (RAG)

* Builds a **constrained prompt** using retrieved chunks.
* Instructs the LLM to:
  * use only provided context,
  * explicitly say *“I don’t know”* if the answer is missing.

---

## 🔐 API Key & Security

* OpenAI API key is loaded securely via environment variables.
* `.env` file is excluded from version control.
* No secrets are hard-coded.

---

## 🧪 Testing Strategy

* Individual components were tested locally (parser, chunker, embedder, retriever).
* End-to-end testing validates the full RAG pipeline.
* Tests are intentionally excluded from the public repository.

---

## ⚠️ Known Limitations

* In-memory vector store (not suitable for large-scale production).
* No streaming or conversation memory.
* API usage limited by OpenAI quota.
* Currently supports only text documents.

These limitations are **intentional** to keep the focus on learning core RAG concepts.

---

## 🚀 Future Improvements

* Replace in-memory vector store with FAISS or a database-backed solution.
* Add support for PDFs and DOCX files.
* Implement answer citations.
* Add logging and configuration management.
* Introduce evaluation metrics for retrieval quality.

---

## 📚 Key Learnings

* Why chunk size affects retrieval quality.
* Why prompt design is critical to reduce hallucinations.
* How modular design improves maintainability.
* How retrieval and generation must be decoupled.
* How real-world constraints (API quotas) affect systems.

---

## 👤 Author

**Lakshay Sharma**
Final-Year B.Tech (CSE – AIML)

