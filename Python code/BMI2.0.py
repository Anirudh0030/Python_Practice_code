# Enter your height in meters e.g., 1.55
height = float(input("what is your height? "))
weight = int(input("Please enter you weight? "))
bmi = weight / (height * height)
if bmi < 18.5:
    print(f" You BMI is {bmi} You are underweight. ")
elif bmi < 25:
     print(f" You BMI is {bmi} You have a normal weight. ")
elif bmi < 30:
     print(f" You BMI is {bmi} You are slightly overweight. ")
elif bmi < 35:
     print(f" You BMI is {bmi} You are obese. ")
else:
 print(f" You BMI is {bmi} You are clinically obsese. ")   

