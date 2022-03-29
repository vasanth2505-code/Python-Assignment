# Q7. Write a program to check whether a number is even or odd.

a = int(input("Please enter a number:"))

if a%2==0:
    print("{} is Even".format(a))
else:
    print("{} is odd".format(a))