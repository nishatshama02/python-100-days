# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


left_years= 90-int(age)
days= int(left_years)*365
weeks= int(left_years)*52
months= int(left_years)*12

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
