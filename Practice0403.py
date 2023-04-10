n = int(input("Enter an integer"))

if n % 2 == 0:
    print("Not Weird")
elif n % 3 == 0:
    print ("Weird")     
elif 2 <= n <= 5:    
    print ("Not Weird")
elif 6 <= n <= 20:
    print ("Weird")
elif  n > 20:
    print ("Not Weird")
else:
    pass               

