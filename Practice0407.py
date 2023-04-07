#Robot Barista 

name = input("What is your name? ")
menu = "Latte Machiato, Coffee, Black Coffee "
price =  8 

#Evil identification sector

if name == "Pepe" or name == "Paloma" or name == "Loki":
    evil = input("Are you evil?\n")
    gooddeeds = int(input("How many good deeds have you done today?\n"))
    if evil == "yes" and gooddeeds < 4:
        print("Your are not welcome here " +  name)
        exit()    
    else:
        print("So you are not that evil eh? Ok, you can come in")

else:
    print("Hello " + name + " what do you want from our menu today? Here is what we have " + menu)

#Order sector  

order = input ()

if order == "Latte Machiato":
    price = 13
    order2 = input("Do you want it with extra cream?")
    if order2 == "yes":
        price = 15
if order == "Coffee":
    price = 8
elif order == "Black Coffee":
    price = 3
else:
    print ("We don't have this")
    exit()

print("How many " + order + " " + "do you want?")


ammount = input()

total = price * int(ammount)

#Total ammount

print ("Thank you!, your total is:" + " " + str(total) + " USD")

print ("We will have your " + ammount + " " + order + " in a moment")

