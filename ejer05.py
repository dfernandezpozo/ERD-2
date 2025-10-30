import pandas as pd

df=pd.read_csv(r"C:\Users\Ferni\Desktop\proyecto2-ERD\ERD-2\DigiDB_digimonlist.csv")
# print(df)

df=df.dropna()
# print(df)
df["Digimon"]=df["Digimon"].astype(str)
df["Stage"] = df["Stage"].astype(str)
df["Lv 50 HP"] = df["Lv 50 HP"].astype(float)
df["Lv50 Atk"] =df["Lv50 Atk"].astype(int)
df["Lv50 Def"] =df["Lv50 Def"].astype(float)

# print(df)

df["A palabra"] = ["AlfonsoMon", "JaenMon", "FigmaMon", "IAMon", "GPTMon", "FiredMon"] + [""] * (len(df) - 6)
print(df.head(6))

# Exportamos el resultado a csv

df.to_csv("digimon_cleaned.csv")






