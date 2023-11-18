import numpy as np


media1 = 99.84
desviacion_estandar1 = 31.12
Shift1 = np.random.normal(media1, desviacion_estandar1)
limite_inferior = 70
Shift1 = round(Shift1)
Shift1 = max(Shift1, limite_inferior)

media2 = 93.14
desviacion_estandar2 = 23.26
Shift2 = np.random.normal(media2, desviacion_estandar2)
Shift2 = round(Shift2)
Shift2 = max(Shift2, limite_inferior)

media3 = 90.28
desviacion_estandar3 = 37.57
Shift3 = np.random.normal(media3, desviacion_estandar3)
Shift3 = round(Shift3)
Shift3 = max(Shift3, limite_inferior)
def simulate_shift_with_production(lambda_fallas, mean_fallas, lambda_no_util, mean_no_util, shift_length_minutes,
                                   cycle_time=147):
    """
    Simula un turno completo de operación de la máquina e incluye cálculo de producción ideal.

    Parameters:
    lambda_fallas (float): tasa de llegada de fallas.
    mean_fallas (float): media de la duración de fallas.
    lambda_no_util (float): tasa de llegada de no utilización.
    mean_no_util (float): media de la duración de no utilización.
    shift_length_minutes (int): duración del turno en minutos.
    cycle_time (int): tiempo de ciclo ideal para producir una pieza, en segundos.

    Returns:
    dict: un diccionario que contiene el número total de eventos, las duraciones acumuladas y la producción ideal.
    """
    shift_length_seconds = shift_length_minutes * 60  # Convertir minutos a segundos
    clock = 0  # Reloj de simulación

    num_fallas = 0
    duration_fallas = 0

    num_no_util = 0
    duration_no_util = 0

    while clock < shift_length_seconds:
        # Generar el tiempo hasta el próximo evento
        time_to_falla = np.random.exponential(scale=1 / lambda_fallas)
        time_to_no_util = np.random.exponential(scale=1 / lambda_no_util)

        # Determinar qué evento ocurre primero y actualizar el estado de la máquina
        if time_to_falla < time_to_no_util:
            event_duration = np.random.exponential(scale=mean_fallas)
            num_fallas += 1
            duration_fallas += event_duration
        else:
            event_duration = np.random.exponential(scale=mean_no_util)
            num_no_util += 1
            duration_no_util += event_duration

        # Actualizar el reloj de simulación
        clock += min(time_to_falla, time_to_no_util) + event_duration

    # Calcular la producción ideal basada en el tiempo de operación efectivo
    effective_operation_time = shift_length_seconds - duration_fallas - duration_no_util
    ideal_production = effective_operation_time // cycle_time

    #Se divide entre 60 para representarlo en minutos
    return {
        'num_fallas': num_fallas,
        'duration_fallas': duration_fallas / 60,
        'num_no_util': num_no_util,
        'duration_no_util': duration_no_util / 60,
        'down_time': (duration_fallas + duration_no_util) / 60,
        'ideal_production': ideal_production
    }

def format_results(shift_number, results, real_prod):
    """
    Formatea y devuelve una cadena de caracteres que representa los resultados de un turno de manera legible.
    """
    formatted_str = f"Shift {shift_number} Results:\n"
    formatted_str += '-' * 30 + '\n'
    for key, value in results.items():
        formatted_str += f"{key.replace('_', ' ').title()}: {value}\n"
    formatted_str += f"Real Production: {real_prod}\n"
    formatted_str += '-' * 30
    return formatted_str

# Ejemplo de uso:
result_shift_1 = simulate_shift_with_production(1 / (420 * 60), 251.67, 1 / (420 * 60), 544.21, 420, 147)
result_shift_2 = simulate_shift_with_production(1 / (395 * 60), 251.67, 1 / (395 * 60), 544.21, 395, 147)
result_shift_3 = simulate_shift_with_production(1 / (450 * 60), 251.67, 1 / (450 * 60), 544.21, 450, 147)

formatted_result_shift_1 = format_results("1", result_shift_1, Shift1)
formatted_result_shift_2 = format_results("2", result_shift_2, Shift2)
formatted_result_shift_3 = format_results("3", result_shift_3, Shift3)

print(formatted_result_shift_1)
print(formatted_result_shift_2)
print(formatted_result_shift_3)


# Parámetros mejorados para una máquina más eficiente
mean_fallas_mejorado = 200  # Reducción en la duración de las fallas
cycle_time_mejorado = 147 #Tiempo de Ciclo modificable


# Simulación con los parámetros mejorados
result_shift_1_mejorado = simulate_shift_with_production(0.6 / (420 * 60), mean_fallas_mejorado, 0.6 / (420 * 60), 544.21, 420, cycle_time_mejorado)
result_shift_2_mejorado = simulate_shift_with_production(0.6 / (395 * 60), mean_fallas_mejorado, 0.6 / (395 * 60), 544.21, 395, cycle_time_mejorado)
result_shift_3_mejorado = simulate_shift_with_production(0.6 / (450 * 60), mean_fallas_mejorado, 0.6 / (450 * 60), 544.21, 450, cycle_time_mejorado)

#Shift mejorado
media = 130
desviacion_estandar = 10

Up_Shift1 = np.random.normal(media, desviacion_estandar)
limite_inferior2 = 110
Up_Shift1 = round(Up_Shift1)
Up_Shift1 = max(Up_Shift1, limite_inferior2)


Up_Shift2 = np.random.normal(media, desviacion_estandar)
Up_Shift2 = round(Up_Shift2)
Up_Shift2 = max(Up_Shift2, limite_inferior2)


Up_Shift3 = np.random.normal(media, desviacion_estandar)
Up_Shift3 = round(Up_Shift3)
Up_Shift3 = max(Up_Shift3, limite_inferior2)

# Formateo y presentación de los resultados
formatted_result_shift_1_mejorado = format_results("1 Mejorado", result_shift_1_mejorado, Up_Shift1)
formatted_result_shift_2_mejorado = format_results("2 Mejorado", result_shift_2_mejorado, Up_Shift2)
formatted_result_shift_3_mejorado = format_results("3 Mejorado", result_shift_3_mejorado, Up_Shift3)

print(formatted_result_shift_1_mejorado)
print(formatted_result_shift_2_mejorado)
print(formatted_result_shift_3_mejorado)

