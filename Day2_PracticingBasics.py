name="Denish Pradhan"
age=19
country="Nepal"

bpm=int(input("What is your BPM? "))
bars=int(input("How many bars do you want to practice? "))
totalTime=(bpm * bars)/60
print("You will practice for", totalTime, "seconds")


numrun=0
for i in range (5):
    print("I am practicing my basics")
    numrun+=1
print(numrun)

for i in range(1,10,1):
    for j in range(1,10,1):
        print(i,"x",j,"=",i*j)