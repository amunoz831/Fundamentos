from datetime import datetime

class Vuelo:
    tarifas_base = {
        ("Madrid", "Londres"): 150,
        ("Madrid", "París"): 120,
        ("Madrid", "Nueva York"): 450,
        ("Londres", "Nueva York"): 400,
        ("París", "Berlín"): 100,
        # Añade más trayectos si es necesario
        }
    def __init__(self, numero_vuelo:int, origen, destino, asientos, fecha_imcio:datetime, fecha_final:datetime):
        self.numero_vuelo = numero_vuelo
        self.origen = origen
        self.destino = destino
        self.asientos_disponibles = asientos
        self.reservas = []
        self.activo = True
        self.tarifa:int=0

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


    def calcular_tarifa(self):
        # Buscamos si existe una tarifa base para el trayecto origen-destino
        trayecto = (self.origen, self.destino)
        tarifa = self.tarifas_base.get(trayecto)
        
        if tarifa is None:
            # Si el trayecto no existe en la lista de tarifas base, asignamos una tarifa estándar
            print(f"No se encontró una tarifa predefinida para el trayecto {self.origen} - {self.destino}.")
            tarifa = 1550  # Tarifa por defecto, puedes ajustarla
        self.tarifa=tarifa
        return tarifa