year = int(input("Enter your year :"))

if(year % 4 == 0 and year % 100 == 0 and year % 400 == 0):
    print("Your entred year is a leap year")
else:
    print("Your entred year is not a leap year")