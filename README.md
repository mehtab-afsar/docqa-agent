

# DocQA Agent

An **enterprise-ready Document Q&A AI Agent** that processes multiple PDFs, extracts structured content, and answers natural language queries with accurate, explainable insights.

> **Bonus:** Includes Arxiv API-based search for querying the latest scientific papers.

---

## 🚀 Project Overview

This project demonstrates applied AI skills in building a robust, scalable tool for enterprise document analysis.  
Given a collection of PDF files, the agent:

- Extracts and organizes information from documents
- Answers user questions about the contents
- Provides citations and references for each answer
- (Bonus) Searches Arxiv.org for relevant research, integrating results in responses

---

## ✨ Features

- **Multi-PDF Upload:** Drag and drop or batch-upload PDF files for analysis.
- **AI-Powered Q&A:** Ask questions in natural language and receive context-aware, accurate answers.
- **Structured Data Extraction:** Extracts tables, headings, bullet points, and more from PDFs.
- **Source Citations:** Each answer includes references to the document and page number.
- **Enterprise-Ready:** Built with modularity, scalability, and security in mind.
- **Arxiv Integration:** (Bonus) Query scientific literature via Arxiv API for up-to-date research answers.

---

## 🛠️ Tech Stack

- **Backend:** Python, FastAPI/Flask, PyPDF2/pdfplumber, OpenAI API or LlamaIndex
- **Frontend:** React.js / Streamlit / Gradio (choose your stack)
- **NLP:** OpenAI GPT-4 / Llama / Huggingface Transformers
- **Arxiv API:** For scientific paper search

---

## 🚩 How It Works

1. **Upload Documents:** Add one or more PDFs using the web interface or API.
2. **Processing:** The agent parses and indexes the content, extracting structured elements.
3. **Ask Questions:** Use the chat interface or API endpoint to query the documents.
4. **Get Answers:** Receive concise, well-cited answers, optionally enhanced with recent Arxiv research.

---

## 🖥️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/mehtab-afsar/docqa-agent.git
cd docqa-agent
````

### 2. Install Dependencies

```bash
# Example for Python projects
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure API Keys

* For OpenAI or other LLMs, create a `.env` file and add your API keys:

```env
OPENAI_API_KEY=your-openai-key
ARXIV_API_KEY=your-arxiv-key (if required)
```

### 4. Run the App

```bash
# Example for FastAPI
uvicorn app:app --reload
```

or

```bash
# Example for Streamlit frontend
streamlit run app.py
```

---

## 💡 Usage

* Access the web UI or use API endpoints to upload PDFs and ask questions.
* For Arxiv search, use `/search_arxiv` endpoint or UI tab.

---

## 📂 Folder Structure

```
docqa-agent/
├── app.py
├── requirements.txt
├── README.md
├── docs/
├── src/
│   ├── document_parser.py
│   ├── qa_engine.py
│   ├── arxiv_integration.py
│   └── ...
├── static/
└── ...
```

---

## 🧑‍💻 Example Query

> **User:** "What are the key findings in the annual report?
> **Agent:** "The key findings are... \[Source: annual\_report.pdf, Page 12]"

---

## 🎯 Evaluation Criteria

* **Robustness:** Handles diverse, messy PDFs.
* **Accuracy:** High-quality answers with references.
* **Enterprise-readiness:** Modular code, scalable architecture, security practices.
* **Bonus:** Arxiv API search implemented and integrated.

---

## 📜 License

[MIT License](LICENSE)

---

## 🤝 Contributions

PRs and issues are welcome! Please open an issue or submit a pull request for any suggestions or bug reports.

---

## 🙏 Acknowledgements

* OpenAI / Huggingface for LLM APIs
* Arxiv.org for scientific paper API
* PyPDF2, pdfplumber for PDF parsing




