from datetime import datetime, date
class Pasaporte:
    def __init__(self, numero:int, pais_emision:str, fecha_emision:datetime, fecha_expiracion:datetime):
        self.numero:int = numero
        self.pais_emision:str = pais_emision
        self.fecha_emision:datetime = fecha_emision
        self.fecha_expiracion:datetime = fecha_expiracion

    def mostrar_info(self):
        print(f"Pasaporte Número: {self.numero}")
        print(f"País de Emisión: {self.pais_emision}")
        print(f"Fecha de Emisión: {self.fecha_emision}")
        print(f"Fecha de Expiración: {self.fecha_expiracion}")
    
    def es_valido(self):
        # Aquí se podría implementar una lógica para validar si el pasaporte está vigente
        hoy = date.today()
        return hoy < self.fecha_expiracion


# Crear un pasaporte de ejemplo
pasaporte = Pasaporte("123456789", "España", date(2020, 1, 15), date(2030, 1, 15))

# Mostrar información del pasaporte
pasaporte.mostrar_info()

# Comprobar si el pasaporte es válido
if pasaporte.es_valido():
    print("El pasaporte es válido.")
else:
    print("El pasaporte ha expirado.")