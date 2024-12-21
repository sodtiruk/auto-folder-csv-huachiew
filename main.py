import os
import pandas as pd

# Load CSV file
dataframe = pd.read_csv("NameHN.csv")

for index, row in dataframe.iterrows():
    base_path = f"result/{str(row['ฝ่าย']).strip()}/{str(row['แผนก']).strip()}/{str(row['ตำแหน่ง']).strip()}/{str(row['ชื่อ']).strip() + str(row['สกุล'])}".strip()

    # Define folder paths
    training_folder = f"{base_path}/Trainning"
    result_health_folder = f"{base_path}/ผลตรวจสุขภาพ"
    vaccine_folder = f"{base_path}/วัคซัน"

    # Create directories if they do not exist
    print(training_folder)
    os.makedirs(training_folder, exist_ok=True)

    print(result_health_folder)
    os.makedirs(result_health_folder, exist_ok=True)

    print(vaccine_folder)
    os.makedirs(vaccine_folder, exist_ok=True)