from src.algo.best_time_to_buy_and_sell_stock_2 import Solution

def test1():
    prices = [7,1,5,3,6,4]
    sol = Solution()
    assert sol.maxProfit(prices) == 7
    
def test2():
    prices = [7,6,4,3,1]
    sol = Solution()
    assert sol.maxProfit(prices) == 0
    
def test3():
    prices = [1,2,3,4,5]
    sol = Solution()
    assert sol.maxProfit(prices) == 4