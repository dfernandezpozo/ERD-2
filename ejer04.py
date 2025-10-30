import pandas as pd

df=pd.read_csv("alumnos4.csv")

media = df["Nota"].mean()
maximo = df["Nota"].max()
minimo = df["Nota"].min()

# print(media)
# print(maximo)
# print(minimo)

df["Categoria"]=df["Nota"].apply(lambda x: "Excelente" if x>=9 else "Notable" if x>=7 else "Aprobado" if x>=5 else "Suspendido")
# print(df)

dfV=pd.read_csv("ventas.csv")
#print(dfV)

dfV_sin_espacios=dfV.dropna()
# print(dfV)

dfV["Cantidad"]=dfV["Cantidad"].abs()
dfV["Precio"]=dfV["Precio"].abs()
# print(dfV)

# Hacemos el total con un groupby
dfV["Total"] = dfV["Cantidad"] * dfV["Precio"]
total_por_producto = dfV.groupby("Producto")["Total"].sum()
print(total_por_producto)
