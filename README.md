
# 🤖 Binance Futures Trading Bot – Python CLI Project

An end-to-end **Python-based Command Line Interface (CLI)** application designed to automate order placement on the **Binance Futures Testnet**.  
This project demonstrates **modular backend design, API automation, strict validation, and production-style logging**.

---

## 🖼️ Project Overview

This trading bot allows users to place **Market** and **Limit** orders securely through the Binance Futures API using a CLI interface.  
It ensures that invalid inputs never reach the API, reducing execution errors and improving reliability.

---

## 🧭 Purpose

The **Binance Futures Trading Bot** was developed to:
- Automate repetitive trading actions
- Safely interact with external APIs
- Demonstrate clean Python architecture for real-world backend systems
- Maintain audit-ready logs for every transaction

This project focuses on **backend reliability, validation, and automation**, not manual UI interaction.

---

## 🧰 Tech Stack

- **Python 3.x** – Core programming language  
- **python-binance** – Binance Futures API integration  
- **Argparse** – Command-line argument parsing  
- **Logging** – Persistent audit logs (Console + File)  
- **REST APIs** – Secure request-response handling  

---

## 📂 Project Structure

The application follows a **modular and scalable architecture**:

```

binance-futures-trading-bot/
│
├── bot/
│   ├── client.py          # Binance API client (Singleton Pattern)
│   ├── orders.py          # Market & Limit order execution logic
│   ├── validators.py      # Input validation layer
│   ├── logging_config.py  # Centralized logging configuration
│
├── cli.py                 # CLI entry point (argparse-based)
├── requirements.txt       # Project dependencies
├── trading_bot.log        # Auto-generated audit log file
└── README.md

````

---

## 🛠️ Technical Workflow

### 1. Input Validation Layer
Before placing any order, the system validates:
- **Trading Symbol Format** (e.g., `BTCUSDT`)
- **Order Side** (`BUY` / `SELL`)
- **Order Type** (`MARKET` / `LIMIT`)
- **Quantity Checks** (no zero or negative values)
- **Price Enforcement** (mandatory only for LIMIT orders)

This prevents unnecessary API failures and invalid trades.

---

### 2. Order Execution & API Automation
- Orders are executed on the **Binance Futures Testnet**
- Supports:
  - 📈 Market Orders (instant execution)
  - 📉 Limit Orders (price-based execution)
- Captures full JSON responses from the Binance API

---

### 3. Logging & Error Handling
- All actions are logged in `trading_bot.log`
- Logs include:
  - Order ID
  - Order status
  - Quantity and price
  - API error messages (if any)
- Graceful handling of:
  - Permission errors
  - Notional value errors
  - Invalid request formats

---

## ✨ Key Highlights & Learnings

- ✅ Implemented **production-style logging**
- ✅ Designed a **clean CLI-based backend tool**
- ✅ Worked with **real-world financial APIs**
- ✅ Applied **modular Python architecture**
- ✅ Improved understanding of **API validation & error handling**

---

## ⚙️ How to Use

### 1️⃣ Install Dependencies
```bash
python -m pip install -r requirements.txt
````

---

### 2️⃣ Place a Market Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002
```

---

### 3️⃣ Place a Limit Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 80000
```

---

## 💡 Business & Practical Impact

* Eliminates manual trading errors
* Demonstrates backend automation skills
* Shows real-world API integration capability
* Can be extended to:

  * Trade history tracking
  * Strategy-based execution
  * Scheduler-based automation

---

## 📧 Contact

👩‍💻 **Arti Chaudhari** 🎓 BE Graduate '25 | Aspiring Data Analyst  
📩 Email: [chaudhariarti2146@gmail.com](mailto:chaudhariarti2146@gmail.com)  
🌐 GitHub: [github.com/artichaudhari](https://github.com/artichaudhari)  
💼 LinkedIn:  https://www.linkedin.com/in/arti-chaudhari-b998a82a9/

---
⭐ **If you found this project helpful, don’t forget to star the repo!**
## 📧 Contact

👩‍💻 **Arti Chaudhari**
🎓 BE Graduate '25 | Aspiring Data Analyst / Python Developer

📩 Email: [chaudhariarti2146@gmail.com](mailto:chaudhariarti2146@gmail.com)
🌐 GitHub: [https://github.com/artichaudhari](https://github.com/artichaudhari)
💼 LinkedIn: [https://www.linkedin.com/in/arti-chaudhari-b998a82a9/](https://www.linkedin.com/in/arti-chaudhari-b998a82a9/)

---

⭐ **If you found this project useful, don’t forget to star the repository!**

```


