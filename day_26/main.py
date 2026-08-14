import pandas as pd

data = pd.read_csv("day_26/nato_phonetic_alphabet.csv")
df = pd.DataFrame(data)

word_dict = {row.letter : row.code for (index, row) in df.iterrows()}

# word_dict = {
#     letter : desc for letter,desc in df.items()
# }

choice = input("Type : ").upper()
output_list = [word_dict[item] for item in choice]
print(output_list)