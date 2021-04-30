#This algorithm is to search a word in a text plain file with a long of lines.
 
from itertools import islice
 
try:
   with open("proof") as file:
       search_word = "americatupapa2"
       number = 1000
       contents = list(islice(file,2000))
       del contents[:number]
       for line in contents:
           line = line.replace('\n', '')
           if line == search_word:
               print("word found!")
       print(contents)
except MemoryError:
   print("A fucking memory error appeared")

