with open("rosalind_gc.txt") as file:
    f = file.read()
list_file = f.split(">")
list_file.remove("")
names = [elem[:13] for elem in list_file]
clean = [elem.replace(elem[:13], "") for elem in list_file]
clean = [elem.replace("\n", "") for elem in clean]
content = [(elem.count("C") + elem.count("G"))/len(elem) * 100 for elem in clean]
content = [round(elem, 3) for elem in content]

idx = content.index(max(content))

result_name = names[idx]
result_content = content[idx] # Ensure I pick the same element

print(result_name)
print(result_content)