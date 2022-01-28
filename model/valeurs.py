import csv

header = "date_reference,semaine_injection,region_residence,libelle_region,departement_residence,libelle_departement,population_insee,classe_age,libelle_classe_age,type_vaccin,effectif_1_inj,effectif_termine,effectif_cumu_1_inj,effectif_cumu_termine,taux_1_inj,taux_termine,taux_cumu_1_inj,taux_cumu_termine,date,effectif_rappel,effectif_cumu_rappel,effectif_rappel_parmi_eligible,effectif_eligible_au_rappel,taux_rappel,taux_cumu_rappel,taux_cumu_rappeleli".split(",")

dico = {}
liste_dico=[]

with open('fusion.csv',"r") as csvfile:
    reader = csv.DictReader(csvfile,delimiter=";")
    for row in reader:
        liste_dico.append(row)

def search_by(arg,liste):
    l = []
    for i in liste:
        l.append(i[arg])
    return l

def missing_val(data):
    missing=0
    for i in data:
        if i=="":
            missing+=1
    return missing

for i in header:
    print(missing_val(search_by(i,liste_dico)))




