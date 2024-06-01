def fibonacci(n):
    ans = [0, 1]
    for x in range(2,n+1):
        ans.append(ans[x-2] + ans[x-1])
    
    return ans[n]