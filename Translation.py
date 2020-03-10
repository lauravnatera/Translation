import Dictionary

print (Dictionary.d)

text = "She ate tuna in my house"
translate = ""
words = text.split()
for w in words:
    translate = translate + " " + Dictionary.d[w]

print(translate)