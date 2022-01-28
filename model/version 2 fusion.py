import pandas as pd #on import la librairie pandas pour pouvoir faire appel à ses fonctions associés.

final_dataframe = pd.concat(map(pd.read_csv, [f'donnees-{i}.csv' for i in range(1, 5)]),
                            ignore_index=True)  # dans la fonction concat de pandas on utilise map qui va appliquer la fonction read à touts les fichiers commençant par donnes- pour tout i allant de 1 à 4

print(final_dataframe)

final_dataframe.to_csv(
    'donnees-f.csv', index=False)  # ici on convertit notre variable final_dataframe en fichier csv nommé donnees-f.csv