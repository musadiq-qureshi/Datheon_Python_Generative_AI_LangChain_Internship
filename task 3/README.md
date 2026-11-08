 <h1 align="center">⚡ Multi-Tool Autonomous AI Agent</h1>

<h3 align="center">An Intelligent AI Agent Powered by LangChain & Google Gemini</h3>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.14-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/LangChain-AI%20Framework-green" alt="LangChain">
  <img src="https://img.shields.io/badge/Google-Gemini-orange?logo=google" alt="Google Gemini">
  <img src="https://img.shields.io/badge/Internship-Datheon-purple" alt="Datheon">
  <img src="https://img.shields.io/badge/Task-03-blueviolet" alt="Task 3">
  <img src="https://img.shields.io/badge/Status-Completed-success" alt="Completed">
</p>

<p align="center">
  A Python-based AI agent that searches the web, performs calculations, and reads local text files using multiple integrated tools.
</p>

---

## 📌 Project Overview

The **Multi-Tool Autonomous AI Agent** is developed as Task 3 of the **Datheon Python + Generative AI & LangChain Internship**.

This project demonstrates how an AI agent can understand a user's request, select an appropriate tool, execute the required operation, and generate a final response.

Powered by Google Gemini and LangChain, the agent integrates three tools:

- 🌐 **Web Search:** Retrieves information from the internet using DuckDuckGo.
- 🧮 **Python Calculator:** Performs mathematical calculations.
- 📄 **Local File Reader:** Reads TXT files from the project directory.

---

## ✨ Key Features

- Intelligent tool selection using LangChain.
- DuckDuckGo web search integration.
- Mathematical calculations using restricted Python AST operations.
- Local TXT file reading.
- Google Gemini language model integration.
- Tool execution and observation display.
- AI-generated final responses.
- Input validation and basic security restrictions.

---

## 🛠️ Technologies Used

<table width="100%">
  <thead>
    <tr>
      <th align="left" width="30%">Technology</th>
      <th align="left" width="70%">Purpose</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="left">Python 3.14</td>
      <td align="left">Core programming language</td>
    </tr>
    <tr>
      <td align="left">LangChain</td>
      <td align="left">AI agent creation and tool integration</td>
    </tr>
    <tr>
      <td align="left">Google Gemini</td>
      <td align="left">Language model for understanding and generating responses</td>
    </tr>
    <tr>
      <td align="left">DuckDuckGo Search (DDGS)</td>
      <td align="left">Web search and information retrieval</td>
    </tr>
    <tr>
      <td align="left">Python AST</td>
      <td align="left">Restricted mathematical expression evaluation</td>
    </tr>
    <tr>
      <td align="left">Python-dotenv</td>
      <td align="left">Environment variable and API key management</td>
    </tr>
  </tbody>
</table>

## 📂 Project Structure

```text
Task_3/
│
├── main.py
├── sample.txt
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
│
└── screenshots/
    ├── task3_agent_code_01.png
    ├── task3_agent_code_02.png
    ├── task3_agent_code_03.png
    ├── task3_agent_code_04.png
    ├── task3_agent_code_05.png
    ├── task3_agent_code_06.png
    ├── task3_agent_ready.png
    ├── task3_agent_calculator.png
    ├── task3_agent_web_search.png
    └── task3_agent_file_reader.png
```

---

## ⚙️ Installation & Setup

### Prerequisites

- Python 3.14 or a compatible Python version.
- Google Gemini API key.
- Internet connection for Gemini requests and web search.

### Step 1: Clone the Repository

```bash
git clone https://github.com/musadiq-qureshi/Datheon_Python_Generative_AI_LangChain_Internship.git
```

### Step 2: Navigate to Task 3

```bash
cd Datheon_Python_Generative_AI_LangChain_Internship/Task_3
```

### Step 3: Create a Virtual Environment

```bash
python -m venv .venv
```

### Step 4: Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Configure the Gemini API Key

