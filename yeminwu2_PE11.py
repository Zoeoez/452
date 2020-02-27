# first n numbers

total = 0
n=int(input("Enter a number: "))
for num in range(1,n+1):
    total = total + num
print("The sum of N natural numbers is",total)
