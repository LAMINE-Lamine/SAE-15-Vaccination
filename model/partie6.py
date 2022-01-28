import pandas as pd
import csv
import matplotlib.pyplot as plt

x = []
y = []

with open('dataframe.csv', "r") as csvfile:
    plots = csv.reader(csvfile, delimiter=';')
    for row in plots:
        x.append(str(row[5]))
        y.append(str(row[18]))

df = pd.read_csv('dataframe.csv')

l=[]
for i in range(len(x)):
    if x[i]=="Haut-Rhin":
        l.append(y[i])

y=[i for i in range(len(l))]

plt.xlabel('Evolution dans le Haut-Rhin', fontsize=10)
plt.ylabel('Effectif primo vaccinés', fontsize=10)
plt.plot(y,l)
plt.title('l évolution de primo vaccinés pour le haut rhin')

plt.show()
