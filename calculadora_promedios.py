'''
Calculadora de promedios

Desarrollo de una calculadora de promedios escolares en Python utilizando variables, operadores, estructuras de control y funciones básicas.

'''
def ingresar_calificaciones():
    ''' Función para ingresar las materias y sus calificaciones. Valida que las calificaciones estén entre 0 y 10.
    Args: 
        None
    Returns:
        Una tupla con dos listas: la primera contiene los nombres de las materias y la segunda contiene las calificaciones correspondientes.
    Raises:
        ValueError si la calificación ingresada no es un número válido.
    '''
    materias = []
    calificaciones = []
    while True:
        # Validación de entrada de calificaciones para cada materia.
        materia = input("Ingrese el nombre de la materia: ")
        while True:
            try:
                calificacion = float(input("Ingrese la calificación de la materia: "))
                if 0 <= calificacion <= 10:
                    calificaciones.append(calificacion)
                    materias.append(materia)
                    break
                else:
                    print("La calificación debe estar entre 0 y 10. Intente nuevamente.")
            except ValueError:
                print("Por favor, ingrese un número válido para la calificación.")
        
        # Validación de entrada para continuar con registro de materias.
        while True:
            continuar = input("¿Desea ingresar otra materia? (s/n): ")
            if continuar.lower() == 's' or continuar.lower() == 'n':
                break
            else:
                print("Por favor, ingrese 's' para sí o 'n' para no.")
        
        # Solo sale del ciclo de registro si la entrada es n.
        if continuar.lower() == 'n':
            break

    return materias, calificaciones

def calcular_promedio(calificaciones):
    ''' Función para calcular el promedio de las calificaciones. 
    Args: 
        calificaciones (list): Una lista de calificaciones numéricas.
    Returns: 
        El promedio de las calificaciones. Si la lista está vacía, devuelve 0.
    Raises: 
        None
    '''
    
    return sum(calificaciones) / len(calificaciones) if calificaciones else 0

def determinar_estado(calificaciones, umbral):
    ''' Función para determinar qué materias están aprobadas y cuáles están reprobadas según un umbral dado.
    Args: 
        calificaciones (list): Una lista de calificaciones numéricas.
        umbral (float): El umbral para determinar si una materia está aprobada o reprobada.
    Returns: 
        Una tupla con dos listas: la primera contiene los índices de las materias aprobadas y la segunda contiene los índices de las materias reprobadas. Si la lista de calificaciones está vacía, devuelve (None, None).
    Raises: 
        None
    '''
    if not calificaciones:
        return None, None
    id_reprobadas = []
    id_aprobadas = []
    for i, calificacion in enumerate(calificaciones):
        if calificacion < umbral:
            id_reprobadas.append(i)
        else:
            id_aprobadas.append(i)
    return id_aprobadas, id_reprobadas

def encontrar_extremos(calificaciones):
    ''' Función para encontrar la calificación máxima y mínima de una lista de calificaciones.
    Args: 
        calificaciones (list): Una lista de calificaciones numéricas.
    Returns: 
        Una tupla con los indices de las materias con la calificación máxima y mínima. Si la lista está vacía, devuelve (None, None).
    Raises: 
        None
    '''
    if not calificaciones:
        return None, None
    max_calificacion = max(calificaciones) if calificaciones else None
    min_calificacion = min(calificaciones) if calificaciones else None
    
    idx_max = calificaciones.index(max_calificacion)
    idx_min = calificaciones.index(min_calificacion)
   
    return idx_max, idx_min

def main():
    ''' Función principal que ejecuta la calculadora de promedios escolares.
    Args: 
        None
    Returns:
        None
    Raises:
        None
    '''
    
    print("Bienvenido a la Calculadora de Promedios Escolares")
    materias, calificaciones = ingresar_calificaciones()
    if calificaciones:
        promedio = calcular_promedio(calificaciones)
        print(f"El promedio de las calificaciones es: {promedio:.2f}")
        
        umbral = 5.0
        id_aprobadas, id_reprobadas = determinar_estado(calificaciones, umbral)
        
        idx_max, idx_min = encontrar_extremos(calificaciones)
        
        for i, materia in enumerate(materias):
            print(f"{materia}: {calificaciones[i]}")
        print(f"Materias aprobadas: {[materias[i] for i in id_aprobadas]}")
        print(f"Materias reprobadas: {[materias[i] for i in id_reprobadas]}")
        print(f"Materia con la calificación más alta: {materias[idx_max]} con una calificación de {calificaciones[idx_max]}")
        print(f"Materia con la calificación más baja: {materias[idx_min]} con una calificación de {calificaciones[idx_min]}")
    else:
        print("No se ingresaron calificaciones. No se puede calcular el promedio ni determinar el estado de las materias.")
    
    print ("Gracias por usar la Calculadora de Promedios Escolares. ¡Hasta luego!")

if __name__ == "__main__":
    main()