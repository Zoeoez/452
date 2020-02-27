data = [1, 0, 0, 0, 0, 2, 2]  # this is a list
count = 0  # 1counter
total_cats = 0  # 1 accumulator
for num_cats in data :  # this data is a list of numbers#2 2counter
    # do stuff #3 counter
    count = count + 1  # 4 counter 循环次数算count
    total_cats = total_cats + num_cats

print(count, total_cats, "average", total_cats / count)

