def acro(input_phrase):
    words =input_phrase.split()
    acronym = ""
    for one_word_str in words :
        first_letter = one_word_str[0]
        acronym = acronym + first_letter
        acronym=acronym.upper()
    return acronym

user_phrase=input("Please enter the phrase:",)
user_phrase=acro(user_phrase)
print(user_phrase)
