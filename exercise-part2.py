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
