# -*- coding: utf-8 -*-
## 1\.Exercice 1 : Un échiquier
print("\nExercice 1 : Un échiquier")
line = "# # # # # # # #"
blanc = " "

print("```")
print("  \"")
for i in range(0, 8):
    if i%2 == 0:
        print("   {}{}".format(line, blanc))
    else: 
        print ("   {}{}".format(blanc, line)) 
print("  \"")
print("```")      

## 2\.Exercice 2 : Matrix dans le terminal
print("\nExercice 2 : Matrix dans le terminal")
L = [0,0,0,0]
var1=0; var2=0; var3=0; var4=0; var5= "-------"
print("```")
for i in range(0, 4):
    L[i] = 1
    var1 = L[0]
    var2 = L[1]
    var3 = L[2]
    var4 = L[3]
    print("{}\n{}\n{}\n{}\n{}".format(var1,var2,var3,var4,var5))
    L[i] = 0
print("```")

## 3\.Exercice 3 : Nombre paire ?
print("\nExercice 3 : Nombre paire ?")

def evenYesNo(number):
    number = int(number)
    print(not(number%2))

user = input("Entrez votre montant ? ") 
if "." in user:
    user=float(user)
else:
    user=int(user)
evenYesNo(user) 

## 4\.Exercice 4 : Vous avez dit factorielle ?
print("\nExercice 4 : Vous avez dit factorielle ?")

def fact(n):
    """fact(n): calcule la factorielle de n (entier >= 0)"""
    x=0
    if "." in n:
        print("Pas un nombre enier")
    else:
        n=int(n)
        if n == 0:
            x=0
        else:
            x=1
            for i in range(2,n+1):
                x*=i
    return x

nb= input("Entrez un nombre entier : ")
print("Resultat = ",fact(nb))

## 5\.Exercice 5 : Les tirets ça compte !
print("\nExercice 5 : Les tirets ça compte !")

def convertHyphenintoUnderscore(theString):
    try:
        isNB = float(theString)
        if float(isNB):
           myReturn = "Ceci est un nombre"
    except:
        if "-" in theString:
            i=0
            while "-" in theString:
                if theString[i] == '-':
                    break
                i+=1
            myReturn = theString[:i]+'\_'+theString[i+2:]
        else:
            myReturn = theString
    return(myReturn)

myString = input("Entrez votre ligne de facturation : ")
print(convertHyphenintoUnderscore(myString))

## 6\.Exercice 6 : Entraînez-vous avec les tableaux
print("\nExercice 6 : Entraînez-vous avec les tableaux")

## 7\.Exercice 7 : Le tableau d'un homme
print("\nExercice 7 : Le tableau d'un homme")

## 8\.Exercice 8 : Le max d'un tableau
print("\nExercice 8 : Le max d'un tableau")

## 9\.Exercice 9 : Une to do list
print("\nExercice 9 : Une to do list")
