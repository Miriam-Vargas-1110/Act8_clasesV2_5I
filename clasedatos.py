class Informacion:

    def mi_lista(self):
        lista_Nomperros=["boby","Dollar","fany"]
        for X in lista_Nomperros:
            print(X)

    def mi_tupla(self):
        tupla_colores=("Azul","Morado","Rosa")
        for x in  tupla_colores:
            print(x)

    def mi_conjunto(self):
        conjunto_flores={"Rosa","Margarita","Lavanda"}
        for X in conjunto_flores:
            print(X)

    def mi_diccionario(self):
        diccionario_ropa= {
            "tipo": "vestido",
            "estilo": "largo",
            "color": "Azul"}
        for X, key in diccionario_ropa.items():
            print(X,"=",key)

# creando el objeto

datos=Informacion()
print("\nListado de nombre de perros------")
datos.mi_lista()
print("\nTupla de nombre de colores--------")
datos.mi_tupla()
print("\nConjunto de nombre de flores-------")
datos.mi_conjunto()
print("\nDiccionario de ropa------")
datos.mi_diccionario()