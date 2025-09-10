def salaire_mensuel(salaire_annuel):
    return salaire_annuel/12

def salaire_hebdomadaire(salaire_mensuel):
    return salaire_mensuel/4

def salaire_horaire(salaire_hebdomadaire, heure_travaillee):
    return salaire_hebdomadaire/heure_travaillee

salaire_annuel = int(input("quelle est votre salaire annuel:"))
heure_travaillee = int(input("quelles sont vos heures de travail:"))

taux_horaire = salaire_horaire(salaire_annuel, heure_travaillee)

print("votre salaire a l heure :", taux_horaire)
