angA = int(input("Enter your degree A :"))
angB = int(input("Enter your degree B :"))
angC = int(input("Enter your degree C :"))

if(angA == 90 or angB == 90 or angC == 90 ):
    print("It's a right angle")
elif(angA > 90 or angB > 90 or angC > 90):
    print("It's a obtus angle")
else:
    print("its a acute angle")