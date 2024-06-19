def union_of_words(array):
    """
    Función encargada de unir las palabras contiguas a las preposiciones.

    Parameters:
    array (list): Lista de palabras que se van a procesar.

    Returns:
    list: Lista de palabras con las preposiciones unidas a las palabras contiguas.
    """
    # Lista de preposiciones que se utilizarán para unir palabras contiguas
    prepositions = ["de", "del", "la", "las", "lo", "los", "de las", "de los"]
    
    result = []  # Lista que almacenará el resultado final
    i = 0  # Índice inicial para recorrer la lista de palabras
    while i < len(array):  # Bucle para recorrer toda la lista de palabras
        # Comprobación de si la palabra actual es una preposición
        if array[i].lower() in prepositions:
            if i < len(array) - 1:  # Verifica que no se salga del índice de la lista
                # Se une la preposición a la palabra contigua y se añade al resultado
                result.append(array[i] + " " + array[i+1])
                i += 1  # Incrementa el índice para saltar la palabra que ya se ha unido
        else:
            # Si la palabra no es una preposición, se añade tal cual al resultado
            result.append(array[i])
        i += 1  # Incrementa el índice para pasar a la siguiente palabra
    return result

# Lista de ejemplo para ser procesada
data = ["Jose", "De", "los", "Angeles", "Portillo", "gutierrez"]

# Primera llamada a la función para procesar la lista de palabras
res = union_of_words(data)

# Impresion de la primera lista de data organizada.
print(res)

# Segunda llamada a la función para procesar nuevamente la lista de palabras
resp = union_of_words(res)

# Impresión del resultado final después de procesar la lista dos veces
print(resp)
