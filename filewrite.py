#write data into file
#open("fname","mode")
f1=open("zeenal.txt","w")
n=int(input("Enter n"))

for x in range(1 ,n+1) :
    city=input("Enter city")
    f1.write(city+"\n")

f1.close()

