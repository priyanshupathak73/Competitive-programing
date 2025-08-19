# for i in range(1,10,2):
#     print(i)

# for i in range(1,10,2):
#     print(i*i, end=" ")


# n = int(input("Enter you no. :"))
# for i in range(1,n+1):
#     print(i, end=" ")

# n = int(input("Enter you no. :"))
# for i in range(1,n+1, 2):
#     print(i, end=" ")


A = int(input("Enter your first no. A: "))
B = int(input("Enter your second no. B: "))

result = 1
for i in range(B):
    result *= A

print("A^B =", result)