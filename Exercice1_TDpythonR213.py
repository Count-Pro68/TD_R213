print("calcul prêt imobilier ou d'un crédit à la consommation.")
s=int(input("Entrer le montant du prêt ou crédit:"))
t=float(input("Entrer le taux annuel en %:"))
n=int(input("Entrer le nombre d'années:"))

#tm=(1+t/100)**(1/12)-1

tm=t/12/100
a=(1+tm)**(12*n)
m=s*tm*a/(a-1)

print("la mensualité avec intérêts est de", round(m,2),"euros")
print("le montant des intérêts remboursés sont de", round(m*12*n-s,2),"euros.")
print("le taux mensuel est de", tm)
print("\nTableau d'amortissement:")
print("Mois - Mensualité - Intérêts - Capital remboursé - Captital restant dû - Intérêts remboursés")

ir=0

for j in range(n*12):
    i=tm*s      #intérêts
    cr=m-i      #capital restant
    crd=s-cr    #capital restant dû
    ir=i+ir     #intérêts restant

    print("", j+1, "- ", round(m,1), " - ", round(i,1), " -  ", round(cr,1), "  -  ", round(crd,1), "  - ", round(ir,2))
    s=crd