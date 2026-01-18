# 🚀 GenAI LinkedIn Post Generator

A Python-based **Generative AI application** that helps you automatically create engaging, professional, and high-quality LinkedIn posts using Large Language Models (LLMs). This project is designed to streamline personal branding and content creation for developers, students, and professionals.

---

## ✨ Features

* 🔹 Generate LinkedIn posts from simple prompts or keywords
* 🔹 Uses environment variables for secure API key management
* 🔹 Clean and modular Python code structure
* 🔹 JSON-based data handling for flexibility and scalability
* 🔹 Easy to run locally with a virtual environment

---

## 🛠️ Tech Stack

* **Python 3.10+**
* **Pandas** (Data processing)
* **LLM / GROQ API** (Text generation)
* **Git & GitHub** (Version control)
* **Virtual Environment (.venv)**

---

## 📁 Project Structure

```
GenAI-LinkedIn-Post-Generator/
│
├── data/
│   ├── llm.py                # Handles LLM/API interaction
│   ├── main.py             # Entry point of the application
│   ├── post_generator.py  # LinkedIn post generation logic
│   ├── prepare_data.py    # Data loading and preprocessing
│   ├── raw_data.json      # Raw input data
│   ├── processed_data.json
│   └── processed_data.py
│
├── .gitignore
├── .env.example
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Jitendra-HUB/GenAI-LinkedIn-Post-Generator.git
cd GenAI-LinkedIn-Post-Generator
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

Activate it:

**Windows:**

```bash
.venv\Scripts\activate
```

**Mac/Linux:**

```bash
source .venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```


### 4️⃣ Configure Environment Variables

Create a `.env` file in the root folder:

```
GROQ_API_KEY=your_api_key_here
MODEL_NAME=llama-3.3-70b-versatile
```

---

### 5️⃣ Run the Project

```bash
python data/main.py
```

---

## 🧪 Example Usage

Input:

```
Topic: Motivation
Language:Hinglish 
Length: Medium
```

Output:

```
🚀"Motivation ka sabse bada source humari khud ki zaroorat hoti hai. Jab humein kuch achieve karna hota hai, tab humari mehnat aur lagan badh jaati hai. Apne goals ko achieve karne ke liye, humein apne aap par vishwas rakhna chahiye. Motivation ke liye kisi bhi cheez ki zaroorat nahi, bas apne sapne ko poora karne ka junoon hona chahiye. Toh aaj se hi apne sapne ko poora karne ki shuruaat karein!" #Motivation #Success
```

---

## 🔐 Security Best Practices

* Never commit your `.env` file
* Always use `.env.example` for sharing config structure
* Rotate API keys if exposed accidentally

---

## 🌟 Future Improvements

* Web-based UI (Streamlit)
* Multiple tone & format templates
* Hashtag generator
* Post scheduling integration

---

## 👤 Author

**Jitendra Pradhan**
Prompt Engineer | GenAI & ML Enthusiast

🔗 GitHub: [https://github.com/Jitendra-HUB](https://github.com/Jitendra-HUB)

---

## 📜 License

This project is licensed under the MIT License. Feel free to use, modify, and share.

---

> ⭐ If you like this project, consider starring the repository — it really helps!

---

## 🔍 How This Project Is Built

1. **Data Collection**
   Manually curated high-quality LinkedIn posts across multiple domains and converted them into a structured **JSON dataset** for consistency and scalability.

2. **Data Preprocessing**
   Cleaned, normalized, and transformed the raw JSON data using Python to remove noise, standardize text, and prepare it for efficient model input and prompt engineering.

3. **LLM Integration (Groq API)**
   Integrated a **Groq-hosted Large Language Model (LLM)** via API to generate professional, context-aware, and engaging LinkedIn posts based on user-defined topics, tone, and length.

4. **User Interface (Streamlit)**
   Built an interactive **Streamlit web interface** that allows users to generate posts in real time with customizable inputs such as topic, tone, and format.

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve this project:

1. Fork the repository
2. Create a new branch (`feature/your-feature-name`)
3. Commit your changes
4. Open a Pull Request

---

## 📬 Contact

For suggestions, feedback, or collaboration:

* GitHub: [https://github.com/Jitendra-HUB](https://github.com/Jitendra-HUB)
* LinkedIn: [https://www.linkedin.com/in/jitendra20/](https://www.linkedin.com/in/jitendra20/)

