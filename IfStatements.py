#1
Phone_Balance = 5
Bank_Balance = 150

if Phone_Balance < 7:
    Phone_Balance += 10
    Bank_Balance -=10

print(Phone_Balance, Bank_Balance)

#2
Points = 180

if Points <= 50:
    print("Congratulation! You won the wooden tower.")

elif Points <= 150:
    print("Congratulation! You won the Time Loop tower.")

elif Points <= 180:
    print("Congratulation! You won the Klassic tower.")

else:
    print("Congratulation! You won the Towers of Time.")

#3
Is_male = True
Is_tall = False

if Is_male and Is_tall:
    print("You are a tall male.")

elif Is_male and not(Is_tall):
    print("You are a short male.")

elif not(Is_male) and Is_tall:
    print("You are not a male but are tall.")

else:
    print("You are either not male or not tall or both.")

#4
Weight = 100
Height = 2

if 18.5 <= Weight / Height ** 2 <= 25:
    print("BMI is considered normal.")

else:
    print("You are overweight.")