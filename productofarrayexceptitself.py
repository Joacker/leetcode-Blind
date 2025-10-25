def bruteforce(nums, output):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                output[i] *= nums[j]
    return output

def productExceptSelf(nums):
    left = [1] * len(nums)
    right = [1] * len(nums)
    output = [1] * len(nums)
    
    # cota de la izquierda
    for i in range(1, len(nums)):
        left[i] = left[i - 1] * nums[i - 1]
    
    # cota de la derecha
    for i in range(len(nums) - 2, -1, -1):
        right[i] = right[i + 1] * nums[i + 1]
        
    # producto de ambos
    for i in range(len(nums)):
        output[i] = left[i] * right[i]

    return output

nums = [1,2,3,4]
output = [1,1,1,1]

print(bruteforce(nums, output))

