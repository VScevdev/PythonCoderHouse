from paquete1 import Cliente, GestorClientes

def main():
    c1 = Cliente("Valentin", "vale@mail.com", 27, 1000)
    c2 = Cliente("Ana", "ana@mail.com", 22)

    gestor = GestorClientes()
    gestor.agregar(c1)
    gestor.agregar(c2)

    print("Clientes cargados:")
    gestor.mostrar_todos()

    print("\nProbando métodos:")
    print("Nuevo saldo de Valentin:", c1.actualizar_saldo(500))
    print("¿Ana es mayor de edad?", c2.es_mayor_de_edad())

if __name__ == "__main__":
    main()


