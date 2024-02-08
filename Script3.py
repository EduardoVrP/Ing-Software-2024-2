import matplotlib.pyplot as plt

# Definir la función
def f(x):
    return (x*x) + 2

# Generar valores de x
x = []
i=-10
while i <= 10:
    x.append(i)
    i = i + 0.1

# Calcular los valores de y
y = [f(xi) for xi in x]

# Crear el gráfico
print(y[100])
plt.plot(x, y)

# Agregar etiquetas y título
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráfico de f(x) = x^2 + 2')

# Mostrar el gráfico
plt.grid(True)
plt.show()