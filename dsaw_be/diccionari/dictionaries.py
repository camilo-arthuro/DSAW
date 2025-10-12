print("10.11.3. Exercise")
# Write a function named has_duplicates that takes a sequence – like a list or string – as a parameter
# and returns True if there is any element that appears in the sequence more than once.
def has_duplicates(sequence):
    new_dic={}
    result=False
    for i in sequence:
        if i in new_dic:
            result=True
        new_dic[i]=True
    return result

first_word='unpredictably'
second_word='wednesday'
first_answer=has_duplicates(first_word)
second_answer=has_duplicates(second_word)
print(f"Do the word {first_word} has duplicates? {first_answer}")
print(f"Do the word {second_word} has duplicates? {second_answer}")

print("10.11.4. Exercise")
# Write a function called find_repeats that takes a dictionary that maps from each key to a counter,
# like the result from value_counts. It should loop through the dictionary and return a list of keys
# that have counts greater than 1. You can use the following outline to get started.
def find_repeats(counter):
    """Makes a list of keys with values greater than 1.

    counter: dictionary that maps from keys to counts

    returns: list of keys
    """
    list = []
    for i in counter:
        if counter[i] > 1:
            list.append(i)
    return list
counter = {'b': 1, 'r': 2, 'o': 2, 'n': 1, 't': 1, 's': 2, 'a': 1, 'u': 2}
repeats_result = find_repeats(counter)
print(f"Values greater than 1 {repeats_result}")

print("10.11.5. Exercise")
# Suppose you run value_counts with two different words and save the results in two dictionaries.
# Each dictionary maps from a set of letters to the number of times they appear. Write a function
# called add_counters that takes two dictionaries like this and returns a new dictionary that contains
# all of the letters and the total number of times they appear in either word.
def value_counts(string):
    counter = {}
    for letter in string:
        if letter not in counter:
            counter[letter] = 1
        else:
            counter[letter] += 1
    return counter
counter1 = value_counts('brontosaurus')
counter2 = value_counts('apatosaurus')

def add_counters (dic1, dic2):
    new_dic={}
    for i in dic1:
        new_dic[i] = dic1[i]
    for i in dic2:
        if i in new_dic:
            new_dic[i] += dic2[i]
        else:
            new_dic[i] = dic2[i]
    return new_dic

counter3 = add_counters(counter1, counter2)
print(f"1st counter {counter1}")
print(f"2nd counter {counter2}")
print(f"3rd counter {counter3}")