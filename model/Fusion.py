import pandas as pd
import csv
import glob
import os

# merging the files
files_joined = os.path.join('C:\\vaccination-covid\\data\\raw', "donnees-*.csv")

# Return a list of all joined files
list_files = glob.glob(files_joined)

print("** Merging multiple csv files into a single pandas dataframe **")
# Merge files by joining all files
dataframe = pd.concat(map(pd.read_csv, list_files), ignore_index=True)
dataframe.to_csv("fusion.csv", index=False)
print(dataframe)



