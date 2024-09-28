def solicitar_numero():
    while True:
        try:
            numero = int(input("Ingrese unnumero entero: "))  
            return numero  
        except ValueError:
            print("Por favor, ingrese un numero entero válido.")  

def mostrar_cuadrado(numero):
    
    cuadrado = numero ** 2  
    print(f"El cuadrado de {numero} es:{cuadrado}")  

def solicitar_dos_numeros():
    while True:
        try:
            numero1 = int(input("Ingrese el primer numero entero: "))  
            numero2 = int(input("Ingrese el segundo nnumero entero: ")) 
            return numero1, numero2  
        except ValueError:
            print("Error, ingrese 1 numero entero real.")

def mostrar_producto(numero1, numero2):
    
    producto = numero1 * numero2  
    print(f"El producto de {numero1}y{numero2} es: {producto}")  
if __name__ == "__main__":
    numero_ingresado = solicitar_numero()  
    mostrar_cuadrado(numero_ingresado)  

    
    numero1, numero2 = solicitar_dos_numeros()  
    mostrar_producto(numero1, numero2)  
