import re

filename = 'input.txt'
input = open(filename, 'r')
orig_data = input.read()
add1 = re.sub("one", "o1ne", orig_data)
add2 = re.sub("two", "tw2o", add1)
add3 = re.sub("three", "th3ree", add2)
add4 = re.sub("four", "fo4ur", add3)
add5 = re.sub("five", "fi5ve", add4)
add6 = re.sub("six", "si6x", add5)
add7 = re.sub("seven", "sev7en", add6)
add8 = re.sub("eight", "eig8ht", add7)
add9 = re.sub("nine", "ni9ne", add8)
add_all_clean = re.sub("[A-Za-z]", "", add9)
# print(add_all_clean)
array_strings = add_all_clean.split('\n')
first_last = []
for x in array_strings:
    new_val = x[0] + x[-1]
    first_last.append(new_val)
print(first_last)
result = 0
error_letter = []
singular_list = []
for i in first_last:
    if len(i) == 1:
        i += i
        result += int(i)
        singular_list.append(int(i))
    if len(i) == 2:
        result += int(i)
    else:
        error_letter.append(int(i))
print(result)
print(singular_list)
# print(error_letter)
input.close()
