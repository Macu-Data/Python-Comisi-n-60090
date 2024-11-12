def saludando():
    print("Hola gente estoy trabajando con GIT")
    saludando()

    def sumar (n1,n2):
        print("el resultado de la suma de n1 y n2 es de: ", n1 + n2)
        sumar(int(input("ingresa el primer numero: ")),int(input("ingrese el segundo numero: ")))  

    def dividir (n1,n2):
        print("el resultado de la division de n1 y n2 es de: ", n1 / n2)
        dividir(int(input("ingresa el primer numero: ")),int(input("ingrese el segundo numero: "))) 
    
