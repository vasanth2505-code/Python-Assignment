#Q1. Write a program to check whether a number entered is three digit number or not.

num = int(input("Please enter a number: "))
if len(str(num)) ==3:
     print("True")
else:
    print("False")