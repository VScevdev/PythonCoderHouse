from .modulo_clientes import Cliente
import json
import os

ruta_archivo = "clientes.json"

def cargar_archivo():
    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, "r", encoding="utf-8") as file:
            return json.load(file)
    else:
        return []

def guardar_archivo(datos):
    with open(ruta_archivo, "w", encoding="utf-8") as file:
        json.dump(datos, file, indent=4)

class GestorClientes:
    def __init__(self):
        self.clientes = []

    def agregar(self, cliente):
        self.clientes.append({
            "nombre": cliente.nombre,
            "email": cliente.email,
            "edad": cliente.edad,
            "saldo": cliente.saldo
        })
        guardar_archivo(self.clientes)

    def mostrar_todos(self):
        for datos in self.clientes:
            obj = Cliente(datos["nombre"], datos["email"], datos["edad"], datos["saldo"])
            print(obj)