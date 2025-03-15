import matplotlib.pyplot as plt
import numpy as np

# Ecuación de la recta: 2x + 5y + 31 = 0
# y = (-2/5)x - 31/5

# Valores para x
x = np.linspace(-20, 10, 100)
y = (-2/5)*x - 31/5

# Puntos importantes
A = (-15.5, 0)  # Intersección con el eje x
B = (0, -31/5)  # Intersección con el eje y
P = (-3, -5)    # Punto dado

# Graficar la recta
plt.figure(figsize=(8, 6))
plt.plot(x, y, label="2x + 5y + 31 = 0", color="blue")

# Marcar los puntos
plt.plot(A[0], A[1], 'ro', label=f'A{A}')
plt.plot(B[0], B[1], 'go', label=f'B{B}')
plt.plot(P[0], P[1], 'bo', label=f'P{P}')

# Etiquetas y estilo
plt.axhline(0, color='black', linewidth=0.7, linestyle='--')
plt.axvline(0, color='black', linewidth=0.7, linestyle='--')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Gráfico de la recta y puntos importantes')
plt.grid(True)
plt.legend()
plt.show()
