# Trading Bot - Binance Futures Testnet

## Setup

1. Install dependencies:
   pip install -r requirements.txt

2. Set environment variables:
   export BINANCE_API_KEY=your_key
   export BINANCE_API_SECRET=your_secret

3. Run examples:

### MARKET ORDER
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

### LIMIT ORDER
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000

## Features

- Market & Limit Orders
- BUY / SELL support
- CLI input validation
- Logging to file
- Error handling

## Log File

Check trading_bot.log