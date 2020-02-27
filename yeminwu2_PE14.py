total = 0
count=0
for i in range(eval(input("How many times will the loop repeat:"))):
    num = eval(input("Enter numbers you want to add up:"))
    count=count+1
    total = total + num

print("average", total/ count)

