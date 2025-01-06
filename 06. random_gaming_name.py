import random
print("RANDOM NAME GENERATOR")
letter_ls =["B", "C", "D","F", "G", "H","J", "K", "L", "M", "N","P",
            "Q", "R", "S", "T","V", "W", "X", "Z", "A", "E", "I", "O", "U", "Y"]
num_ls = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

name = int(input("how many letter you want: \n"))
name_num= int(input("how many num you want: \n"))


word_ls= []
for i in range(name):
    word_ls.append(random.choice(letter_ls))

for i in range(name_num):
    word_ls.append(random.choice(num_ls))

word=""
for i in word_ls:
    word+=i
print(word)

