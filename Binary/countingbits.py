# Hay que usar el modulo
def coutBits(n):
    dp = [0] * (n + 1)
    offset = 1
    
    for i in range(1, n + 1):
        if offset * 2 == i:
            offset = i
        dp[i] = 1 + dp[i - offset]
        
    return dp

def countBits(n):
    result = [0]
    for i in range(1, n+1):
        result.append(result[i // 2] + (i % 2))
    return result

print(countBits(5))