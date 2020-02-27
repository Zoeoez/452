# count
# 1.establish your base，outside of and before any for loop
# 2.do a for loop
# 3.do stuff
# 4.increment your counter
# 5.secret last step,print the value,outside of the loop

count = 0  # step 1

for character in "cats" :  # step 2
    # do stuff,step 3
    count = count + 1  # step 4

print(count)

count = 0

for character in "hello world".split() :
    count = count + 1
print(count)

# accumlator: sum up the value
# 1.establish your base,often 0
# 2.for loop
# 3.do your stuff
# 4.determine which variable has the value you want to add in

total = 0

for num_of_cats in [1, 0, 0, 0, 0, 2, 2]:
    # do stuff
    # determine which variable has the value you want to add in
    total = num_of_cats + total
print(total)

total = 0

for num_of_cats in [1, 0, 0, 0, 0, 2, 2]:
    recalculated_cat = num_of_cats*1.1
    # do stuff
    # determine which variable has the value you want to add in
    total = recalculated_cat + total
print(total)


data = [1, 0, 0, 0, 0, 2, 2]  # this is a list
count = 0  # 1counter
total_cats = 0  # 1 accumulator
for num_cats in data :  # this data is a list of numbers#2 2counter
    # do stuff #3 counter
    count = count + 1  # 4 counter 循环次数算count
    total_cats = total_cats + num_cats

print(count, total_cats, "average", total_cats / count)


