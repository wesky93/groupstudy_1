
def count(text,word):
  count_let = 0
  for letter in text:
    if letter == word:
      count_let = count_let+1
  print (count_let)

text = "alalpahea"
count(text,"a")