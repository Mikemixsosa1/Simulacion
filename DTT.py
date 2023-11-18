import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

# Cargar los datos de Excel
file_path = 'C:/Users/SOSAMIG/Desktop/WorkFlow/School/Simulación/DefDurationFaultAndNoUtilization.xlsx'  # Reemplaza con la ruta correcta
excel_data = pd.ExcelFile(file_path)

# Leer las hojas de interés
fallas_df = excel_data.parse('Fallas')
no_utilizacion_df = excel_data.parse('NoUtilization')


# Función para realizar el análisis exploratorio de los datos
def exploratory_analysis(data, title):
    # Estadísticas descriptivas
    desc_stats = data.describe()

    # Visualización de la distribución de los datos
    plt.figure(figsize=(14, 6))

    plt.subplot(1, 2, 1)
    sns.histplot(data, kde=True)
    plt.title(f'Histogram of {title}')

    plt.subplot(1, 2, 2)
    sns.boxplot(x=data)
    plt.title(f'Boxplot of {title}')

    plt.show()

    return desc_stats






# Puedes también ajustar una distribución a los datos si deseas
# Ajuste de una distribución exponencial a las duraciones de las fallas
params_fallas = stats.expon.fit(fallas_df['DurationStatus'])

# Ajuste de una distribución exponencial a las duraciones de no utilización
params_no_utilizacion = stats.expon.fit(no_utilizacion_df['DurationStatus'])

print(f'Parámetros de la distribución exponencial para fallas: {params_fallas}')
print(f'Parámetros de la distribución exponencial para no utilización: {params_no_utilizacion}')
