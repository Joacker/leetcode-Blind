def hammingWeight(n):
    ans = 0
    
    while n!=0:
        ans += 1 
        print(n)
        n = n & (n - 1)
    return ans

print(hammingWeight(11))  # Output: 3