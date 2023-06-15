#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary


a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
new_dict = update_dictionary(a_dictionary, 'meme', "Python")
print(new_dict)
print("--")
#print(update_dictionary(a_dictionary))
