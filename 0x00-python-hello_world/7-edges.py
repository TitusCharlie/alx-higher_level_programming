#!/usr/bin/python3

word = "Holberton"

#contains the firtst 3 words in the variable word
word_first_3 = word[:3]
#contains the last two letters in the variable word
word_last_2 = word[:-2]
#excludes the first and last letters from the variable word
middle_word = word[1:-1]

print(f"The first three letters of the word {word} are: {word_first_3}\nThe last two letters of the word {word} are: {word_last_2}\nand the middle letters of the word {word} are: {middle_word}")
