def bruteforce_max_subarray(arr):
    sub = []
    max_sum = float('-inf')
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            # slicing the array from i to j
            current_sub = arr[i:j+1]
            current_sum = sum(current_sub)
            if current_sum > max_sum:
                max_sum = current_sum
                sub = current_sub
    return sub
            

def max_subarray(arr):
    max_sum = float('-inf')
    current_sum = 0
    for i in range(len(arr)):
        current_sum += arr[i]
        if current_sum > max_sum:
            max_sum = current_sum
            sub_end = i
        if current_sum < 0:
            current_sum = 0
            sub_start = i + 1
    return arr[sub_start:sub_end + 1]

print(bruteforce_max_subarray([-2,1,-3,4,-1,2,1,-5,4]))
print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))