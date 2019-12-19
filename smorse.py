# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 12:10:20 2019

@author: goldsche

This contains a function "smorse" that takes string inputs and converts them 
to space-less morse code
"""


# load the standard alphabet into a list
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
            'q','r','s','t','u','v','w','x','y','z']

# load the morse alphabet into a list 
with open('MorseAlphabet.txt') as file:
    morseAlphabet = [letter.replace('\r','').replace('\n','') for letter in file.readlines()]

# load the enable1 word list
with open('enable1.txt') as file:
    words = [word.replace('\r','').replace('\n','') for word in file.readlines()]

# create a function to clean up inputs before they can raise exceptions
def cleaner(dirtyWord):
    cleanWord = ''
    for letter in dirtyWord:
        if letter.lower() not in alphabet:
            pass
        else:
            cleanWord += letter.lower()
    return cleanWord

# convert each letter to a morse letter using map, lambda
# create a string by converting the map object to a list and joining without a spacer
def smorse(word):
    word = cleaner(word)
    morse = map(lambda letter: morseAlphabet[alphabet.index(letter)], word)
    return ''.join(list(morse))

# convert the enable1 word list to smushed morse code
smorsed = list(map(smorse, words))

