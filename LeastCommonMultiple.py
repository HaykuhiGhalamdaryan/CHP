def find_lcm(a, b):
    lcm = max(a, b)
    
    while lcm % a != 0 or lcm % b != 0:
        lcm += max(a, b)
    
    return lcm

a = int(input("Enter number1. "))
b = int(input("Enter number2. "))

lcm = find_lcm(a, b)
print(f"The least common multiple of {a} and {b} is {lcm}.")