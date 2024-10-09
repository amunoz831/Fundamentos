from usuario import Usuario
from reserva import Reserva


# Clase Pasajero hereda de Usuario
class Pasajero(Usuario):
    def __init__(self, nombre, email, pasaporte,edad:int):
        super().__init__(nombre, email)
        self.pasaporte = pasaporte
        self.reservas = []
        self.edad:int= edad

    def hacer_reserva(self, vuelo):
        nueva_reserva = Reserva(self, vuelo)
        self.reservas.append(nueva_reserva)
        vuelo.agregar_reserva(nueva_reserva)
        print(f"Reserva creada para el vuelo {vuelo.numero_vuelo}")

    def mostrar_reservas(self):
        for reserva in self.reservas:
            reserva.mostrar_info()