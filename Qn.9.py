#Q9 Write a program to whether a number (accepted from user) is divisible by 2 and 3 both.

num = int(input("Please enter a number: "))

if num%6==0:
    print("{} is divisible by both 2 and 3".format(num))
else:
    print("{} is not divisible by both 2 and 3".format(num))