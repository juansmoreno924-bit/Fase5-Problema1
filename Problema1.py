#creamos una matriz con 5 filas
matriz=[[1,120,8],[2,40,5],[3,60,7],[4,10,2],[5,200,10]]

#modulo de clasificacion basado en duracion y clics
def clasificacion(duracion,clics):
    if duracion>180 and clics>8:
        return "alta"
    elif duracion<60 or clics<3:
        return "baja"
    else:
        return "media"

# imprimimos el informe
print("Informe")
for fila in matriz:
    if not fila:
        print("fila vacia")
    else:
        id,duracion,clics=fila
        print("id:",id,
              "Duracion:",duracion,
              "Clics:",clics,
              "clasificacion:",clasificacion(duracion, clics)
        )