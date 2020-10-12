# 1
Travelling = input("yes or no:- ")

while Travelling == "yes":
    num = int(input("No. of people travelling:- "))

    for num in range(1,num + 1):
        Name = input("Name:- ")

        Age = input("Age:- ")
        Sex = input("Male or Female:- ")
        print(Name)
        print(Age)
        print(Sex)
    Travelling= input("Oops! forgot someone:- ")

