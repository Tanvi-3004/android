f1=open("zeenal.txt","r")
#print(f1.read())
cnt=0

for x in f1 :
     print(x)
     cnt+=1

f1.close()
print("Total lines ",cnt)