# slice:grab data

greeting = "hello world"
print(len(greeting))  # count from 1

# access position from 0

print(greeting[10])  # use index to give one bin in the Sequence
# get back is a string



#b = a[i:j]   表示复制a[i]到a[j-1]，以生成新的list对象

# [ start:stop: step]
print(greeting[6:11]) #count from 1 # there is:,  so it is slicing

start=6
stop=10
print(greeting[start:stop])
print(greeting[:])#give back all
print(greeting[:6])#包括空格
print(greeting[5:])
print(greeting[6:])



left= "hello"
right= "world"
print(left+right)
print(left+" "+right)

phrase="hello my fellow humans"# white space is also a char
newphrase="3"
for char in phrase:
    newphrase=newphrase+char.upper()
print(newphrase)
print(phrase)


phrase="hello my fellow humans"# white space is also a char
words=phrase.split()
for one_word_str in words:
    print(one_word_str )

