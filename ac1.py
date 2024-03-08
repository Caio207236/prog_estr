import cmath

def calcula_raizes(coeficiente_a, coeficiente_b, coeficiente_c):
    # Calcula o discriminante
    discriminante = (coeficiente_b ** 2 - 4 * coeficiente_a * coeficiente_c) ** 2 - 4 * (coeficiente_a ** 2 * coeficiente_b ** 2 - 4 * coeficiente_a * coeficiente_b * coeficiente_c + coeficiente_c ** 2)

    # Calcula as raízes usando a fórmula de Bhaskara
    delta_numerador = (discriminante ** (1/2) - (coeficiente_b ** 2 - 4 * coeficiente_a * coeficiente_c)) / (2 * 27 * coeficiente_a ** 3)
    delta_denominador = (9 * coeficiente_a ** 2)
    delta = delta_numerador / delta_denominador

    raiz1 = (-coeficiente_b / (2 * coeficiente_a) + cmath.sqrt(delta))
    raiz2 = (-coeficiente_b / (2 * coeficiente_a) - cmath.sqrt(delta))
    raiz3 = -0.5 * raiz1
    raiz4 = -0.5 * raiz2

    return raiz1, raiz2, raiz3, raiz4

# Solicita os coeficientes
coef_a = float(input("Digite o coeficiente A: "))
coef_b = float(input("Digite o coeficiente B: "))
coef_c = float(input("Digite o coeficiente C: "))

# Encontra as raízes
raizes = calcula_raizes(coef_a, coef_b, coef_c)

# Imprime as raízes
print("As raízes são:", raizes)