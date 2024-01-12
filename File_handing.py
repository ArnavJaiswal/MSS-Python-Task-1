# open and read the file
file_path = "/Users/kirthijaiswal/Documents/File Handling/product_descriptions.txt"
with open(file_path, "r") as file:
    descriptions = file.readlines()

# process each line and keep them separate
formatted_descriptions = []
for line in descriptions:
    formatted_line = ' '.join(word.capitalize() for word in line.split())
    formatted_descriptions.append(formatted_line + '\n')  # adding '\n' to keep the lines separate

# write to a new file
with open("formatted_descriptions.txt", "w") as output_file:
    output_file.writelines(formatted_descriptions)

