print("11.11.2. Exercise")
# Write a line of code that appends the value 6 to the end of the second list in t.
# If you display t, the result should be ([1, 2, 3], [4, 5, 6]).

list0 = [1, 2, 3]
list1 = [4, 5]

t = (list0, list1)
print(f"Original tuple: {t}")

t[1].append(6)
print(f"Tuple modified: {t}")

d = {t: 'this tuple contains two lists'}
