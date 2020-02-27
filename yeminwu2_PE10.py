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
# In the loop, in order to get the length of the phrase,
# I add len(one_word_str) to the accumulator to get the sum of  length of each word in the
# phrase. Outside the loop, average is calculated.









