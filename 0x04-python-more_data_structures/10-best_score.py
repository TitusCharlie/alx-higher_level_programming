#!/usr/bin/python3
def best_score(a_dictionary):
    for i in list(a_dictionary):
        if i != a_dictionary:
            return None
        else:
            return max(a_dictionary, a_dictionary.get)


a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))
