# Binance Futures Trading Bot - Internshala Assignment

A robust, modular Python CLI tool designed to interact with the Binance Futures Testnet API. This bot supports placing Market and Limit orders with built-in validation and logging.

## 📂 Project Structure
As per the assignment requirements, the project follows a modular structure:
- `bot/client.py`: Handles Binance API client initialization.
- `bot/orders.py`: Contains logic for placing Market and Limit orders.
- `bot/validators.py`: Validates user inputs (symbol, quantity, price) before execution.
- `bot/logging_config.py`: Configures file and console logging for audit trails.
- `cli.py`: The main entry point using `argparse` for terminal commands.

## ⚙️ Setup Instructions
1. **Install Requirements**:
   ```bash
   python -m pip install -r requirements.txt