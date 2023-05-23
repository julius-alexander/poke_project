input_file = "saveFileTemp.txt"
output_file = "saveFileOutput.txt"

i = 0

# with open(input_file) as f1:
#     for line in f1:
#         row = line.split(",")
#         for stat in row:
#             print(stat)
#
#         print(line, end="")
#
# print("\n*************************")

# name,level,nature,hpIV,ev,atkIV,ev,defIV,ev,spatkIV,ev,spdefIV,ev,spdIV,ev,isShiny

saved_party = []


def loadSave():
    with open(input_file) as f1:
        for line in f1:
            row = line.split(",")
            saved_party.append(row)


def saveGame():
    pass


loadSave()

for poke_stat in saved_party:
    print(poke_stat)

# make a new pokemon via nane
#   poke_mon = Pokemon()