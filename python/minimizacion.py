import numpy as np
from scipy.optimize import linprog

# 1. Función Objetivo (Minimización): Z = 3y1 + 2y2
c_min = [3, 2] # No se niega

# 2. Restricciones transformadas a tipo "<="
#   [-1, -1]  (-y1 - y2)
#   [-2, 1]   (-2y1 + y2)
A_ub_min = [
    [-1, -1],
    [-2, 1]
]

# 3. Lados derechos de las restricciones transformadas
b_ub_min = [-10, -5]

# 4. Límites de las variables
y1_bounds = (0, None)
y2_bounds = (0, None)
bounds_min = [y1_bounds, y2_bounds]

# 5. Resolver el Problema
res_min = linprog(c_min, A_ub=A_ub_min, b_ub=b_ub_min, bounds=bounds_min, method='highs')

# 6. Mostrar los Resultados
print("\n--- SOLUCIÓN DE MINIMIZACIÓN SIMPLEX ---")
if res_min.success:
    print(f"Estado de la Solución: {res_min.message}")
    print(f"Valor Mínimo de Z: {res_min.fun:.4f}")
    print(f"Valor Óptimo de y1: {res_min.x[0]:.4f}")
    print(f"Valor Óptimo de y2: {res_min.x[1]:.4f}")
else:
    print(f"La optimización no fue exitosa. Mensaje: {res_min.message}")