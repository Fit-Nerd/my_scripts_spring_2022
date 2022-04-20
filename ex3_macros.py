weight = input("What is your weight in pounds?")
protein = 2* (int(weight)/2.2)
clean_protein = round(protein, 2)
fat = .8 * (int(weight)/2.2)
clean_fat = round(fat, 2)

height = input("What is your height in inches?")

age = input("What's your age in years?")

sex = input("Are you M or F?")

if sex in ["M", "m", "male", "man", "Male", "Man"]:
    bmr = 88.362 + (13.397 * (int(weight)/2.2)) + (4.799 * (int(height) * 2.54)) - (5.677 * int(age))
else:
    bmr = 447.593 + (9.247 * (int(weight)/2.2)) + (3.098 * (int(height) * 2.54)) - (4.330 * int(age))

clean_bmr = round(bmr, 2)
carb = (clean_bmr - ((protein * 4) + (fat*9)))/4
clean_carb = round(carb, 2)
print("Your bmr is " + str(clean_bmr))
print("Your recommended protein intake is: " + str(clean_protein))
print("Your recommended fat intake is: " + str(clean_fat))
print("Your recommended carb intake is: " + str(clean_carb))
    

# BMR = 88.362 + (13.397 x weight in kg) + (4.799 x height in cm) – (5.677 x age in years)
# BMR = 447.593 + (9.247 x weight in kg) + (3.098 x height in cm) – (4.330 x age in years)