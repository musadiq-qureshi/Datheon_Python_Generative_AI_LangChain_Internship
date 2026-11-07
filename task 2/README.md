
<h1 align="center">⚡ Document Q&A Assistant | RAG & Vector Embeddings</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.14-blue?logo=python&logoColor=white" alt="Python 3.14" />
  <img src="https://img.shields.io/badge/LangChain-RAG-green?logo=chainlink&logoColor=white" alt="LangChain RAG" />
  <img src="https://img.shields.io/badge/Google-Gemini-4285F4?logo=google&logoColor=white" alt="Google Gemini" />
  <img src="https://img.shields.io/badge/Vector_Database-ChromaDB-orange" alt="ChromaDB" />
  <img src="https://img.shields.io/badge/Internship-Datheon-red" alt="Datheon Internship" />
</p>

<p align="center">
  <b>Intelligent PDF Question Answering Powered by Retrieval-Augmented Generation</b>
</p>

<p align="center">
  A Python-based AI application that transforms PDF documents into searchable knowledge using LangChain, Google Gemini Embeddings, and ChromaDB.
</p>

<p align="center">
  <a href="https://github.com/musadiq-qureshi">
    <img src="https://img.shields.io/badge/GitHub-My_Profile-181717?logo=github&logoColor=white" alt="GitHub Profile" />
  </a>
  <a href="https://www.linkedin.com/in/musadiq-qureshi-32271936a/">
    <img src="https://img.shields.io/badge/LinkedIn-Musadiq_Qureshi-0A66C2?logo=linkedin&logoColor=white" alt="LinkedIn Profile" />
  </a>
</p>

---

## 🎯 Project Overview

This project was developed as **Task 2** of the Datheon Python + Generative AI & LangChain Internship.

The application allows users to ask questions about PDF documents and receive relevant answers using **Retrieval-Augmented Generation (RAG)**.

It extracts text from PDF files, divides the content into smaller chunks, converts the chunks into vector embeddings, and stores them in ChromaDB.

When a user asks a question, the system retrieves relevant document content and uses Google Gemini to generate an answer based only on the provided document.

## ✨ Key Features

- 📄 PDF document loading and text extraction
- ✂️ Recursive text splitting into smaller chunks
- 🧠 Google Gemini embedding generation
- 🗄️ Persistent vector storage using ChromaDB
- 🔍 Similarity-based document retrieval
- 💬 AI-powered question answering with LangChain
- 📑 Retrieved document page references
- 🛡️ Answers restricted to the provided document
- 🚫 Handles questions when information is unavailable
- ⚙️ Input validation and error handling
- 💻 Interactive command-line interface

## 🛠️ Technologies Used

| Technology | Purpose |
|:---|:---|
| Python | Main programming language |
| LangChain | RAG application framework |
| Google Gemini | AI answer generation |
| Gemini Embeddings | Text vectorization |
| ChromaDB | Vector database |
| PyPDF | PDF text extraction |
| python-dotenv | Environment variable management |

---

## 🧠 How the RAG System Works

The application follows this workflow:

```text
             PDF Document
                   |
                   v
              PDF Loading
                   |
                   v
            Text Extraction
                   |
                   v
             Text Splitting
                   |
                   v
          Gemini Embeddings
                   |
                   v
                ChromaDB
             Vector Storage
                   |
                   |
             User Question
                   |
                   v
           Similarity Search
                   |
                   v
           Relevant Context
                   |
                   v
            Google Gemini
                   |
                   v
              Final Answer
                   |
                   v
        Retrieved Page References
```

## 📁 Project Structure

### GitHub Repository Structure

```text
Task-2/
│
├── main.py
├── sample.pdf
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
│
└── screenshots/
    ├── task2_code_1.png
    ├── task2_code_2.png
    ├── task2_code_3.png
    ├── task2_code_4.png
    ├── task2_code_5.png
    ├── task2_code_6.png
    ├── task2_output_1.png
    ├── task2_output_2.png
    └── task2_output_3.png
```

### Local Runtime Structure

The following folders and files are used or generated locally when running the application:

```text
Task-2/
│
├── .venv/          # Python virtual environment
├── chroma_db/      # Persistent ChromaDB vector database
├── __pycache__/    # Python-generated cache files
├── .env            # Private Gemini API key
│
└── Project Files
```

