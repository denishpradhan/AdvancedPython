
def greet(time,name,status):
    time = int(input("Enter 1 for Morning, 2 for Afternoon, 3 for Evening: "))
    name = input("Enter your name: ")
    if time == 1:
        print("Good Morning",name,"Welcome to our Musicians Community")
    elif time == 2:
        print("Good Afternoon",name,"Welcome to our Musicians Community")
    elif time == 3:
        print("Good Evening",name,"Welcome to our Musicians Community")
    else:
        print("Hello",name,"Welcome to our Musicians Community")

    status = input("Enter your thing (Producer, Vocalist, Guitarist, Bassist, Drummer) or type (1,2,3,4,5) respectively: ")
    if status == "Producer" or status == "1":
        print("Are you ready to create some beats?")
    elif status == "Vocalist" or status == "2":
        print("Are you ready to sing some melodies?")
    elif status == "Guitarist" or status == "3":
        print("Are you ready to play some chords?")
    elif status == "Bassist" or status == "4":
        print("Are you ready to lay down some bass lines?")
    elif status == "Drummer" or status == "5":
        print("Are you ready to keep the beat?")

greet("time","name","status")