class Usuario:
    def __init__(self, nombre:str, email:str):
        self.nombre:str = nombre
        self.email:str = email
    
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Email: {self.email}")