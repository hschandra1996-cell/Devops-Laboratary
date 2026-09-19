import sys

if len(sys.argv) > 1:
    age = int(sys.argv[1])
else:
    age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible. You are 18 or older.")
else:
    print("You are not eligible. You are under 18.")