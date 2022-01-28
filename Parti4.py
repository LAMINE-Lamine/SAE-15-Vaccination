import csv

#ici on crée une fonction qui va me permettre d'avoir une region et sa date l'une a coter de l'autre .
def forme(fusion_csv):
    #ouverture et lecture du fichier nommer fusion .
    with open(fusion_csv) as file:
        x = csv.reader(file)
        #je met acttuellement tout les mot clés se qui represente la ligne de la partie du haut avec une separation | pour pas avoir de probleme au niveau du regroupement par la suite. 
        c ="date_reference|semaine_injection|region_residence|libelle_region|departement_residence|libelle_departement|population_insee|classe_age|libelle_classe_age|type_vaccin|effectif_1_inj|effectif_termine|effectif_cumu_1_inj|effectif_cumu_termine|taux_1_inj|taux_termine|taux_cumu_1_inj,taux_cumu_termine|date,effectif_rappel|effectif_cumu_rappel|effectif_rappel_parmi_eligible|effectif_eligible_au_rappel|taux_rappel|taux_cumu_rappel|taux_cumu_rappeleli".split("|")
        #cela va me permettre d'afficher deux ligne distinct (0 inclus et 2 non inclus) 
        l=[list() for loop in range(2)]
        #une boucle lier a notre fichier .
        for i in x:
            i=i[0].split(";")
            #permet de de lire le tableau et en suite dans notre liste 0 on ajoute la ligne 5 celle dont on a besoin et la liste 1 on ajoute la ligne 18 la ou se trouve les dates .
            if not "date_reference" in i and len(i)>19:
                l[0].append(i[5])
                l[1].append(i[18])
        return l



#sotck les donnes dans a 
a=forme("fusion.csv")
for i in range(len(a[0])):
    #permet de lire la liste 0 tant quelle ne se finisse pas la meme chose pour la liste 1
    print(a[0][i],a[1][i])
