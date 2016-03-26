#6_4

text = "banana"
text = text.lower()
abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","x","y","z"]

count = 0

for a in abc:
  if a in text:
    count = count+1
    print (a)

print (count)

