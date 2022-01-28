import pandas as pd
import csv
import matplotlib.pyplot as plt

x = []
y = []

with open('fusion.csv', "r") as csvfile:
    plots = csv.reader(csvfile, delimiter=';')
    for row in plots:
        x.append(str(row[5]))
        y.append(str(row[10]))

df = pd.read_csv('fusion.csv')

l=[]
for i in range(len(x)):
    if x[i]=="Haut-Rhin":
        l.append(y[i])

y=[i for i in range(len(l))]
explode=(0, 0.15, 0, 0)
plt.xlabel('Evolution dans le Haut-Rhin', fontsize=10)
plt.ylabel('Effectif primo vaccinés', fontsize=10)
plt.pie(df, explode=explode, labels=l, autopct='%1.1f%%', startangle=90, shadow=True)
plt.axis('equal')
plt.show()