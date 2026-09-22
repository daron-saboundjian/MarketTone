from stock_utils import format_stock


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
    result = format_stock(ticker, stocks[ticker]["price"])
    print(result)

