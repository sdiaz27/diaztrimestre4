
usuarios = {
    "juan": "123456",
    "ana": "67890",
    "maria": "12345",
}


def comprobacion (usuario, contraseña):
    
    c=usuario in usuarios and contraseña == usuarios[usuario]
    return c

def permitir_acceso(func):

    def validacion(*args, **kwargs):
        
        usuario = input("Ingrese su usuario: ")
        contraseña = input("Ingrese su contraseña: ")

        if comprobacion(usuario, contraseña):
            print("Bienvenido!")
            return func(*args, **kwargs)
        else:
            print("Usuario o contraseña incorrectos.")

    return validacion

@permitir_acceso
def acecso():
    print("As ingresado exitosamente")


acecso()
