# Create a .txt file
f = open('Result.txt','a')

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
f.write('_______________________________________________'+ '\n')
f.write('Name: ' + str(name) + '\t\t\t\t')
f.write('Roll No: ' + str(roll_no)+ '\n')
f.write('_______________________________________________'+ '\n')
f.write('Physics: ' + str(Physics)+ '\n\n')
f.write('Chemistry: ' + str(Chemistry)+ '\n\n')
f.write('Maths: ' + str(Maths)+ '\n\n')
f.write('Cs: ' + str(Cs)+ '\n\n')
f.write('English: ' + str(English)+ '\n\n')
f.write('_______________________________________________'+ '\n')
f.write('Total: ' + str(Total) + '\t\t\t\t')
f.write('Percentage: ' + str(Percentage) + ' %' + '\n')
f.write('_______________________________________________'+ '\n\n\n')

# Closing the file
f.close()