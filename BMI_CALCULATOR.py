height = float(input("Enter your height: "))
weight = int(input("Enter your weight: "))

BMI = round(weight / (height * height) , 2)

if BMI < 18.5:
    print(f"Your bmi is {BMI},You are underweight")
elif BMI < 25:
    print(f"Your bmi is {BMI},You are normal weight")
elif BMI < 30:
    print(f"Your bmi is {BMI},You are slightly overweight")
elif BMI < 35:
    print(f"Your bmi is {BMI},You are obese")
else:
    print(f"Your bmi is {BMI},You are clinically obese")
