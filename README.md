## 🧮 Telegram Bot: Hybrid Calculator-4000

### 📌 About the Project
This project is a hybrid Telegram chatbot that functions as a fully interactive calculator. 
Unlike standard chatbots that spam the chat history with text replies, this project implements a **UI-based (Single-Screen) approach**. It dynamically updates a single message using the Telegram API, mimicking the screen of a real physical calculator.

This project was developed as a final assignment for the "Programming in Python" course.

### 🚀 Key Features
* **Interactive UI:** A custom mathematical keyboard via `ReplyKeyboardMarkup`.
* **Dynamic Screen:** Updates calculations on the same message without cluttering the chat history.
* **Session Management:** Supports multiple users simultaneously by isolating states using `chat_id`.
* **Exception Handling:** Prevents bot crashes from invalid inputs (e.g., division by zero, syntax errors).
* **Database Logging:** Uses **Django ORM** and **SQLite** as a backend to securely log all user requests and calculation results.

## 🛠️ Technology Stack
* **Python 3.x** - Main programming language.
* **pyTelegramBotAPI (telebot)** - Interaction with the Telegram API.
* **Numexpr** - Fast and secure evaluation of string mathematical expressions.
* **Django ORM** - Database management and automated admin panel creation.

## ⚙️ Installation and Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git
   cd YOUR_REPO_NAME