print("Welcome to the roller coaster ride! ")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You are ready to go!! ")
    age = int(input("What is your age? "))
    if age < 12:
        print("You have to pay $5. ")
    elif age <= 18:
        print("You have to pay $7" )
    elif age >= 45 and age <= 55:
        print("Enjoy the free ride from our end")
    else:
        print("You have to pay $12")  
else:
    print("Better luck next time. ")