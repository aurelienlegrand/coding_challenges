from max_profit import max_profit

def test_simple():
    stocks = [1, 2, 3, 4]
    assert (max_profit(stocks) == [1, 4])

def test_empty():
    stocks = []
    assert (max_profit(stocks) == [])

def test_one_elt():
    stocks = [1]
    assert (max_profit(stocks) == [1, 1])

def test_medium():
    stocks = [5, 10, 2, 5]
    assert (max_profit(stocks) == [5, 10])

def test_medium2():
    stocks = [5, 10, 2, 5, 14]
    assert (max_profit(stocks) == [2, 14])