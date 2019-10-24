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