import numpy as np


media1 = 99.84
desviacion_estandar1 = 31.12
Shift1 = np.random.normal(media1, desviacion_estandar1)
Shift1 = round(Shift1)

media2 = 93.14
desviacion_estandar2 = 23.26
Shift2 = np.random.normal(media2, desviacion_estandar2)
Shift2 = round(Shift2)

media3 = 90.28
desviacion_estandar3 = 37.57
Shift3 = np.random.normal(media3, desviacion_estandar3)
Shift3 = round(Shift3)


print(f"Producción estimada para Shift 1: {Shift1}")
print(f"Producción estimada para Shift 2: {Shift2}")
print(f"Producción estimada para Shift 3: {Shift3}")
