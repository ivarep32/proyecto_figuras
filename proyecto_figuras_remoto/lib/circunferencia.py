import math

def get_area(radio: float) -> float:
    return math.pi * (radio ** 2)

# Ejemplo de uso
radio = 5.0
area = get_area(radio)
print(f"El área del círculo con radio {radio} es {area}")
