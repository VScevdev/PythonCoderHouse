class Cliente:
    def __init__(self, nombre, email, edad, saldo=0):
        self.nombre = nombre
        self.email = email
        self.edad = edad
        self.saldo = saldo

    def __str__(self):
        return f"Cliente: {self.nombre} - Email: {self.email} - Saldo: {self.saldo}"

    def actualizar_saldo(self, monto):
        self.saldo = self.saldo + monto
        return self.saldo

    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return f"{self.nombre} es mayor de edad."
        else:
            return f"{self.nombre} NO es mayor de edad."