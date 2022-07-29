height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

num = float(weight)
denom = float(height)
bmi = (num / (denom ** 2))

print(int(bmi))
