print("\nexercise 1 : Tallest number \n")
#i declare many variable
pomme = 16
poire = 4
banane = 32
orange = 12



print("\nexercise 2 : age condition\n")

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


print("\nexercise 3 : hidden number \n")

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


print("\nexercise 4 : numbers to loops \n")

for num in range(100):#for num in range 0 at 100
    print(num + 1)#display all number 0 at 100

print("\nexercise 5 : number to loops 2\n")


for num in range(101):#for num in range 0 at 101
    if num %2 == 0:#if num is modulo of 2 egual zero
        print(num)#print num


print("\nexercise 6 : fill the pool\n")
#i declare many variable longeur largeur hauteur and debit
hauteur = 2 
largeur = 4
longeur = 6
debit_eau = 2
minute = 1
metre_cube_piscine = largeur * longeur * hauteur#i declare a variable to m3 of picsine with result of calcul 
print("temps de remplissage",metre_cube_piscine/debit_eau,"mn")#i display the result of calcul


print("\nexercise 7 : calcul the circle\n")

import math#import the function math
from math import pi #from math i import the function pi
rayon=int(input("enter rayon:"))#i declare a variable to ray of input user

def aire():#i create a function "aire"
    aze=round(pi*(rayon**2),2)#i declare a variable "aze" egual round pi x ray xx 2 ,2
    print(aze)#display aze
def perimetre():#i create a function "perimetre"
    diametre = 2 * rayon#i declare a variable "diametre" egual two x ray
    are=round(pi * diametre,2)#i declare a variable "are" round pi x diametre ,2
    print(are)#i display are

aire()#call function aire
perimetre()#call function perimetre


print("\nexercise 8 : a pyramid \n")

i= 5#i declare "i" egual 5
for i in range(1,6): #for i in range 1 at 6
    print('*' * i)#display star multiply by i
    i = i-1#i declare i egual i - 1


print("\exercise 9 : fizzbuzz")

chiffre = 0 #i declare a variable i = 0
chiffre=chiffre+1#i declare a variable chiffre egual chiffre + 1

import math #import method math
for num in range(101):#for num in range 0 at 101
  chiffre = num+1#i declare a variable chiffre egual num + 1
  if num%3 == 0:#if num modulo of 3 is egual zero
    print("FIZZ")#display"fizz"
  if num%5 == 0:#if num modulo of 5
    print("BUZZ")#display "buzz"
  if num%3 == 0 and num%5 == 0:#if num modulo of 3 is egual 0
    print("FIZZBUZZ")#display "fizzbuzz"