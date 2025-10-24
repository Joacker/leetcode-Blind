# [2,7,11,15], target=9 => Output: [0,1]

def twosumBruteForce(arr, target):
  for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
      if arr[i] + arr[j] == target:
        return [i, j]
  return []

def twosumHashMap(nums, target):
    mem = dict()
    for i in range(len(nums)):
        if target-nums[i] in mem:
            return [mem[target-nums[i]], i]
        mem[nums[i]] = i
    return []


arr = [2, 7, 11, 15]
target = 9
print(twosumBruteForce(arr, target))  # Output: [0, 1]
print(twosumHashMap(arr, target))    # Output: [0, 1]
