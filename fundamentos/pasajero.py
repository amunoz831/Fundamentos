from usuario import Usuario
from reserva import Reserva
from Vuelo import Vuelo
from pasaporte import Pasaporte

# Clase Pasajero hereda de Usuario
class Pasajero(Usuario):
    def __init__(self, nombre:str, email:str, pasaporte:Pasaporte,edad:int,nacionalidad:str,genero:str):
        super().__init__(nombre, email)
        self.pasaporte:Pasaporte = pasaporte
        self.reservas:list [Reserva] = []
        self.edad:int= edad
        self.nacionalidad:str = nacionalidad
        self.genero:str = genero

    def hacer_reserva(self, vuelo:Vuelo):
        nueva_reserva:Reserva = Reserva(self, vuelo)
        self.reservas.append(nueva_reserva)
        vuelo.agregar_reserva(nueva_reserva)
        print(f"Reserva creada para el vuelo {vuelo.numero_vuelo}")

    def mostrar_reservas(self):
        for reserva in self.reservas:
            reserva.mostrar_info()

    def pagar_vuelo(self):
        for i in self.reservas:
            print(f"{i}.{(self.reservas[i]).vuelo.mostrar_info()}")
        eleccion=input(int("elige una opcion para pagar: "))
        print(f"vuelo pagado por el valor de {self.reservas[eleccion].vuelo.tarifa}")
