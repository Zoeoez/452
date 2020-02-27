acronym=""
phrase=input("Please enter the phrase:",)
words=phrase.split()
for one_word_str in words:
    first_letter=one_word_str[0]
    acronym=acronym+first_letter
print(acronym.upper())

# I first set an accumulator. This time accumulator is an empty string because I want to add
# first letter of each word to accumulator.  Then I input the phrase and split them to words.
# In the loop, I use one_word_str[0] to get first letter of each word and collect them by adding the first_letter
# to my accumulator. Since the question asks us to get the uppercase, I use acronym.upper.

