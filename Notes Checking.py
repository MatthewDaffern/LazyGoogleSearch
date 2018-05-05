import subprocess
file=open("IdentityNotes.txt", 'r+')
listofsearchqueries=list()
listofsearches=list()
for i in file:
    newline=str(i).replace(" ","+")
    listofsearches.append(str("http://www.google.com/search?q="+str(newline))+"+Windows+Server")  
x=1
ChromePath=input('Please enter the full path variable of Chrome.exe')
for i in listofsearches:
    subprocess.run([ChromePath,i])
    print(str(x)+" : "+listofsearches[x])
    x=x+1
