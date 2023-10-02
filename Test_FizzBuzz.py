def affiche(n1, n2):
    results = [] 
    for i in range(n1, n2 + 1):  
        output = ""  
        if i % 3 == 0 and i % 5 == 0:  
            output = "FrisBee"
        elif i % 3 == 0:  
            output = "Fizz"
        elif i % 5 == 0:  
            output = "Buzz"
        else:
            output = str(i)  
        results.append(output)  
    return results  

n1 = int(input("Entrez la valeur de n1 : "))
n2 = int(input("Entrez la valeur de n2 : "))

resultats = affiche(n1, n2)

for resultat in resultats:
    print(resultat)
