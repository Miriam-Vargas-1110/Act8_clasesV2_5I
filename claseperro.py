
print("Clase version 2 el constructor")

class Perro:
    # Fucion constructor
    def __init__(self,color,edad):
        self.color = color
        self.edad = edad
    # Funciones creadas por el usuario 
    def muerde(self):
        print("Chale el perro me mordio")
    def chatperro(self, mensaje):
        print(f"Chat perro: {mensaje}")
    def chatperra(self, mensajep):
        print(f"chat perra: {mensajep}")
    def datos(self):
        print(f"color {self.color} edad{self.edad}")
# crear el objeto
chihuas=Perro("Negro",2)
# llamadas a funciones
chihuas.datos()
chihuas.muerde()
chihuas.chatperro("Hola canina")
chihuas.chatperra("Hola boby")
chihuas.chatperro("Quieres ser mi novia?")
chihuas.chatperra("grrru......")