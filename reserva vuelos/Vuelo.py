from datetime import datetime

class Vuelo:
    def __init__(self, numero_vuelo, origen, destino, asientos, fecha_imcio:datetime, fecha_final:datetime):
        self.numero_vuelo = numero_vuelo
        self.origen = origen
        self.destino = destino
        self.asientos_disponibles = asientos
        self.reservas = []
        self.activo = True

    def agregar_reserva(self, reserva):
        if self.asientos_disponibles > 0 and self.activo:
            self.reservas.append(reserva)
            self.asientos_disponibles -= 1
        else:
            print(f"No hay asientos disponibles en el vuelo {self.numero_vuelo} o el vuelo ha sido cancelado.")

    def cancelar(self):
        self.activo = False

    def mostrar_info(self):
        estado = "Activo" if self.activo else "Cancelado"
        print(f"Vuelo {self.numero_vuelo} de {self.origen} a {self.destino}. Asientos disponibles: {self.asientos_disponibles}. Estado: {estado}")
