def max_profit(stocks):
    """Computes the maximum benefit that can be done by buying and selling once a stock based on a list of stock values
    O(n) time complexity as we only go through the list of values once"""
    if stocks == []:
        return []

    current_max_profit = 0
    min_stock = stocks[0]
    solution = [stocks[0], stocks[0]]

    for stock in stocks:
        if stock < min_stock:
            min_stock = stock

        if stock - min_stock > current_max_profit:
            current_max_profit = stock - min_stock
            solution = [min_stock, stock]

    return solution


if __name__ == "__main__":
    stocks = [1, 2, 3, 4]

    print(max_profit(stocks))