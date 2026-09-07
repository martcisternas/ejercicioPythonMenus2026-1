"""
Gestor de Finanzas Personales (CLI)
------------------------------------
Simulador de línea de comandos para administrar el saldo disponible
y la deuda de una tarjeta de crédito: permite registrar pagos y
simular compras, validando siempre los montos ingresados.

Autor: Martín Cisternas
"""

from dataclasses import dataclass


@dataclass
class CuentaTarjeta:
    """Representa el estado financiero de una tarjeta de crédito."""
    saldo: float
    deuda: float

    def pagar(self, monto: float) -> None:
        """Abona `monto` a la deuda, sin superar el total adeudado."""
        if monto <= 0:
            print("El monto a pagar debe ser mayor a cero.")
            return
        if monto > self.deuda:
            print(f"El monto excede la deuda actual (${self.deuda:,.0f}).")
            return
        self.deuda -= monto
        self.saldo += monto
        print(f"Pago exitoso. Deuda restante: ${self.deuda:,.0f}")

    def comprar(self, monto: float) -> None:
        """Registra una compra: descuenta del saldo y aumenta la deuda."""
        if monto <= 0:
            print("El monto de la compra debe ser mayor a cero.")
            return
        if monto > self.saldo:
            print(f"Saldo insuficiente. Disponible: ${self.saldo:,.0f}")
            return
        self.saldo -= monto
        self.deuda += monto
        print(f"Compra registrada. Saldo disponible: ${self.saldo:,.0f}")


def pedir_monto(mensaje: str) -> float:
    """Solicita un monto numérico al usuario, validando la entrada."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Ingresa un valor numérico válido.")


def mostrar_menu() -> None:
    print("\n--- GESTOR DE FINANZAS ---")
    print("1. Pagar tarjeta de crédito")
    print("2. Simular compra")
    print("3. Salir")


def main() -> None:
    cuenta = CuentaTarjeta(saldo=400_000, deuda=100_000)

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            cuenta.pagar(pedir_monto("Monto a pagar: $"))
        elif opcion == "2":
            cuenta.comprar(pedir_monto("Monto de la compra: $"))
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    main()
