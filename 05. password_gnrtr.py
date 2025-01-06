import random

print("Generate Your Own Random Password")
num = int(input("how many numbers you want in the password: \n"))
letters = int(input("how many letters you want in the password: \n"))
special = int(input("how many special characters you want in the password: \n"))

num_ls = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
letters_ls = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p","q",
            "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F","G", "H",
            "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
special_ls = ["~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "|", "\\", "?", "<", ">", "/"]

password_ls=[]

for i in range(0,num):
    password_ls.append(random.choice(num_ls))

for i in range(0, letters):
    password_ls.append(random.choice(letters_ls))

for i in range(0, special):
    password_ls.append(random.choice(special_ls))

print(password_ls)
random.shuffle(password_ls)

password = ""
for i in password_ls:
    password += i
print("Your generated password is: ", password)