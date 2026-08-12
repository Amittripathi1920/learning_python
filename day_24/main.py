# with open("day_24/my_file.txt") as file:
#     content = file.read()
#     print(content)

# with open("day_24/my_file.txt", mode="a") as file:
#     file.write("\nNew Text")
    
# with open("day_24/output/ReadyToSend/rets.txt", mode="a") as file:
#     file.write("\nNew Text")

inivited_members = open("day_24/invited_names.txt")
# print(file.readlines())

letter = open("day_24/input/letter/letter.txt")
letter_data = letter.read()

file_data = inivited_members.readlines()
# print(file_data)

for i in file_data:
    clean_name = i.replace("\n","")
    print(clean_name)
    x = letter_data.replace("[name]", clean_name)
    with open(f"day_24/output/ReadyToSend/letter_for_{clean_name}.txt", "w") as file:
        file.write(x)



inivited_members.close()
letter.close()
