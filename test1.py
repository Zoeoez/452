for ch in "aardvark":
    print(ch)

# print every character in given string



for w in "Now is the winter of our discontent...".split():
    print(w)

# print every word in given string. Last word includes"...".

for w in "Mississippi".split("i"):
    print(w)

# split "i" in  "Mississippi" , "i" here is like a break.


msg=""
for s in "secret".split("e"):
    msg = msg + s
print(msg)

# msg is an empty accumulator. Every time loop adds a character in "secret" except "e" to accumulator.
# In the end, "msg" is got.

msg=""
for ch in "secret":
    msg = msg + chr(ord(ch) + 1)
print(msg)

#The (ord(ch)+1)function returns an integer representing the Unicode character in "secret" plus 1.
#chr() turns the new number into string that it represents. Then it adds the new char to accumulator.

