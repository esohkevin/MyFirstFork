# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print ("Hello World!")
name = input("Please enter your name: " )
print("Hi " + name + ", You are welcome to anaconda. "+ 
      "Please respond to the following questions")
age = input("Tell me " + name + ", what is your age?: ")
address = input("Where do you live?: ")
##address = address.upper
school = input("Where do you school?: ")
pet = input("Do you have a pet?: ")
##pet = pet.lower

if pet == "yes":
    petName = input("What is your pet's name?: ")

opinion = input("How are you finding life here?: ")
wishOpp = input("We wanna give you an opportunity to reach one person today." + 
                 " Do you have a wish to anyone?: ")
if wishOpp == "yes":
    wishList = input("Who do you wanna say Hi to? (Enter name please): ")
    wish = input("Go ahead and make your wish to " + wishList + ": ")
print("\nHey " + name + "!, We are happy to have you on live TV" +
     "\n" + "\nWe understand that you are " + age + " years old, " +
      "and you're from " + address + ". \nYou're a student of " + school)
if pet == "yes":
    print("it's interesting that you have a pet. \nYou must surely love " + petName)
else:
    print("\nIt looks like you are no fun of pets.")    
print("\nThis is your opinion about this city; " + opinion)
if wishOpp == "yes":
    print("\nYou said this to " + wishList + ": " + wish + ".")
print("We are happy to have you again " + name + ", and we haope you enjoy your stay with us.")