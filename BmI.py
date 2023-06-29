height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))
BMI = weight / (height/100)**2
print(f"You BMI is {BMI}")

if BMI < 18:
    print("Underweight")
elif BMI >= 18.1 <29:
    print("Normalweight")
elif BMI >= 29.1 <34:
    print("overweight")
elif BMI >=34:
    print("Obese")
