#PE9
count=0
phrase=input("Please enter the phrase you want to count:",)
words=phrase.split()
for one_word_str in words:
    count=count+1
print(count)

# I first set a count and then input the phrase that I want to count.
# I use phrase.split to make the phrase separate as words. Then in the loop, since I want to count words in phrase,
# I just use count=count+1 to get the loop times.
