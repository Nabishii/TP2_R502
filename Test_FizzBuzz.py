def affiche():
    for i in range(1, 101):  
        output = ""  

        if i % 3 == 0 and i % 5 == 0:  
            output = "FrisBee"
        elif i % 3 == 0:  
            output = "Fizz"
        elif i % 5 == 0:  
            output = "Buzz"
        else:
            output = str(i)  

        print(output)  

affiche()
