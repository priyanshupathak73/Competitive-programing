n = int(input("enter a no. :"))

for i in range (1, n + 1):
    for j in range(0,+ i ):
        if (j%2==0):
            print("*", end=" ")
        else:
            print(j, end=" ")
    print()

