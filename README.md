
# LangChain + Streamlit: Celebrity Search Demo

This project is a **Streamlit application** that demonstrates how to use **LangChain with OpenAI** to create a multi-step conversational tool. The app enables users to input a celebrity's name and retrieves:

- Basic information about the person  
- Their date of birth  
- Five major world events that happened around that date  

---

## 🚀 Features

- 🌐 Streamlit-based user interface  
- 🔗 Uses LangChain's `LLMChain` and `SequentialChain` for sequential task execution  
- 🧠 Employs `ConversationSummaryBufferMemory` for context-aware processing  
- 🧾 Structured output using Streamlit expanders  

---

## 🧱 Project Structure

```
langchain-streamlit-celebrity-search/
│
├── main.py                  # Streamlit application logic
├── constants.py             # File storing OpenAI API key
├── promptInput.py           # (Optional) Extra prompt utilities
├── requirements.txt         # Python dependencies
├── Screenshot 2025-06-09.png# App screenshot
├── venv/                    # Python virtual environment (optional)
└── README.md                # Project documentation
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/langchain-streamlit-celebrity-search.git
cd langchain-streamlit-celebrity-search
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Add Your OpenAI API Key

Edit `constants.py`:

```python
# constants.py
openai_key = "your-openai-api-key"
```

---

## ▶️ Run the Application

```bash
streamlit run main.py
```

---

## 📸 Screenshot

![App Screenshot](./Screenshot%202025-06-09%20214717.png)

---

## 🧠 How It Works

1. **User Input**: Enters a celebrity name.  
2. **Chain 1**: Retrieves general info about the person.  
3. **Chain 2**: Determines their date of birth.  
4. **Chain 3**: Lists five major world events from that time.  
5. **Sequential Execution**: Combines all steps in a single call via `SequentialChain`.  
6. **Streamlit Output**: Displays detailed results in separate expanders.  

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **LangChain**
- **OpenAI API**

---

## 🪪 License

MIT License. Free to use and modify.

---

## 🙏 Acknowledgments

- [LangChain](https://github.com/hwchase17/langchain)  
- [Streamlit](https://streamlit.io/)  
- [OpenAI](https://platform.openai.com/)  
