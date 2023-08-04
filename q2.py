paragraph=input('type a paragraph:')


words = paragraph.split()
l = []
for word in words:
   if len(word) > 4:
      l.append(word)
print(l)
  
