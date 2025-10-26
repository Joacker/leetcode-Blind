def mySolution(list):
    list.sort()
    for i in range(len(list) - 1):
        if list[i] == list[i + 1]:
            return True
    return False

def bestSolution(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

print(mySolution([1, 2, 3, 1]))
print(bestSolution([1, 2, 3, 4]))