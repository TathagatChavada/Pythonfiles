import os
# Working with Binary file
import pickle as p

# Creating a binary file.
def Create_file():
    f = open('bfile.dat','wb')
    
    roll_no = int(input('Enter the Roll No. of Student: '))
    name = input('Enter the Name of Student: ')
    marks = int(input("Enter Student's Marks in CS Subject: "))

    stu = [roll_no, name, marks]
    p.dump(stu,f)
    f.close()

# Appending in a binary file.
def Append_file():
    f = open('bfile.dat','ab')
    
    roll_no = int(input('Enter the Roll No. of Student: '))
    name = input('Enter the Name of Student: ')
    marks = int(input("Enter Student's Marks in CS Subject: "))

    stu = [roll_no, name, marks]
    p.dump(stu,f)
    f.close()

# Reading from a binary file
def Read_file():
    f = open('bfile.dat','rb')
    try:
        while True:
            x = p.load(f)
            print(x)

    except EOFError:
        pass        

# Searching in a binary file
def Search_file():
    f = open('bfile.dat','rb')
    print('1. Search by Roll No.\n'
          '2. Search by Name.\n'
          '3. Search by Marks.')

    Sc = int(input('Enter the way in which you want to search: '))
    
    if Sc == 1:
        R_no = int(input('Enter the Roll no of Student: '))
        try:
            while True:
                x = p.load(f)
                if x[0] == R_no:
                    print(x)
        except EOFError:
            pass        
            
    elif Sc == 2:        
        Name = input("Enter the name of Student: ")
        try:
            while True:
                x = p.load(f)
                if x[1] == Name:
                    print(x)
        except EOFError:
            pass        

    elif Sc == 3:
        Marks = int(input('Enter the Marks of Student: '))
        try:
            while True:
                x = p.load(f)
                if x[2] == Marks:
                    print(x)
        except EOFError:
            pass                    

    else:
        pass


# def Delete_record(rollno):
#     f = open('bfile.dat', 'rb')
#     flag = 0
#     reclst = []
#     try:
#         while True:
#             rec = p.load(f) 
#             reclst.append(rec)

#     except EOFError:
#         pass
#     f.close()
#     print(reclst)

#     file = open('bfile.dat', 'wb')
#     for i in reclst:
#         if i[0] == rollno:
#             flag = 1
#             print('Deleted the record of: ',rollno)
#             continue
#         p.dump(i,file)
#     f.close()

#     if flag == 0:
#         print('Record not found')

def delete_record():
     rno = int(input("Enter a roll no you want to delete:"))
     rfile = open("bfile.dat","rb")
     wfile = open("temp.dat","wb")
     flag =0
     try:
         while True:
             rec = p.load(rfile)
             if rec[0]== rno:
                 flag =1
                 print("record found & deleted.")
                 continue
             else:
                 p.dump(rec,wfile)
     except EOFError:
        pass
     rfile.close()
     wfile.close()
    
     os.remove("bfile.dat")
     os.rename("temp.dat","bfile.dat")
    
     if flag ==0:
        print("Record not found....")

# Controlling the execution of the program
ans = 'y'
while ans =='y' or ans =='Y':
    print('\t1. Create a binary File.\n'
          '\t2. Append in the existing binary file.\n'
          '\t3. Read the binary file.\n'
          '\t4. Search in the binary file.\n'
          '\t5. Delete a record from the binary file.\n')
   

    choice = int(input('Enter your choice: '))

    if choice == 1:
        Create_file()

    elif choice == 2:
        Append_file()

    elif choice == 3:
        Read_file()

    elif choice == 4:
        Search_file()

    elif choice == 5:
        delete_record()
    else:
        print('Invalid choice....')      

    ans = input('You want to run again (y or Y): ')
    