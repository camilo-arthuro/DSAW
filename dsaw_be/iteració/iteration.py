print("7.9.3. Exercise")
# Write a function called uses_only that takes a word and a string of letters,
# and that returns True if the word contains only letters in the string.

first_word = 'banana'
second_word = 'apple'
first_available = 'ban'
second_available = 'apl'
def uses_only(word, available):
    result = True
    for i in word:
        if i not in available:
            result = False
    return result

print(f"Word: {first_word}. Available: {first_available}. Result: {uses_only(first_word,first_available)}.")
print(f"Word: {second_word}. Available: {second_available}. Result: {uses_only(second_word,second_available)}")

print("7.9.4. Exercise")
# Write a function called uses_all that takes a word and a string of letters,
# and that returns True if the word contains all of the letters in the string at least once.

first_word = 'banana'
second_word = 'apple'
first_required = 'ban'
second_required = 'api'
def uses_all(word, required):
    result = True
    for i in required:
        if i not in word:
            result = False
    return result

print(f"Word: {first_word}. Available: {first_required}. Result: {uses_all(first_word,first_required)}")
print(f"Word: {second_word}. Available: {second_required}. Result: {uses_all(second_word,second_required)}")