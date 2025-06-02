def c(n):
    if n==0:
        return c0
    else:
        #return ((c(n-1)+m)*(1+t/100)**(1/12))
        return ((c(n-1)+m)*(1+t/100/12))

print("Calcul du capital acquis et des ses intérets versés lorsque les intérêts sont calculés une fois par mois")

c0=int(input("Entrer le placement de départ (c0) :"))
m=int(input("Entrer le montant du versement mensuel:"))
t=float(input("Entrer me taux annuel en %:"))
n=int(input("Entrer le nombre d'années:"))

print("le capital acquis avec intérêts est de", round(c(n*12),2), "euros au bout de", n, "ans avec des versements mensuels") #capital acquis (c0 = capital de départ)
print("Les intérêts gagnés au taux annuel de", t, "% sont de", round(c(n*12)-n*m*12-c0,2), "euros.") #
print("Sans placement avec intérêts le capital acquis serait de", round(n*m*12+c0,2),"euros")

#--> Exemples 1

# 10 ans m = 1469   i = 26313
# 15 ans m = 1058   i =
# 20 ans m =        i =
# 25 ans m =        i =
# 30 ans m =        i =

