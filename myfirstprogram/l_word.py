# This is a program to make a word list of all possible words with a defined length

from itertools import product
import gc

numbers = [str(x) for x in range(0,10)]
minus_alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
mayus_alphabet = [x.upper() for x in minus_alphabet ]
special_characters = ['!', ' ' ,'"','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=','{','}','[',']','|','/',':',';','"','<','>',',','.','?']

possibilities = minus_alphabet + mayus_alphabet + numbers + special_characters

# this makes a word list depending of the length of each word
# @param x -> length of the each word
# @returns list
def mk_wordList(x):
    number = 1
    wordList = {}
    while(number <= x):
        key = str(number)
        wordList.update({key: possibilities})
        number += 1
    return wordList
    
# shows all the possible words in a defined length
# @param x -> defined length
def allPosibilities(x):
    number = 1
    while(number <= x):
        worldList = mk_wordList(number)
        for c in product(*[worldList[k] for k in sorted(worldList.keys())]):
            print(''.join(c))
            gc.collect()
        number += 1
        
allPosibilities(3)




