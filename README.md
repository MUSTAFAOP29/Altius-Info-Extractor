# 📄 PDF Extractor

Developed a **Streamlit-based PDF extraction tool** that enables users to extract structured text, tables, and images from PDF files. The system supports both a **normal extraction mode** and an **AI-powered extraction** using Google Gemini API for enhanced processing.  

![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-orange)
![GenAI](https://img.shields.io/badge/GenAI-Gemini-red)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## ✨ Features
- 🖥️ Extract text as structured paragraphs  
- 📊 Extract tables while preserving structure  
- 🖼️ Optional image extraction per page (Normal mode)  
- ⚡ AI-powered extraction with Google Gemini for JSON output  
- 📱 Interactive Streamlit interface with preview and download options  

---

## 🛠️ Tech Stack
- **Frontend & UI**: Streamlit  
- **Backend AI**: Google Gemini API  
- **Language**: Python  
- **PDF Processing**: pdfplumber, PyMuPDF  

---

## 📂 Project Structure
~~~
PDF-EXTRACTOR/
│── README.md
│── file.py
│── requirements.txt
│── output.json
│── images/
│   ├── page1_img1.png
│   ├── page2_img1.jpg
│   └── ...
~~~

---

## 📦 Installation (Run Locally)

1. **Clone the repo**
   ```
   git clone https://github.com/MUSTAFAOP29/Altius-Info-Extractor.git
   cd Altius-Info-Extractor
   
2. **Create a virtual environment (recommended)**
~~~
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
pip install -r requirements.txt
Run the Streamlit app
~~~

streamlit run file.py

## 🧠 Tech Stack

| Component  | Technology        |
| ---------- | ----------------- |
| Frontend   | Streamlit         |
| Backend AI | Google Gemini API |
| Language   | Python            |

## Screenshots
### 🔹 Python Script To Extract Features
![Interface](https://github.com/MUSTAFAOP29/Altius-Info-Extractor/blob/main/Screenshot%20(2484).png)
![Outputs](https://github.com/MUSTAFAOP29/Altius-Info-Extractor/blob/main/Screenshot%20(2485).png)

### 🔹 Generatiove Method To Extract Features
![Interface](https://github.com/MUSTAFAOP29/Altius-Info-Extractor/blob/main/Screenshot%20(2486).png)
![Outputs](https://github.com/MUSTAFAOP29/Altius-Info-Extractor/blob/main/Screenshot%20(2487).png)



## 🚀 Live Demo
👉 [Try SQL Buddy here](https://data-extractor-alltius.streamlit.app/)

---

## ⚠️ Note
1. Extraction may take some time depending on the PDF size, so please be patient.  
2. If you choose the **Normal** extraction method, make sure to click the **Extract** button to download the output as a JSON file.





## 📜 License
This project is licensed under the MIT License – free to use and modify with attribution.

## 👨‍💻 Author
Developed with ❤️ by Syed Mustafa
## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/syedmustafa29)
