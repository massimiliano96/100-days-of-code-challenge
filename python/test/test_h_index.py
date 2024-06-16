from src.algo.h_index import Solution

def test1():
    citations = [3,0,6,1,5]
    sol = Solution()
    assert sol.hIndex(citations) == 3
    
def test2():
    citations = [1,3,1]
    sol = Solution()
    assert sol.hIndex(citations) == 1
    
    