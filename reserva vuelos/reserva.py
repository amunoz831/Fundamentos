class Reserva:
    def __init__(self, pasajero, vuelo):
        self.pasajero = pasajero
        self.vuelo = vuelo
    
    def mostrar_info(self):
        print(f"Reserva para {self.pasajero.nombre} en el vuelo {self.vuelo.numero_vuelo} de {self.vuelo.origen} a {self.vuelo.destino}.")