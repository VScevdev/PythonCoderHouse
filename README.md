# TuModeloDeClientes (Proyecto Python)

Este proyecto implementa un pequeño modelo de clientes utilizando programación orientada a objetos. Incluye:
- Una clase `Cliente`.
- Métodos para actualizar el saldo y verificar si un cliente es mayor de edad.
- Lectura y escritura de datos en un archivo JSON.
- Organización modular en (`paquete1`).
- Un archivo `main.py` para probar todas las funcionalidades.

---

## Clase Cliente
La clase `Cliente` representa a un usuario. Sus atributos y métodos principales:

### Atributos
- `nombre` (str)
- `email` (str)
- `edad` (int)
- `saldo` (float, opcional)

### Métodos
- `__str__(self)` → Representación legible del cliente.
- `actualizar_saldo(self, monto)` → Suma o resta saldo.
- `es_mayor_de_edad(self)` → Devuelve un mensaje indicando si es mayor de edad.

---

## Funciones utilitarias
En `modulo_utils.py` se maneja:
- Carga del archivo JSON.
- Guardado de datos.
- Generación de clientes desde información en JSON.

---

## Archivo JSON
El archivo `clientes.json` almacena la lista de clientes en formato estructurado.


