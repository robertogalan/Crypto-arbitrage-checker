import asyncio
import ccxt.async_support as ccxt
import time
import os

exchange_names = ['binance', 'coinbase', 'kraken', 'bitso', 'bitfinex', 'poloniex', 'bitget', 'bitmex', 'bitstamp', 'bittrex', 'kucoin']
usdc = 'USDC'
update_interval = 2  # seconds


async def find_arbitrage_opportunities():
    # Initialize exchanges
    exchanges = []
    for name in exchange_names:
        exchange = getattr(ccxt, name)()
        await exchange.load_markets()
        exchanges.append(exchange)

    while True:
        # Get ticker prices for USDC across all exchanges
        ticker_prices = {}
        for exchange in exchanges:
            try:
                ticker = await exchange.fetch_ticker(f'{usdc}/USD')
                ticker_prices[exchange.id] = ticker['last']
            except ccxt.errors.ExchangeError:
                pass

        # Check for arbitrage opportunities
        for i in range(len(exchanges)):
            for j in range(len(exchanges)):
                if i != j:
                    exchange1 = exchanges[i]
                    exchange2 = exchanges[j]
                    if exchange1.id in ticker_prices and exchange2.id in ticker_prices:
                        rate1 = ticker_prices[exchange1.id]
                        rate2 = ticker_prices[exchange2.id]
                        if rate1 > rate2:
                            profit_percentage = (rate1 / rate2 - 1) * 100
                            if profit_percentage > 2:
                                print(f"\033[92mArbitrage opportunity found between {exchange1.id} ({rate1}) and {exchange2.id} ({rate2}): {profit_percentage}%\033[0m")
                            else:
                                print(f"Arbitrage opportunity found between {exchange1.id} ({rate1}) and {exchange2.id} ({rate2}): {profit_percentage}%")

        await asyncio.sleep(update_interval)


async def main():
    while True:
        await find_arbitrage_opportunities()
        os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    asyncio.run(main())
