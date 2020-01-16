from test_framework import generic_test


def buy_and_sell_stock_once(prices):
    min_stock, max_stock, local_delta, abs_delta, stock_count = prices[0], prices[0], 0.0, 0.0, len(prices)

    for i in range(0, stock_count):
        curr = prices[i]

        if i == stock_count - 1:
            return abs_delta

        nxt = prices[i + 1]

        if nxt >= curr:
            max_stock = nxt
            local_delta = max_stock - min_stock
            abs_delta = max(abs_delta, local_delta)
        else:
            min_stock = min(nxt, min_stock)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
