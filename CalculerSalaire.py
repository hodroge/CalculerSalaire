
##test vide pour verifier que notre test est valable
# def CalculerSalaire(metier,exp):
#     return " "

def CalculerSalaire(metier,exp):
    if metier=="Architecte" and exp==4:
        return "4000 euros"
    if metier=="médecin" and exp==8:
        return "7000 euros"
    if metier=="consultant" and exp==5:
        return "5000 euros"
    else:
        return "non existant"

#faitre attentyion à ne pas mettre le salaire dans le string pour que la fonction l'execute une fois c"est bon pour les test
print ("le salaire de l'Architecte est: ",str(CalculerSalaire("Architecte",4)))
print ("le salaire du médecin est: ",str(CalculerSalaire("médecin",8)))
print ("le salaire du consultant est: ",str(CalculerSalaire("consultant",5)))