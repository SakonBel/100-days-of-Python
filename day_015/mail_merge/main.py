with open("input/sample.txt") as file:
    lines = file.readlines()


with open("name.txt") as file:
    names = file.readlines()
    name_list = []
    for name in names:
        name_list.append(name.split()[1])

for name in name_list:
    with open(f"output/{name}_mail.txt", mode="w") as file:
        messages = ""
        for line in lines:
            new_line = line.replace("[name]", name)
            messages += new_line
        file.write(messages)
