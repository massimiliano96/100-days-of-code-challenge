from src.algo.best_time_to_buy_and_sell_stock import Solution

def test1():
    prices = [7,1,5,3,6,4]
    sol = Solution()
    assert sol.maxProfit(prices) == 5
    
def test2():
    prices = [7,6,4,3,1]
    sol = Solution()
    assert sol.maxProfit(prices) == 0