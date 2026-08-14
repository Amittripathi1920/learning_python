with open("file1.txt") as file:
    data = file.readlines()
    data_cleaned_file1 = [int(item.replace("\n", "")) for item in data]

with open("file2.txt") as file:
    data = file.readlines()
    data_cleaned_file2 = [int(item.replace("\n", "")) for item in data]

result = [item for item in data_cleaned_file1 if item in data_cleaned_file2 ]

print(result)