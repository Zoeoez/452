
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




#PE10
count=0
length=0
phrase=input("Please enter the phrase you want to get the average length:",)
words=phrase.split()
for one_word_str in words:
    count=count+1
    length=length+len(one_word_str)
print(length/count)

# To calculate the average word length in a sentence entered by the user, I need count as count
# and length as accumulator to get the average.
# I use input to get the phrase i want to get the average length and then use phrase.split to get the words.
# In the loop, in order to get the length of the phrase, I add len(one_word_str) to the accumulator to get the sum of  length of each word in the
# phrase. Outside the loop, average is calculated.








