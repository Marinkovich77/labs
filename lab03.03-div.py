#This program reads in two numbers 
#and outputs the integer answer and remainder

x = int(input("Enter the number you want to be divided: "))
y = int(input("Enter the number you want to divide by: "))
answer = int(x/y)
remainder = x%y

print("{} divided by {} is {} with remainder {}".format(x, y, answer, remainder))