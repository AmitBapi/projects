print ("welcome To The Tip Calculator")
bill = int(input("what was the total bill : $"))
tip = int(input("How much tip would you like to give : $"))
count_people = int(input("How many people to split the bill : "))
splitted_bill = (bill+tip)/count_people
print(f"Each person should pay : ${splitted_bill}")
