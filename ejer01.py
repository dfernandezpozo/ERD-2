import pandas as pd

datos={
    "Nombre":["Pepe","Jordi","Alberto","Alfonso","Julia","Ana"],
    "Edad":[22,14,None,22,30,14],
    "Nota":[1.2,5,None,5,None,None]
}

df=pd.DataFrame(datos)
# print(df)

# Eliminar las filas vacías
df_quitar_vacio=df.dropna()
# print(df_quitar_vacio)

# Sustituir los valores nulos por la mediana
df["Edad"].fillna(df["Edad"].median(), inplace=True)
df["Nota"].fillna(df["Nota"].median(),inplace=True)
# print(df)

# Eliminamos datos duplicados
df_sin_dup=df.drop_duplicates()
# print(df_sin_dup)

# Cambiamos la edad a int
df["Edad"]=df["Edad"].astype(int)
# print(df)

# Nueva columna
df["Precios"]=["12.4","13.2","45.3","2","23.4","6"]
# print(df)

# Convertimos a float
df["Precios"]=df["Precios"].astype(float)
# print(df.dtypes)

# Calculamos mediana
df["Precios"].fillna(df["Precios"].median(),inplace=True)
# print(df)

# Ejer 2A
df["Resultado"]=df["Nota"].apply(lambda x: "Aprobado" if x>=5 else "Suspendido")
# print(df)

# Ejer 2C
df_ordenado = df.sort_values(by="Nota",ascending=False)
print(df_ordenado)



