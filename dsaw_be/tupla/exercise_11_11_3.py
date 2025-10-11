print("11.11.3. Exercise")
# Write a function called shift_word that takes as parameters a string and an integer,
# and returns a new string that contains the letters from the string shifted by the
# given number of places.

letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = range(len(letters))
letter_map = dict(zip(letters, numbers))
def shift_word(word, number):
    new_word=""
    new_index=0
    for i in word:
        new_index = (letter_map[i] + number) % 26
        new_word = new_word + ''.join(letters[new_index])
    return new_word

first_word='cheer'
second_word='melon'
first_number=7
second_number=16
first_answer=shift_word(first_word, first_number)
second_answer=shift_word(second_word, second_number)
print(f"Original 1st word: {first_word}. Word shifted: {first_answer}.")
print(f"Original 2nd word: {second_word}. Word shifted: {second_answer}.")