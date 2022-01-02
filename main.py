# Write a program to generate COMPLEX PASSWORD for a user having following functionality
#  Able to generate simple password as well as complex password
#  Min Length and Max Length
#  Number of lower case characters (min, max)
#  Number of upper case characters (min, max)
#  Number of numerics (min, max)
#  Number of special characters (min, max)
import random

lower_case_character_min = int(input("Enter Min Len of lower case: "))
lower_case_character_max = int(input("Enter Max Len of lower case: "))

upper_case_character_min = int(input("Enter Min Len of upper case: "))
upper_case_character_max = int(input("Enter Max Len of upper case: "))

numeric_min = int(input("Enter Min Len of numeric: "))
numeric_max = int(input("Enter Max Len of numeric: "))

special_min = int(input("Enter Min Len of special character: "))
special_max = int(input("Enter Max Len of special character: "))

pass_len_min = int(lower_case_character_min) + int(upper_case_character_min) + int(numeric_min) + int(special_min)
maxx = int(lower_case_character_max) + int(upper_case_character_max) + int(numeric_max) + int(special_max)
print("Your minimum password limit would be: ", pass_len_min)
print("Max password length should no be greater than: ", maxx)
max_inp = int(input("Please enter max password length: "))

lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'w', 'x', 'y', 'z']
upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
              'V', 'W', 'X', 'Y', 'Z']
numeric = [1, 2, 3, 4, 5, 6, 7, 8, 9]
special_char = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '[', '}', '}', '|',
                '\\', ':', ';', '"', ',']

print("password length in between ->  ", pass_len_min, " : ", max_inp)

random.shuffle(lower_case)
random.shuffle(upper_case)
random.shuffle(numeric)
random.shuffle(special_char)
pass_lower = lower_case[:(random.randrange(lower_case_character_min, lower_case_character_max))]
pass_upper = upper_case[:(random.randrange(upper_case_character_min, upper_case_character_max))]
pass_num = numeric[:(random.randrange(numeric_min, numeric_max))]
pass_spec = special_char[:(random.randrange(special_min, special_max))]
final_pass_list = []

lower_case_min_criteria = pass_lower[:lower_case_character_min]
upper_case_min_criteria = pass_upper[:upper_case_character_min]
num_min_criteria = pass_num[:numeric_min]
spe_min_criteria = pass_spec[:special_min]

extra_list = []

for i in lower_case_min_criteria:
    if i in pass_lower:
        pass_lower.remove(i)
extra_list.extend(pass_lower)

for i in upper_case_min_criteria:
    if i in pass_upper:
        pass_upper.remove(i)
extra_list.extend(pass_upper)

for i in num_min_criteria:
    if i in pass_num:
        pass_num.remove(i)
extra_list.extend(pass_num)

for i in spe_min_criteria:
    if i in pass_spec:
        pass_spec.remove(i)
extra_list.extend(pass_spec)

ran = random.randint(0, max_inp - pass_len_min)
ex = extra_list[0:ran]

final_pass_list.extend(lower_case_min_criteria)
final_pass_list.extend(upper_case_min_criteria)
final_pass_list.extend(num_min_criteria)
final_pass_list.extend(spe_min_criteria)
final_pass_list.extend(ex)

random.shuffle(final_pass_list)

password = ''
for index in final_pass_list:
    password += str(index)
print('password is: ', password)
print(len(password))