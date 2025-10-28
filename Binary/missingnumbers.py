def missingnumbers(nums):
    nums.sort()
    for num in range(len(nums) + 1):
        if num not in nums:
            return num
    return len(nums)


# Example usage:
if __name__ == "__main__":
    sample_nums = [3, 0, 1]
    print(f"The missing number in {sample_nums} is: {missingnumbers(sample_nums)}")