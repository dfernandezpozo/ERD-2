import pandas as pd

df = pd.read_csv("alumnos.csv")
dfN =pd.read_csv("notas.csv")

# print(df.head(5))

df_sinNulos=df.head(5).dropna()
# print(df_sinNulos)

df_sinNulos.to_csv("limpieza.csv")

# print(df)
# print(" ")
# print(dfN)

df_merged=pd.merge(df,dfN, on="Nombre")
print (df_merged)



