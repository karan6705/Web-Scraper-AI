# AI Web Scraper

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/)  [![Streamlit](https://img.shields.io/badge/streamlit-1.0-orange)](https://streamlit.io/)  [![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)

An interactive Streamlit app that scrapes any public website’s DOM, cleans and splits its content, and leverages an Ollama LLM (via LangChain) to extract exactly the information you request.

---

## 📋 Table of Contents

1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Running the App](#running-the-app)
6. [Usage](#usage)
7. [Project Structure](#project-structure)
8. [Contributing](#contributing)
9. [License](#license)

---

## ✨ Features

* Enter a URL and scrape its full DOM
* Extract and clean the `<body>` content
* Split large DOM into manageable chunks
* Ask free‑form questions about the page
* Chain through Ollama’s local LLM for precise parsing
* Interactive web UI via Streamlit

---

## 🔧 Prerequisites

* Python 3.9+
* [Streamlit](https://streamlit.io/)
* [Ollama](https://ollama.com/) installed and running locally with model `phi3`
* Internet access to scrape target URLs

---

## 🚀 Installation

```bash
# 1. Clone the repo
git clone https://github.com/karan6705/Web-Scraper-AI.git
cd Web-Scraper-AI

# 2. (Optional) create & activate a virtual environment
python -m venv .venv
source .venv/bin/activate

# 3. Install Python dependencies
pip install -r requirements.txt
```

---

## ⚙️ Configuration

No environment variables are required by default. Ensure Ollama is running with your chosen LLM:

```bash
ollama run phi3
```

If you use a different model, update `model="phi3"` in `parse_with_ollama()` within `parse.py` or the main script.

---

## ▶️ Running the App

```bash
streamlit run app.py
```

This will open a browser window at `http://localhost:8501`.

---

## 📡 Usage

1. **Scrape Website**:

   * Paste a URL into the input box.
   * Click **Scrape Website**.
   * View the cleaned DOM under “View DOM Content.”

2. **Parse Content**:

   * Describe the data you want to extract in the text area.
   * Click **Parse Content**.
   * The app displays only the exact matching information, or an empty string if none.

<details>
<summary>Core Streamlit Code</summary>

```python
import streamlit as st
from scrape import (
    scrape_website,
    extract_body_content,
    clean_body_content,
    split_dom_content,
)
from parse import parse_with_ollama

st.title("AI Web Scraper")
url = st.text_input("Enter Website URL")

if st.button("Scrape Website") and url:
    dom = scrape_website(url)
    body = extract_body_content(dom)
    clean = clean_body_content(body)
    st.session_state.dom_content = clean
    with st.expander("View DOM Content"):
        st.text_area("DOM Content", clean, height=300)

if "dom_content" in st.session_state:
    desc = st.text_area("Describe what you want to parse")
    if st.button("Parse Content") and desc:
        chunks = split_dom_content(st.session_state.dom_content)
        result = parse_with_ollama(chunks, desc)
        st.write(result)
```

</details>

---

## 🗂️ Project Structure

```text
Web-Scraper-AI/
├── app.py             # Streamlit UI
├── scrape.py         # scrape_website, extract & clean body, split DOM
├── parse.py          # LangChain + Ollama parsing logic
├── requirements.txt  # Python dependencies
└── README.md         # This file
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a branch: `git checkout -b feat/my-addition`
3. Commit your changes: `git commit -m "Add feature X"`
4. Push & open a PR
5. Ensure code style via `black` and `flake8`

---

## 📄 License

This project is released under the [MIT License](LICENSE).
