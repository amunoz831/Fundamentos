from usuario import Usuario
from Vuelo import Vuelo
    # Clase Admin hereda de Usuario
class Admin(Usuario):
    def __init__(self, nombre, email):
        super().__init__(nombre, email)
    
    def crear_vuelo(self, numero_vuelo, origen, destino, asientos):
        nuevo_vuelo = Vuelo(numero_vuelo, origen, destino, asientos)
        print(f"Vuelo {numero_vuelo} creado.")
        return nuevo_vuelo
    
    def cancelar_vuelo(self, vuelo):
        vuelo.cancelar()
        print(f"Vuelo {vuelo.numero_vuelo} cancelado.")