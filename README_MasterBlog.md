# 📝 MasterBlog

Welcome to **MasterBlog**, a simple yet powerful blog application built with **Python** and **Flask**.

This project was created as a hands-on exercise to explore core web development concepts and build a fully functional blog from scratch.

---

## 🚀 Features

- View all blog posts
- Create new posts
- Update existing posts
- Delete posts
- Flash messages for user feedback
- Simple JSON-based storage (no database required)

---

## 🧠 What I Learned

This project helped me practice and understand:

- Flask routing and request handling
- Template rendering with Jinja2
- Form handling (GET & POST)
- CRUD operations (Create, Read, Update, Delete)
- Using `url_for()` for clean routing
- Flash messages for user interaction
- Working with JSON as a lightweight data store
- Basic frontend structure with HTML & CSS

---

## 🛠️ Tech Stack

- Python 3
- Flask
- Jinja2
- HTML / CSS
- JSON (as a simple database)

---

## 📦 Installation

1. Clone the repository:
git clone https://github.com/YOUR_USERNAME/Masterblog.git
cd Masterblog

2. Create and activate a virtual environment:
python -m venv .venv
source .venv/bin/activate   # macOS / Linux

3. Install dependencies:
pip install -r requirements.txt

4. Create a `.env` file:
SECRET_KEY=your_secret_key_here

---

## ▶️ Run the App

python app.py

Then open your browser and go to:
http://127.0.0.1:5002

---

## 📁 Project Structure

Masterblog/
│
├── app.py
├── data/
│   └── blog.json
├── templates/
│   ├── index.html
│   ├── add.html
│   ├── update.html
│   └── 404.html
├── static/
│   └── style.css
├── .env
├── requirements.txt
└── README.md

---

## 💡 Future Improvements

- Use a real database (e.g. SQLite with SQLAlchemy)
- Add user authentication
- Improve UI/UX
- Add pagination
- Add search functionality

---

## 📌 Note

This project is intended for learning purposes and demonstrates the fundamentals of building a web application with Flask.

---

## 👨‍💻 Author

Created by Arne
