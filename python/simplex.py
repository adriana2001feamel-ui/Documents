import numpy as np
from scipy.optimize import linprog

# ----------------------------------------------------
# 1. Definir la Función Objetivo (Maximización)
# ----------------------------------------------------
# SciPy linprog minimiza. Para MAXIMIZAR Z, minimizamos -Z.
# Coeficientes de la función objetivo: Z = 5x1 + 4x2
# Coeficientes para la minimización: C = [-5, -4]
c = [-5, -4]

# ----------------------------------------------------
# 2. Definir las Restricciones (Lado Izquierdo)
# Todas deben ser del tipo "menor o igual a" (<=)
# ----------------------------------------------------
# Matriz de coeficientes de las restricciones (A_ub)
#   [6, 4]  (6x1 + 4x2)
#   [1, 2]  (x1 + 2x2)
#   [-1, 1] (-x1 + x2)
#   [0, 1]  (x2)
A_ub = [
    [6, 4],
    [1, 2],
    [-1, 1],
    [0, 1]
]

# ----------------------------------------------------
# 3. Definir los Límites de las Restricciones (Lado Derecho)
# ----------------------------------------------------
# Lados derechos (b_ub)
#   [24]
#   [6]
#   [1]
#   [2]
b_ub = [24, 6, 1, 2]

# ----------------------------------------------------
# 4. Definir los Límites de las Variables (x1, x2)
# ----------------------------------------------------
# Las variables x1 y x2 son no negativas (>= 0)
x1_bounds = (0, None) # 0 a infinito
x2_bounds = (0, None)
bounds = [x1_bounds, x2_bounds]

# ----------------------------------------------------
# 5. Resolver el Problema con el Método Simplex
# ----------------------------------------------------
# method='simplex' especifica el algoritmo
res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')

# ----------------------------------------------------
# 6. Mostrar los Resultados
# ----------------------------------------------------
print("--- SOLUCIÓN DE MAXIMIZACIÓN SIMPLEX ---")
if res.success:
    # El valor óptimo de SciPy es el MINIMIZADO, hay que negarlo
    valor_Z_optimo = -res.fun
    
    print(f"Estado de la Solución: {res.message}")
    print(f"Valor Máximo de Z: {valor_Z_optimo:.4f}")
    print(f"Valor Óptimo de x1: {res.x[0]:.4f}")
    print(f"Valor Óptimo de x2: {res.x[1]:.4f}")
else:
    print(f"La optimización no fue exitosa. Mensaje: {res.message}")