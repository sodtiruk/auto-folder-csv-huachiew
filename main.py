import os
import pandas as p

dataframe = p.read_csv("NameHN.csv") # Your CSV

for index, row in dataframe.iterrows(): 

    nestedFolders = f"{row['ฝ่าย']}/{row['แผนก']}/{row['ตำแหน่ง']}/{row['ชื่อ']+row['สกุล']}"
    os.makedirs(nestedFolders)
