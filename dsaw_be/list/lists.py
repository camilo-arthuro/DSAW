print("9.15.2. Exercise")
# Write a function called is_anagram that takes two strings
# and returns True if they are anagrams.
def is_anagram(first_word, second_word):
    list_one = sorted(first_word)
    list_two =sorted(second_word)
    return list_one == list_two

a_anagram = "stop"
b_anagram = "tops"
answer_anagram = is_anagram(a_anagram, b_anagram)
print(f"Are {a_anagram} and {b_anagram} anagrams? {answer_anagram}")

print("9.15.3. Exercise")
# Write a function called is_palindrome that takes a string argument
# and returns True if it is a palindrome and False otherwise.
def is_palindrome(palindrome):
    word_reversed = ''.join(reversed(palindrome))
    return palindrome == word_reversed

a_palindrome = "parrot"
b_palindrome = "rotator"
answer_a_palindrome = is_palindrome(a_palindrome)
answer_b_palindrome = is_palindrome(b_palindrome)
print(f"Is {a_palindrome} a palindrome? {answer_a_palindrome}")
print(f"Is {b_palindrome} a palindrome? {answer_b_palindrome}")

print("9.15.4. Exercise")
# Write a function called reverse_sentence that takes as an argument a string that contains
# any number of words separated by spaces. It should return a new string that contains the same
# words in reverse order. For example, if the argument is “Reverse this sentence”, the result
# should be “Sentence this reverse”.

# Hint: You can use the capitalize methods to capitalize the first word and convert the other
# words to lowercase.
def reverse_sentence(sentence):
    new_sentence = sentence.split()
    sentence_changed = ' '.join(reversed(new_sentence))
    return sentence_changed.capitalize()

original_sentence = "Reverse this sentence"
other_sentence = reverse_sentence(original_sentence)
print(f"The original sentence is '{original_sentence}' and the reverse sentence is '{other_sentence}'")

print("9.15.5. Exercise")
# Write a function called total_length that takes a list of strings and returns
# the total length of the strings.

def total_length(string_list):
    total = 0
    for i in string_list:
        word_len = len(i)
        total = total + word_len
    return total

sentence_list = ['apple', 'banana', 'grapes']
result_total_lenght = total_length(sentence_list)
print(f"List: {sentence_list}")
print(f"The total length of the strings is {result_total_lenght}")