> **Note:** `.venv/`, `chroma_db/`, `__pycache__/`, and `.env` are excluded from GitHub through `.gitignore`. ChromaDB creates its local database automatically when the application runs.

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/musadiq-qureshi/Datheon_Python_Generative_AI_LangChain_Internship.git
```

### 2. Open the Task-2 Folder

```bash
cd Datheon_Python_Generative_AI_LangChain_Internship/Task-2
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure the Gemini API Key

Create a `.env` file inside the Task-2 folder and add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

> **Important:** Never upload your real `.env` file or API key to GitHub.

### 7. Run the Application

```bash
python main.py
```

The application will load the PDF, process its content, create embeddings, store them in ChromaDB, and start the interactive question-answering system.

## 🧪 Testing and Results

The application was tested with different questions using the sample PDF document.

| Test Question | Result |
|:---|:---|
| What courses does Global Learning Hub offer? | Lists the available courses |
| How much does Python Foundations cost? | EUR 180 |
| How many desktop computers are available? | 24 |
| What attendance percentage is required for a certificate? | 80% |
| What are the support desk hours? | Monday–Friday: 08:30–17:30; Saturday: 10:00–13:00 |
| Does the center offer cybersecurity courses? | Correctly reports that the information is unavailable |

---

### 📸 Sample Application Outputs

**1. RAG Assistant Ready**

![RAG Assistant Ready](screenshots/task2_output_1.png)

**2. Successful Question and Answer**

![Successful Question and Answer](screenshots/task2_output_2.png)

**3. Missing Information Handling**

![Missing Information Handling](screenshots/task2_output_3.png)

## 💻 Code Screenshots

The following screenshots show different sections of the implementation.

**Code Section 1**

![Task 2 Code 1](screenshots/task2_code_1.png)

**Code Section 2**

![Task 2 Code 2](screenshots/task2_code_2.png)

**Code Section 3**

![Task 2 Code 3](screenshots/task2_code_3.png)

**Code Section 4**

![Task 2 Code 4](screenshots/task2_code_4.png)

**Code Section 5**

![Task 2 Code 5](screenshots/task2_code_5.png)

**Code Section 6**

![Task 2 Code 6](screenshots/task2_code_6.png)

## 🔐 Security and Privacy

Security and privacy were considered during development.

- 🔑 API keys are managed through environment variables.
- 🔒 The real `.env` file is excluded from GitHub.
- 📝 `.env.example` contains only a placeholder.
- 🛡️ The Python virtual environment is excluded from the repository.
- 🗄️ The local ChromaDB database is excluded from GitHub.
- 📄 The sample PDF contains fictional organization information.
- 🚫 No real API keys or private credentials are included in the project files.

## 📚 Learning Outcomes

Through this project, I gained practical experience with:

- Loading and processing PDF documents using Python.
- Splitting large documents into smaller text chunks.
- Understanding vector embeddings.
- Working with Google Gemini embedding models.
- Storing and retrieving vectors using ChromaDB.
- Building a RAG pipeline with LangChain.
- Generating document-based answers using an LLM.
- Handling missing information and application errors.

## 👨‍💻 Developer

**Musadiq Mehmood Qureshi**

<p>
  <a href="https://github.com/musadiq-qureshi">
    <img src="https://img.shields.io/badge/GitHub-Visit_Profile-181717?logo=github&logoColor=white" alt="GitHub Profile" />
  </a>
  <a href="https://www.linkedin.com/in/musadiq-qureshi-32271936a/">
    <img src="https://img.shields.io/badge/LinkedIn-Connect_with_Me-0A66C2?logo=linkedin&logoColor=white" alt="LinkedIn Profile" />
  </a>
</p>

- **GitHub:** [musadiq-qureshi](https://github.com/musadiq-qureshi)
- **LinkedIn:** [Musadiq Qureshi](https://www.linkedin.com/in/musadiq-qureshi-32271936a/)

## 🏢 Internship Information

**Organization:** Datheon  
**Program:** Python + Generative AI & LangChain Internship  
**Task:** Task 2 – Document Q&A Assistant with RAG and Vector Embeddings

---

<p align="center">
  <b>⚡ Built with Python, LangChain, Google Gemini, and ChromaDB</b>
</p>

<p align="center">
  <i>Learning • Building • Improving</i>
</p>
