
# Cold Email Generator 🤖

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/built%20with-Streamlit-ff69b4.svg)](https://streamlit.io)
[![LangChain](https://img.shields.io/badge/powered%20by-LangChain-purple.svg)](https://www.langchain.com/)

An end-to-end generative AI application that empowers **software and AI service companies** to create highly personalized and effective cold emails.

This tool automates the tedious process of drafting outreach messages, ensuring each email is contextually relevant and tailored to the recipient.

---

## 🚀 Key Features

*   **🧠 AI-Powered Email Drafting:** Leverages Llama 3 to generate persuasive, coherent, and customized email copy.
*   **🎯 Context-Aware Personalization:** Uses ChromaDB to retrieve industry-specific data, case studies, and company info, making every email resonate with the prospect.
*   **⚙️ End-to-End Automated Workflow:** A seamless pipeline from data ingestion and context retrieval to final AI-powered generation.
*   **🖥️ Interactive User Interface:** Built with Streamlit for an intuitive and easy-to-use experience, no technical expertise required to operate.
*   **🌍 Fully Open-Source:** Built with leading community-driven frameworks and tools, making it transparent and easy to extend.

---

## 💡 How It Works

The application follows a Retrieval-Augmented Generation (RAG) pipeline to deliver personalized emails:

1.  **Data Ingestion:** Domain-specific documents (e.g., your company's case studies, service descriptions, market research) are loaded and processed.
2.  **Embedding and Storage:** The processed text is converted into vector embeddings using SentenceTransformers and stored in a ChromaDB vector store.
3.  **Context Retrieval:** When you input a target company and service, the system queries ChromaDB to find the most relevant information from the knowledge base.
4.  **LLM Generation:** The retrieved context is combined with your prompt and fed to Llama 3 via LangChain, which then generates a compelling, personalized cold email.

---

## 🛠️ Tech Stack

The project integrates a modern stack of AI and development tools to deliver a robust solution.

| Component | Tool | Purpose |
| :--- | :--- | :--- |
| **LLM** | **Llama 3** | Drives the core natural language generation for email drafting. |
| **Vector Store** | **ChromaDB** | Stores and retrieves context embeddings for personalization. |
| **Orchestration** | **LangChain** | Manages prompts, chains, and the retrieval-generation workflow. |
| **Frontend** | **Streamlit** | Provides a simple and interactive user interface. |
| **Embedding Model** | **SentenceTransformers**| Converts text data into high-quality vector representations. |

---



## ⚙️ Installation & Setup

Get the application running on your local machine with these simple steps.

### Prerequisites
*   Python 3.9+
*   Git

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/cold-email-generator.git
cd cold-email-generator
```

### 2. Set Up a Virtual Environment
It's recommended to use a virtual environment to manage dependencies.
*   **macOS/Linux:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
*   **Windows:**
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

### 3. Configure the Application
Create and configure your settings in the `config/` directory or a `.env` file as required by the application setup. This includes specifying the path to your Llama 3 model.

### 4. Run the Application
```bash
streamlit run main.py
```
Open your browser and navigate to `http://localhost:8501` to start using the Cold Email Generator.

---

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

To contribute:
1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

---

## 📄 License

This project is distributed under the MIT License. See the `LICENSE` file for more information.
