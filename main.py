with open("Input/Names/invited_names.txt") as names:
    names_list = names.readlines()
with open("Input/Letters/starting_letter.txt") as starting_letters:
    starting_lines = starting_letters.readlines()
print(starting_lines)
for i in range(len(names_list)):
    name = names_list[i].strip()
    path = f"Output/ReadyToSend/{name}.txt"
    print(path)
    f = open(path, "w")
    for line in range(len(starting_lines)):
        if line == 0:
            updated_name_line = starting_lines[line].strip().replace("[name]", name)
            f.write(updated_name_line + "\n")
        else:
            f.write(starting_lines[line].strip() + "\n")

    f.close()

