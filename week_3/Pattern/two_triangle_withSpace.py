rows = int(input("Enter your rows :"))

for i in range (1, rows + 1):
    for j in range(i):
        print("*", end =" ")
    for j in range(2*rows - 2*i):
        print(" ", end = " ")
    for j in range(i):
        print("*", end =" ")
    print()
