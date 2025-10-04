#5-1
song = "That's - a moray!"
print(song.replace("m", "M"))

#5-2
question = "Who are you?"
answer = "I'm Keikouin Yuki."

print("Q :" + question)
print("A :" + answer)

#5-3
things = "aiueo %s"
thing = "kakikukeko"

'%s' % thing
print(things % thing)

#5-4
letter = "Dear {salutation} {name}."

#5-5
print(letter.format(salutation = "hello", name = "pikatyu"))

#5-6
names = ["duck", "groud", "spitz"]
for name in names:
    cap_name = name.capitalize() #capitalize() 　先頭の1文字を大文字にする
    print("%sy Mc%sface" % (cap_name, cap_name))

#5-7
names = ["duck", "groud", "spitz"]
for name in names:
    cap_name = name.capitalize() #capitalize() 　先頭の1文字を大文字にする
    print("{}y Mc{}face".format(cap_name, cap_name))

#5-8
names = ["duck", "groud", "spitz"]
for name in names:
    cap_name = name.capitalize() #capitalize() 　先頭の1文字を大文字にする
    print(f"{cap_name}y Mc{cap_name}face")
