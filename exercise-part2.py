print("exercise 1 : chessboard\n")
i  = 0 # i declare "i" is = zero
for i in range(0,4):#for i in ran
    print(" # # # # # # # #")# display first line
    print("# # # # # # # #")#display second line
    i = i + 1#i declare i is egual i + 1


print("\nexercise 2 : matrix\n")




print("\nexercise 3 : pair number\n")

nb = round(float(input("enter a number:")))#i declare nb is enter user
def panier(nb) :# i create a function named "panier"
    if (nb%2) == 0:#if nb modulo 2 is == 0
        print(bool(nb))#display true or false "nb"
    else:#sinon
        print(bool())#display ture or false ""

   

panier(nb)#call function "panier"


print("\nexercise 4 : you said factorial\n")
try:#try 
    num = 1#i declare a variable "num" to "1"
    number = int(input("enter an integer number:"))#i declare a variable "number" to number enter
    for i in range(1,number+1):#for i in range number + 1
        num = num * i#i declare num egual num multiply by "i"
        print("factorial of number is:",num)#display the foctorial of number is ...
except:#exception
        print("error is not an integer")#display messenger error


print("\nexercise 5 : les tirets ca compte\n")

def change():#i create a function nammed "change"
     name = input("enter a string:")#i declare a variable name is = string enter of user
     nameChange = name.replace("-", "\_")#i declare a variable with replace "-" by "\_"
     print(nameChange)#i display new variable "namechange" 
     if name=="":#if name is egual not entry
        print("error")#i display an error messenger
     
change()#call the function named "change"


print("\nexercise 6 : training with boards\n")

liste = ["eau","javel","savon","gateaux","lait","chocolat","pain"]#i create a liste with items 
print("by",liste[0])#i display the first items of the list (number 0 )
print("by",liste[-1])#i display the latest items of the list (number -1)
num=(int(len(liste)/2))#i definite the middle items in the list
print(liste[num])#i display this items
       
print("\nexercise 7 : man boards\n")

information = ["nicolas", "turck", "34ans", 1985]#i create a list with informations of an users

def user(information):#i create a function named "user"
    for i in information:#for i in the list 
        print(i)#display i (items)


user(information)#call the function