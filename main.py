import os
import pandas as p

dataframe = p.read_csv("NameHN.csv") # Your CSV

for index, row in dataframe.iterrows(): 

    tranningFolder = f"{row['ฝ่าย']}/{row['แผนก']}/{row['ตำแหน่ง']}/{row['ชื่อ']+row['สกุล']}/{str("Trainning")}"
    resultHealth = f"{row['ฝ่าย']}/{row['แผนก']}/{row['ตำแหน่ง']}/{row['ชื่อ']+row['สกุล']}/{str("ผลตรวจสุขภาพ")}"
    vacine = f"{row['ฝ่าย']}/{row['แผนก']}/{row['ตำแหน่ง']}/{row['ชื่อ']+row['สกุล']}/{str("วัคซัน")}"
    os.makedirs(tranningFolder)
    os.makedirs(resultHealth)
    os.makedirs(vacine)
