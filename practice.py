weight = 85
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇
if (bmi>=18.5 and bmi<25.0):
    print("normal weight")
elif bmi<18.5:
    print("underweight")
else:
    print("overweight")