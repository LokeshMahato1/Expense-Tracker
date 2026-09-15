# Expense-Tracker
A simple Python GUI app to record daily expenses, categorize them, and calculate total spending.


# 💰 Expense Tracker

> 📊 A simple and user-friendly desktop Expense Tracker built with **Python and Tkinter**.

## ✨ Features

- 💵 Add and manage expenses
- 🏷️ Categorize expenses
- 💳 Support for Cash and Online payments
- 🔐 Automatic transaction ID for online payments
- 📁 CSV-based data storage
- 💰 Automatic total spending calculation
- 📊 Spending breakdown with a pie chart
- 📋 Recent transactions table
- ✅ Expense validation
- 🧹 Automatically clears the form after adding an expense
- 🔄 Automatically updates the dashboard after adding an expense

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| 🐍 Python | Main programming language |
| 🖥️ Tkinter | Desktop GUI |
| 📊 Matplotlib | Spending visualization |
| 📄 CSV | Expense data storage |
| 🖼️ Pillow | Image/logo handling |

## 📂 Project Structure

```text
Expense-Tracker/
│
├── 📄 main.py
│
├── 📦 Models/
│   └── expense.py
│
├── ⚙️ Services/
│   └── expense_service.py
│
├── 💾 Storage/
│   └── csv_manager.py
│
├── 🖥️ UI/
│   ├── app.py
│   ├── dashboard.py
│   ├── header.py
│   └── transactions.py
│
├── 🔧 utils/
│   ├── transaction_id.py
│   └── validator.py
│
├── 🖼️ assets/
│   └── logo.png
│
├── 🚫 .gitignore
└── 📖 README.md