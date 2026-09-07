Gestor de Finanzas Personales (CLI)

Simulador de línea de comandos en Python para administrar el saldo y la deuda
de una tarjeta de crédito. Permite registrar pagos y simular compras,
validando siempre los montos ingresados por el usuario.

## Características

- Menú interactivo por consola
- Validación de entradas (montos negativos, no numéricos, deuda/saldo insuficiente)
- Modelo de datos con `dataclass` para representar el estado de la cuenta
- Código organizado en funciones con responsabilidad única

## Tecnologías

- Python 3

## Cómo ejecutarlo

```bash
python gestor_finanzas.py
```

## Posibles mejoras futuras

- Persistir el historial de movimientos en un archivo o base de datos
- Agregar tests unitarios con `pytest`
- Construir una interfaz web simple con Flask

## Autor

Martín Cisternas — Analista Programador en formación, Duoc UC.
