for i in range(1, 11):
    print(i * i)
# In this loop, from 1 to 11, including integers 1,2,3,4,5,6,7,8,9,10
# are multiplied by themselves and the result of every loop is printed since
# print() is inside the loop

for i in [1, 3, 5, 7, 9]:
    print(i, ":", i ** 3)
print(i)
# In this loop, i is from list which contains five integers 1,3,5,7,9. Every time,
# i is printed and cube of i is also printed.PLUS,when the loop is over，the last i is
# also printed.

x=2
y=10
for j in range(0,y,x):
    print(j,end="")
    print(x+y)
print("done")
# First we take a look at range(0,y,x).This means j starts from 0 to y, not including y
# and each time it will add x to itself.In other word，the step is x.
# In this loop, every time j is printed and (x+y) is printed in the same line.
# x+y is always 12.

ans = 0
for i in range(1, 11):
    ans = ans + i*i
    print(i)
print(ans)
# ans as an accumulator,first equals 0 when it is outside
# the loop. In the loop, i starts from 1 to 11,not including 11. In each loop,
# ans equals ans plus square of i.i is printed after each calculation.
# When loop is over, 10 is printed, which is the last value of i.

