#Robot Barista 

name = input("What is your name? ")
menu = "Latte Machiato, Coffee, Black Coffee "
price =  8 


if name == "Pepe":
    print("Your are not welcome here Paloma!")
    exit()
else:
    print("Hello " + name + " what do you want from our menu today? Here is what we have " + menu)
    

order = input ()


print("How many " + order + " " + "do you want?")


ammount = input()

total = price * int(ammount)


print ("Thank you!, your total is:" + " " + str(total) + " USD")

print ("We will have your " + ammount + " " + order + " in a moment")

