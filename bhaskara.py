import math

# Y =ax² + bx + c

a = float(input("Digite o primeiro coeficiente da sua equação: "))
b = float(input("Digite o segundo coeficiente da sua equação: "))
c = float(input("Digite o terceiro coeficiente da sua equação: "))

raiz1 = (-b + math.sqrt(b*b - 4*a*c))/2*a

raiz2 = (-b - math.sqrt(b*b - 4*a*c))/2*a

print("\nAs raízes são %2.f e %.2f"%(raiz1,raiz2))