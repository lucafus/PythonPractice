name = input("What is your name? ")

if len(name) >= 6:
    print("Your names is long")
elif len(name) == 5:
    print("Your names is correct")
elif len(name) >= 4:
    print("Your name is short")
else:
    print("Your names is too long or too short")
    
    