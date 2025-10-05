"""
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "Score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass
"""

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
print (data)

nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# nato_dict = data.to_dict()
print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Please type your name: \n").upper()
user_name = [letter for letter in user_input]
print(user_name)

# your_name_code = []
# method 1
# for char in user_name:
#     for (key, value) in nato_dict.items():
#         if char == key:
#             your_name_code.append(value)

# method 2
# [your_name_code.append(value) for char in user_name for(key, value) in nato_dict.items() if char ==
# key]

# method 3
your_name_code = [nato_dict[letter] for letter in user_name]
print(your_name_code)


