import re

filename = 'input.txt'
input = open(filename, 'r')
orig_data = input.read()
stripped_data = re.sub("[A-Za-z]", "", orig_data)
array_strings = stripped_data.split('\n')
first_last = []
for x in array_strings:
    new_val = x[0] + x[-1]
    first_last.append(new_val)
print(first_last)
result = 0
error_letter = []
for i in first_last:
    if len(i) == 1:
        i += i
        result += int(i)
    if len(i) == 2:
        result += int(i)
    else:
        error_letter.append(int(i))
print(result)
print(error_letter)
input.close()
