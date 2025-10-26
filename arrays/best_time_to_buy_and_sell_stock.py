def bruteforce(prices):
    max_profit = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit
    return max_profit

def maxProfit(prices):
    lowest = float('inf')
    maxGain = 0
    for price in prices:
        if price < lowest:
            lowest = price
        elif maxGain < price - lowest:
            maxGain = price - lowest
    return maxGain

prices = [7, 1, 5, 3, 6, 4]
print(bruteforce(prices))  # Output: 5
print(maxProfit(prices))    # Output: 5