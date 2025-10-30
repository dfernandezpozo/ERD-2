import pandas as pd

ventas={
    "Producto":["coche","aspiradora","lapiz","queso"],
    "Cantidad":[20,4,60,8],
    "Precio":[200,5,1,20]
}

df=pd.DataFrame(ventas)

def mostrar(row):
    
    if row["Cantidad"]>10:
        return row["Producto"]
    else:
        return ""
    


df["Resultado"]=df.apply(mostrar,axis=1) #importante el axis 1 para que lo haga por filas

print(df)

    
    


