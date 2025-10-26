# Sum of two integers without using + or - operator
def getSum(a,b):
    carry = 0
    while b != 0:
        carry = a & b  # AND operation to find carry bits
        a = a ^ b      # XOR operation to add without carrying
        b = carry << 1 # Shift carry to the left
    return a

print(getSum(3,5))  # Output: 8