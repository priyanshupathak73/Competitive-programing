N = int(input("Enter an integer: "))
count = 0
num = abs(N)

while num > 0:
    count += 1
    num //= 10

if N == 0:
    count = 1

print("Count of digits:", count)