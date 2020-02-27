#D2
s1="spam"
s2="ni!"


#a) "NI"
print((s2.upper()).split("!")[0])



#b)"ni!spamni!"
print(s2+(s1+s2))


#c)"SpamNi! SpamN1! SpamNi!"
print(((s1.capitalize())+(s2.capitalize())+" ")*3)

#d)"spam"
print(s1)

#e) ["sp","m"]
print(s1.split("a"))

#f)
print(s1.split("a")[0]+s1.split("a")[1])

