import math

def calcular_limite(texto):
    texto_limpio = texto.replace("math.pi", "pi").replace("pi", "math.pi")
    return float(eval(texto_limpio, {"math": math}))

# INPUT
a_input = input("Write the left endpoint of the interval: ")
a = calcular_limite(a_input)

b_input = input("Write the right endpoint of the interval: ")
b = calcular_limite(b_input)

f_x = input("Write the function to integrate: ")
method = input("Select Integration Method (LRM/RRM/MPM/TM): ").upper()

n = 1000

# FUNCTION TO EVALUATE f(x)
def f(x):
    return eval(
        f_x,
        {"math": math},
        {"x": x}
    )

# PROCESS
h = (b - a) / n
area = 0.0

if method == "LRM":
    for i in range(n):
        xi = a + i * h
        area += f(xi) * h

elif method == "RRM":
    for i in range(1, n + 1):
        xi = a + i * h
        area += f(xi) * h

elif method == "MPM":
    for i in range(n):
        xi = a + (i + 0.5) * h
        area += f(xi) * h

elif method == "TM":
    for i in range(n):
        x_left = a + i * h
        x_right = x_left + h
        area += ((f(x_left) + f(x_right)) / 2) * h

else:
    print("Invalid Method")
    exit()

# OUTPUT
print(f"\nIntegral ≈ {area}")
