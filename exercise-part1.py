print("\nexercise :1 \n")
#i declare many variable
pomme = 16
poire = 4
banane = 32
orange = 12

def maxi(*args):#i create a function named "maxi" and adding "args" method
	maximum = args[0]#i declare a variable named "maximum" is same args[0]
	for fruits in args[1:]:#i create a condition 
		if fruits > maximum:#if fruit is bigger variable maximum
			maximum = fruits#i declare a variable maximum egual fruits
	return maximum#return the function

print(maxi(*[pomme, poire, banane, orange]))#i display the function with items

print("\nexercise 2:\n")

import math#import function "math"
age = int(input("enter age:"))#i declare a variable with the enter of user

if age <= 0:#if age is smallest or egual of zero
	print("enter realy age:")#i display a message "enter realy age"
if age >=21:#if the variable "age" is bigger of egual twenty one
	print("ok")#display message "ok"
if(age%2==0):#if variable "age" modulo of 2 is egual "0"
    print("your age is pair")#display message "pair"
if math.sqrt(age).is_integer():#if math sqrt function is an integer number
    print ("your age is a square")#display a message is a square
if math.sqrt(age).is_integer()==False:#if math sqrt number no
    print ("your age is not a square")#display message is not a square


print("\nexercise 3:\n")

nombent = 58#i declare the hidden number is 58
usernb = int(input("enter a number:"))#i declare a variable for input user number
while usernb != nombent:#while entry user is not the same of the hidden number
    if nombent>usernb:#if hidden numer is tallest the user number
        print("your number is smaller")#display message "smaller"
        usernb = int(input("enter a number:"))#i declare a variable for input user number
    if nombent<usernb:#if hidden number is smaller the user number
        print("your number is taller")#display the message "taller"
        usernb = int(input("enter a number:"))#i declare a variable for input user number
if usernb == nombent:#if user number is egual the hidden number 
    print("you win") #display message "you win"


print("\nexercise 4:\n")

for num in range(100):#for num in range 0 at 100
    print(num + 1)#display all number 0 at 100

print("\nexercise 5:\n")


for num in range(101):#for num in range 0 at 101
    if num %2 == 0:#if num is modulo of 2 egual zero
        print(num)#print num


print("\nexercise 6:\n")
#i declare many variable longeur largeur hauteur and debit
hauteur = 2 
largeur = 4
longeur = 6
debit_eau = 2
minute = 1
metre_cube_piscine = largeur * longeur * hauteur#i declare a variable to m3 of picsine with result of calcul 
print("temps de remplissage",metre_cube_piscine/debit_eau,"mn")#i display the result of calcul