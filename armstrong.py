print("Write a program to check weather the entered number is armstrong num or not")
n=int(input("enter number of digit you want to print:"))
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** n
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
