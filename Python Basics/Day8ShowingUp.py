# Learnings from W3Schools Python Course
# Day 8: Showing Up
# 1. range can be used in many ways not limited to just for loops.
# 2. A tuple is a collection of data like a list which is unchangeable 
# 3. An Object is a thing which is made by class and and the propertiesa dn attributes of the objects are decided in class
# 4. Machine Learning is the process of predicting a outcome accordign to the patterns and data given to the machine.


names=("hero","zero","nero")
print(names[1])
x=range(1,20,3)
print (x)
print(list(x))

# names[0]="denish"  # This will raise an error because tuples are immutable

class Person:
    name=input("Enter your name: ")
    age=int(input("Enter your age: "))

Person1=Person()
print(Person1.name)
print(Person1.age)
