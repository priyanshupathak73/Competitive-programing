A = int(input("Enter an integer: "))
original = A
reverse = 0

while A > 0:
    digit = A % 10
    reverse = reverse * 10 + digit
    A //= 10

if original == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")