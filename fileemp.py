import os

def createfile():
    f1 = open("emp.txt", "a")
    ch = "y"

    while ch == "y" or ch == "Y":
        eno = input("Enter empno")
        name = input("Enter Name")
        salary = input("Enter salary")
        f1.write(eno + ":" + name + ":" + salary + "\n")
        ch = input("Continue (y/n)")
    f1.close()

def searchfile():
    f1 = open("emp.txt", "r")
    # print(f1.read())
    flag = 0

    eno = input("Enter eno to search ")
    for x in f1:
        #print(x)
        str = x.split(":")
        if str[0] == eno:
            print(str[0] + "\t" + str[1] + "\t" + str[2] + "\n")
            flag = 1
            break

    if flag == 0:
        print("No such empno ")
    f1.close()

def showfile():
    f1 = open("emp.txt", "r")
    # print(f1.read())
    flag = 0
    for x in f1:
        # print(x)
        str = x.split(":")
        print(str[0] + "\t" + str[1] + "\t" + str[2] + "\n")

    f1.close()


def insertfile():
    f1 = open("emp.txt", "a")
    eno = input("Enter empno")
    name = input("Enter Name")
    salary = input("Enter salary")
    f1.write(eno + ":" + name + ":" + salary + "\n")
    f1.close()


def deletefile():
    f1 = open("emp.txt", "r")
    f2 = open("nemp.txt", "w")
    # print(f1.read())
    flag = 0

    eno = input("Enter eno to search ")
    for x in f1:
        # print(x)
        str = x.split(":")
        if str[0] == eno:
            print("Record getting deleted ...........")
            print(str[0] + "\t" + str[1] + "\t" + str[2] + "\n")
            flag = 1
        else:
            f2.write(x)

    if flag == 0:
        print("No such empno ")
    f1.close()
    f2.close()
    os.remove("emp.txt")
    os.rename("nemp.txt","emp.txt")


ch=0
while ch<6:
    print( "\n1. Create")
    print( "\n2. Search")
    print( "\n3. Show all")
    print( "\n4. Insert")
    print( "\n5. Delete")
    print( "\n6. Exit")
    ch=int(input( "\nEnter your choice ::"))
    if ch==1:
        createfile()
    elif ch==2:
        searchfile()
    elif ch==3:
        showfile()
    elif ch==4:
        insertfile()
    elif ch==5:
        deletefile()


