import pandas as pd
import csv
import glob
import os
header = "date_reference,semaine_injection,region_residence,libelle_region,departement_residence,libelle_departement,population_insee,classe_age,libelle_classe_age,type_vaccin,effectif_1_inj,effectif_termine,effectif_cumu_1_inj,effectif_cumu_termine,taux_1_inj,taux_termine,taux_cumu_1_inj,taux_cumu_termine,date,effectif_rappel,effectif_cumu_rappel,effectif_rappel_parmi_eligible,effectif_eligible_au_rappel,taux_rappel,taux_cumu_rappel,taux_cumu_rappeleli".split(",")

dico = {}
liste_dico=[]

with open('fusion.csv',"r") as csvfile:
    reader = csv.DictReader(csvfile,delimiter=";")
    for row in reader:
       liste_dico.append(row)
data=pd.fusion()
for f in file_list :
    df=pdread_csv(r"date_reference,semaine_injection,region_residence,libelle_region,departement_residence,libelle_departement,population_insee,classe_age,libelle_classe_age,type_vaccin,effectif_1_inj,effectif_termine,effectif_cumu_1_inj,effectif_cumu_termine,taux_1_inj,taux_termine,taux_cumu_1_inj,taux_cumu_termine,date,effectif_rappel,effectif_cumu_rappel,effectif_rappel_parmi_eligible,effectif_eligible_au_rappel,taux_rappel,taux_cumu_rappel,taux_cumu_rappeleli"+f)
    data = fusion.append(df ,ingnore_index=True)
data.shape

def ComputeMean(c=str):
    mean = x[c].mean()
    return mean
def ComputeMedian(c=str):
    median = x[c].median()
    return median



ComputeMedian('date_reference (A)')