print("9.15.2. Exercise")
# Write a function called is_anagram that takes two strings
# and returns True if they are anagrams.

def is_anagram(first_word, second_word):
    list_one = sorted(first_word)
    list_two =sorted(second_word)
    return list_one == list_two

a_word = "stop"
b_word = "tops"
answer = is_anagram(a_word, b_word)
print(f"{a_word} and {b_word} are anagrams? {answer}")