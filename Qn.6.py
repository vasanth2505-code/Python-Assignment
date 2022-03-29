# Q6. Write a program to check whether a number (accepted from user) is positive or negative.

a = int(input("Please enter a number:"))

if a==0:
    print("Number is Zero")
elif a<0:
    print("The number you entered is a negative number.")
else:
    print("The number you entered is a positive number.")
