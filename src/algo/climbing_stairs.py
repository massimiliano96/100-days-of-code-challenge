# Climbing Stairs
# You are climbing a staircase.It takes n steps to reach the  top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

def climbing_stairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    one_back = 2
    two_back = 1
    for _ in range (2,n):
        next_step = one_back + two_back
        two_back = one_back
        one_back = next_step
    
    return one_back

    

    