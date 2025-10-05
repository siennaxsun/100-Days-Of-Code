#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# method 1:
with open("./input/letters/starting_letter.txt") as letter:
    letter_contents = letter.read()
    word_list = letter_contents.split()
    print (word_list)
    index_name = word_list.index('[name],')
    print(index_name)
    index_sat = word_list.index('Saturday.')
    index_it = word_list.index('it!')

    with open("./input/names/invited_names.txt") as letter:
        names = letter.read()
        name_list = names.split()
        print(names.split())

        for name in name_list:
            # print(name)
            word_list[index_name] = name + ",\n" + '\n'
            print(word_list)
            word_list[index_sat] = 'Saturday.' + '\n'+ '\n'
            word_list[index_it] = 'it!' + '\n'+ '\n'
            my_string = ' '.join(map(str, word_list))
            with open(f"./output/ReadyToSend/letter_for_{name}.txt", mode = "w") as modified_letter:
                modified_letter.write(my_string)



A = " I like Banana"
A.replace("I", "You")
print(A)

txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)


# method 2
with open("./Input/letters/starting_letter.txt") as letter:
    letter_contents = letter.readlines()
    print(letter_contents)

with open("./Input/names/invited_names.txt") as letter:
    names = letter.read()
    name_list = names.split()
    print(names.split())


for name in name_list:
    new_contents = []
    for i in range(0, len(letter_contents)):
        if '[name]' in letter_contents[i]:
            print(i, letter_contents[i])
            new_content = letter_contents[i].replace('[name]', name)
            print(new_content)
            new_contents.append(new_content)
        else:
            new_contents.append(letter_contents[i])
    print(new_contents)

    with open(f"./Output/ReadyToSend/New_letter_for_{name}.txt", mode="w") as modified_letter:
        modified_letter.write(' '.join(map(str, new_contents)))




# teacher's version
PLACEHOLDER = '[name]'

with open("./Input/names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

with open("./Input/letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    print(letter_contents)

    for name in names:
        striped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, striped_name)
        with open(f"./Output/ReadyToSend/Teacher's_letter_for_{striped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
