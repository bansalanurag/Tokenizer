import re
name = input("File name ?:")
file = open(name,"r",encoding="utf-8")
data = file.read()

nlines = nwords = para = 0

#Paragraphs
para = data.count('\n\n')

#Words
words = data.split()
extra = words.count('!')+words.count('"')+words.count(')')+words.count('(')+words.count(',')+words.count('.')+words.count('-')+words.count('?')+words.count(':')+words.count(";")
nwords = len(words)-extra

#Sentences
match = re.findall('[a-z|A-Z|0-9|)]+[\.|\!|\?][\"|\”|\s|\n|)][A-Z]*',data)
two = re.findall("[A-Z][a-z][\.][\s]",data)
special = re.findall('[A-Z|a-z|0-9][\.][\s]+[a-z]',data)
nlines = len(match)-len(two)-len(special)


print('Number of Paragraphs = %d' %para) #ASSUMPTION
print('Number of Sentences = %d' %nlines)
print('Number of Words = %d' %nwords)

file.close()
