from Vuelo import Vuelo
from pasajero import Pasajero


class Reserva:
    def __init__(self, pasajero:Pasajero, vuelo:Vuelo):
        self.pasajero:Pasajero = pasajero
        self.vuelo:Vuelo = vuelo
    
    def mostrar_info(self):
        print(f"Reserva para {self.pasajero.nombre} en el vuelo {self.vuelo.numero_vuelo} de {self.vuelo.origen} a {self.vuelo.destino}.")