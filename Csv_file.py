import csv

def Create_CSVfile():
    f = open('Records.csv', 'w', newline='')
    x = csv.writer(f,delimiter=',')

    roll_no = int(input('Enter the Roll No. of Student: '))
    name = input('Enter the Name of Student: ')
    marks = int(input("Enter Student's Marks in CS Subject: ")) 

    stu = [roll_no, name, marks]   

    x.writerow(stu)
    f.close()


def Append_CSVfile():
    f = open('Records.csv', 'a', newline='')
    x = csv.writer(f,delimiter=',')

    roll_no = int(input('Enter the Roll No. of Student: '))
    name = input('Enter the Name of Student: ')
    marks = int(input("Enter Student's Marks in CS Subject: ")) 

    stu = [roll_no, name, marks]   

    x.writerow(stu)
    f.close()

def Read_CSVfile():
    f = open('Records.csv')
    x = csv.reader(f)

    for i in x:
        print(i)
    
ans = 'y'

while ans =='y' or ans =='Y':
    print('\t1. Create a CSV File.\n'
          '\t2. Append in the existing binary file.\n'
          '\t3. Read the CSV file.')

    choice = int(input('Enter your choice: '))

    if choice == 1:
        Create_CSVfile()

    elif choice == 2:
        Append_CSVfile()

    elif choice == 3:
        Read_CSVfile()

    else:
        print('Invalid choice....')

    ans = input('You want to run again (y or Y): ')