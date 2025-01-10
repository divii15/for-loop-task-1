# 6 add number, for example user enter 5, need to add 1 to 5 numbers


b = int(input("Enter a number: "))
num = 0
for i in range(1, b + 1):
    num=num+i
print("The sum of numbers from 1 to",b,"is",num)