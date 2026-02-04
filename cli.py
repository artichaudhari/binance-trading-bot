import argparse
import logging
from bot.client import get_binance_client
from bot.orders import place_futures_order
from bot.validators import validate_order_input
from bot.logging_config import setup_logging

# Initialize logging setup
setup_logging()

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot CLI")
    parser.add_argument("--symbol", type=str, required=True, help="e.g., BTCUSDT")
    parser.add_argument("--side", type=str, required=True, choices=['BUY', 'SELL'])
    parser.add_argument("--type", type=str, required=True, choices=['MARKET', 'LIMIT'])
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float, help="Required for LIMIT orders")

    args = parser.parse_args()

    # 1. Validate Input
    is_valid, error = validate_order_input(args.symbol, args.side, args.type, args.quantity, args.price)
    if not is_valid:
        print(f"Validation Error: {error}")
        return

    # 2. API Credentials (Indented correctly inside main)
    API_KEY = "sBdCowpoOvtmJqvTQvMYVIg5DtUzfyohgDdv9iiNsq2rmi2We9jSUpwu2IVfcoul"
    API_SECRET = "UdiMEr5cgc8N3Jo7EQ4VRnsu2zuv6bj8RawgQhfD4t8aQFfs4P9dQ45mBtETqNUS"
    
    client = get_binance_client(API_KEY, API_SECRET)

    # 3. Execution
    print(f"\nSummary: {args.side} {args.quantity} {args.symbol} ({args.type})")
    response = place_futures_order(client, args.symbol, args.side, args.type, args.quantity, args.price)

    if response:
        print("--- Order Successfully Placed ---")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print(f"Avg Price: {response.get('avgPrice', 'N/A')}")
    else:
        print("--- Order Placement Failed ---")
        print("Check 'trading_bot.log' for details.")

if __name__ == "__main__":
    main()