import json

stock_data = {
    "ticker" : "SPCX",
    "company" : "SpaceX",
    "price" : 150.50
}

print(f'{stock_data["company"]}, ticker {stock_data["ticker"]}, is trading at ${stock_data["price"]:.2f}')

JSON_str = '{"ticker": "SPCX", "company": "SpaceX", "price": 150.50}'

result = json.loads(JSON_str)
print(result)


