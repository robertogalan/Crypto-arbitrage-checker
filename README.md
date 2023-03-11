# Inter-Exchange Cryptocurrency Arbitrage Opportunity Finder Tool
This Python script uses the ccxt library to check for inter-exchange arbitrage opportunities for the USDC/USD trading pair.

## How it Works
The script connects to various exchanges and fetches the latest ticker prices for USDC/USD pair. It then looks for arbitrage opportunities between the exchanges by comparing the exchange rates. If it finds an arbitrage opportunity, it will output a message to the console.

## Installation

Clone this repository: 
```
git clone https://github.com/robertogalan/inter-exchange-arbitrage-bot.git
```

Install the required packages: 
```
pip install -r requirements.txt
```

Run the script: 
```
python3 app.py
```

## Supported Exchanges
This script will work with any exchange supported by CCXT. This example comes pre configured with the following exchanges:

Binance
Coinbase
Kraken
Bitso
Bitfinex
Poloniex
Bitget
Bitmex
Bitstamp
Bittrex
Kucoin

## Disclaimer
Trading cryptocurrencies involves a high degree of risk. This script is provided for educational and informational purposes only and should not be construed as investment advice. The author and contributors of this script are not responsible for any losses incurred while using this script.

### Use this script at your own risk and always exercise caution when trading cryptocurrencies.



