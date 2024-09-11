a = int(input("Enter number1. "))
b = int(input("Enter number2. "))

for i in range(min(abs(a), abs(b)), 0, -1):
    if abs(a) % i == 0 and abs(b) % i == 0:
        print(i)
        break
    
