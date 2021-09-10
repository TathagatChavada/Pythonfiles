# Create a .txt file
f = open('Result.txt','w')

# Enter details for your result
name = input("Enter your name: ")
roll_no = int(input("Enter your roll number: "))

print('\n')
print('________________Enter marks out of 100________________')

Physics = int(input("Enter your marks in Physics: "))
Chemistry = int(input("Enter your marks in Chemistry: "))
Maths = int(input("Enter your marks in Maths: "))
Cs = int(input("Enter your marks in Cs: "))
English = int(input("Enter your marks in English: "))

# Line 18 to total and precentage
Total = (Physics + Chemistry + Maths + Cs + English)
Percentage = (Total/500)*100
x = ''

if Percentage >= 25:
    x ='Pass'

else:
    x = 'Fail'
    
# Layout of your result
f.writelines('_______________________________________________'+ '\n'
'Name: ' + str(name) + '\t\t\t\t'
'Roll No: ' + str(roll_no)+ '\n'
'_______________________________________________'+ '\n'
'Physics: ' + str(Physics)+ '\n\n'
'Chemistry: ' + str(Chemistry)+ '\n\n'
'Maths: ' + str(Maths)+ '\n\n'
'Cs: ' + str(Cs)+ '\n\n'
'English: ' + str(English)+ '\n\n'
'_______________________________________________'+ '\n'
'Total: ' + str(Total) + '\t\t\t\t'
'Percentage: ' + str(Percentage) + ' % ' + str(x) + '\n'
'_______________________________________________'+ '\n\n\n')

# Closing the file
f.close()