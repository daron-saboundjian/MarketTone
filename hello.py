Tickers = ["NVDA", "AAPL", "GOOG"]
Companies = ["Nvidia", "Apple", "Google"]
Prices = [190.40, 290.25, 300.10]



stocks = {
    "AAPL" :
    {
        "company" : "Apple",
        "price" : 150.90
    },

    "NVDA" :
    {
        "company" : "Nvidia",
        "price" : 399.32
    },

    "GOOG" :
    {
        "company" : "Google",
        "price" : 167.34
    },
}

for ticker in stocks:
    print(f'Ticker {ticker} of {stocks[ticker]["company"]} is trading at ${stocks[ticker]["price"]:.2f}')

