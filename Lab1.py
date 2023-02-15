#!/usr/bin/env python3

name = input("Name: ")
def helloWorld():
    print("Hello World")

def calculateAge():
    age = input("Age: ")
    try:
        return int(age)
    except:
        print("Please enter an int")
        continue


helloWorld()
print("Hi " + name + ", You are " + str(age) + " years old.")
