#Fonction permettant le calcul pour assurance vie


#<---- déclare variables ---->
def c(n):
    if n==0:
        return c0
    else:
        return((c(n-1)+12*m)*(1+t/100)) #taux

print("Calcul du capital acquis et de ses intérêts versés lorsque les intérêts sont calculés une fois par an")


#<---- déclare variables ---->
c0=int(input("Entrer le placement de départ:"))
m=int(input("Entrer le montant du versement mensuel:"))
t=float(input("Entrer me taux annuel en %:"))
n=int(input("Entrer le nombre d'années:"))

#<---- affiche variables ---->
print("le capital acquis avec intérêts est de", round(c(n),2), "euros au bout de", n, "ans avec des versements mensuels") #capital acquis (c0 = capital de départ)
print("Les intérêts gagnés au taux annuel de", t, "% sont de", round(c(n)-n*m*12-c0,2), "euros.") #
print("Sans placement avec intérêts le capital acquis serait de", round(n*m*12+c0,2),"euros")


# Exemples 1 -->

# c0 = 200 euros
# t = 3 %
# c^n = 10 000 euros (capital avec intérêts)
# m = ? (--> 69 euros)
# durée = 10 ans
# intérêts => 1565 euros

# Exemples 2 -->

# c0 = 200 euros
# t = 3 %
# c^n = 10 000 euros
# m = 100 euros
# durée maximum = ?
# intérêts
#    n = 8 => 11 246 (intérêts = 1444)