Create a `.env` file in the Task 3 directory and add:

```env
GEMINI_API_KEY=your_api_key_here
```

Replace the placeholder with your own Gemini API key.

**Security:** Never upload your real `.env` file to GitHub. The `.env.example` file contains only a placeholder.

### Step 7: Run the Application

```bash
python main.py
```

---

## 💻 Example Usage

### 🌐 Web Search

**Example question:**

```text
Search the web for Python 3.14 official release notes.
```

### 🧮 Python Calculator

**Example question:**

```text
Calculate 25000 * 2 + 5000
```

### 📄 Local File Reader

**Example question:**

```text
Read sample.txt and tell me the annual revenue and number of employees.
```

---

## 📸 Screenshots & Demonstrations

The following screenshots demonstrate the source code, agent initialization, and successful execution of all three tools.

### 1. Python Source Code

**Code Screenshot 01**

![Python Code Screenshot 01](screenshots/task3_agent_code_01.png)

**Code Screenshot 02**

![Python Code Screenshot 02](screenshots/task3_agent_code_02.png)

**Code Screenshot 03**

![Python Code Screenshot 03](screenshots/task3_agent_code_03.png)

**Code Screenshot 04**

![Python Code Screenshot 04](screenshots/task3_agent_code_04.png)

**Code Screenshot 05**

![Python Code Screenshot 05](screenshots/task3_agent_code_05.png)

**Code Screenshot 06**

![Python Code Screenshot 06](screenshots/task3_agent_code_06.png)

---

### 2. Agent Initialization

![Agent Ready](screenshots/task3_agent_ready.png)

---

### 3. Calculator Tool Execution

![Calculator Test](screenshots/task3_agent_calculator.png)

---

### 4. DuckDuckGo Web Search Execution

![Web Search Test](screenshots/task3_agent_web_search.png)

---

### 5. Local File Reader Execution

![Local File Reader Test](screenshots/task3_agent_file_reader.png)

---

## 🔐 Security & Privacy

Security considerations implemented in this project:

- Gemini API key is loaded through environment variables.
- `.env` is excluded through `.gitignore`.
- Calculator uses restricted AST operations instead of `eval()`.
- File reader accepts TXT files directly inside the project directory.
- File reading is limited to a maximum size of 100 KB.
- Web search results and file contents are treated as untrusted input.
- Fictional demonstration data is used in `sample.txt`.

**Privacy Note:** User queries and local file contents processed by the agent may be sent to external services, including Google Gemini and DuckDuckGo. Do not submit passwords, API keys, confidential documents, or other sensitive information.

---

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

- Developing multi-tool AI agents using LangChain.
- Integrating Google Gemini with Python applications.
- Implementing external web search.
- Creating a restricted Python calculator.
- Reading and processing local text files.
- Understanding tool-based AI agent execution.
- Managing API keys and applying basic security practices.

---

## 🏆 Internship Information

<table>
  <tbody>
    <tr>
      <th align="left">Internship</th>
      <td>Datheon Python + Generative AI & LangChain Internship</td>
    </tr>
    <tr>
      <th align="left">Task Number</th>
      <td>Task 03</td>
    </tr>
    <tr>
      <th align="left">Project</th>
      <td>Multi-Tool Autonomous AI Agent</td>
    </tr>
    <tr>
      <th align="left">Status</th>
      <td>Successfully Completed</td>
    </tr>
  </tbody>
</table>

---

## 👨‍💻 Author

**Musadiq Mehmood Qureshi**

- GitHub: [musadiq-qureshi](https://github.com/musadiq-qureshi)
- LinkedIn: [Musadiq Qureshi](https://www.linkedin.com/in/musadiq-qureshi-32271936a/)

---

<p align="center">
  <strong>⭐ Thank you for visiting this project!</strong>
  <br>
  <sub>Built with Python, LangChain and Google Gemini.</sub>
</p>
