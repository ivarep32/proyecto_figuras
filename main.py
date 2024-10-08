from lib import cuadrado,triangulo, rectangulo
from proyecto_figuras_remoto.lib import circunferencia

print("Proyecto Figuras")
print(cuadrado.get_identificador())
lado=4
print(f"El area de un {cuadrado.get_identificador()} de lado {lado} es:{cuadrado.get_area(lado)} y el perímmetro es\
       {cuadrado.get_perimetro(lado)}")

base=4
altura=2
print(triangulo.get_identificador())
print(f"El área de un {triangulo.get_identificador()} de base\
      {base} y altura {altura} es: {triangulo.get_area(base,altura)} y  el\
      perímetro es {triangulo.get_perimetro(base,base,base)}")

base=4
altura=2
print(rectangulo.get_identificador())
print(f"El area de un {rectangulo.get_identificador()} de base {base}\
      y altura {altura} es: {rectangulo.get_area(base,altura)} \
        y el perímetro es: {rectangulo.get_perimetro(base,altura)}")

radio = 0.5
print("Circunferencia: ")
print(f"El area de una circunferencia de radio {radio} \
      es {circunferencia.get_area(radio)}")
