def contar_a(cadena):
    
    cadena_minuscula = cadena.lower()
    cantidad_a = cadena_minuscula.count('a')
    return cantidad_a

texto = "Que tal vos ¿Como estas?"
resultado = contar_a(texto)
print(f"La cantidad de letras 'A' o 'a' es: {resultado}")
