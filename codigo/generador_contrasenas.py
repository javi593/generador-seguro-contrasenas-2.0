import secrets
import string


def validar_paso_a_paso(contrasena):
    
    if len(contrasena) < 12:
        print("Error: la contraseña debe tener mínimo 12 caracteres.")
        return False


    tiene_mayuscula = False

    for caracter in contrasena:
        if caracter.isupper():
            tiene_mayuscula = True

    if tiene_mayuscula == False:
        print("Error: la contraseña debe tener al menos una letra mayúscula.")
        return False

    tiene_minuscula = False

    for caracter in contrasena:
        if caracter.islower():
            tiene_minuscula = True

    if tiene_minuscula == False:
        print("Error: la contraseña debe tener al menos una letra minúscula.")
        return False

    tiene_numero = False

    for caracter in contrasena:
        if caracter.isdigit():
            tiene_numero = True

    if tiene_numero == False:
        print("Error: la contraseña debe tener al menos un número.")
        return False

    simbolos = "!@#$%&*+-_?"
    tiene_simbolo = False

    for caracter in contrasena:
        if caracter in simbolos:
            tiene_simbolo = True

    if tiene_simbolo == False:
        print("Error: la contraseña debe tener al menos un símbolo especial.")
        print("Símbolos permitidos: ! @ # $ % & * + - _ ?")
        return False

    return True


def pedir_contrasena_valida():
    while True:
        contrasena = input("Ingrese una contraseña segura: ")

        if validar_paso_a_paso(contrasena):
            print("-----------------------------------")
            print("Contraseña válida.")
            print("Cumple todas las medidas de seguridad.")
            print("-----------------------------------")
            return contrasena
        else:
            print("Ingrese nuevamente la contraseña.")
            print("-----------------------------------")


def generar_alternativa_segura(contrasena_inicial):
    mayusculas = string.ascii_uppercase
    minusculas = string.ascii_lowercase
    numeros = string.digits
    simbolos = "!@#$%&*+-_?"

    todos = mayusculas + minusculas + numeros + simbolos

    nueva_contrasena = ""

    nueva_contrasena = nueva_contrasena + secrets.choice(mayusculas)
    nueva_contrasena = nueva_contrasena + secrets.choice(minusculas)
    nueva_contrasena = nueva_contrasena + secrets.choice(numeros)
    nueva_contrasena = nueva_contrasena + secrets.choice(simbolos)

    for caracter in contrasena_inicial:
        if caracter != " ":
            nueva_contrasena = nueva_contrasena + caracter

    while len(nueva_contrasena) < 16:
        nueva_contrasena = nueva_contrasena + secrets.choice(todos)

    lista = list(nueva_contrasena)
    secrets.SystemRandom().shuffle(lista)

    resultado = ""

    for caracter in lista:
        resultado = resultado + caracter

    return resultado


def medir_seguridad(contrasena):
    puntaje = 0

    if len(contrasena) >= 16:
        puntaje = puntaje + 1

    for caracter in contrasena:
        if caracter.isupper():
            puntaje = puntaje + 1
            break

    for caracter in contrasena:
        if caracter.islower():
            puntaje = puntaje + 1
            break

    for caracter in contrasena:
        if caracter.isdigit():
            puntaje = puntaje + 1
            break

    simbolos = "!@#$%&*+-_?"

    for caracter in contrasena:
        if caracter in simbolos:
            puntaje = puntaje + 1
            break

    if puntaje == 5:
        return "Muy segura"
    elif puntaje == 4:
        return "Segura"
    else:
        return "Media"


def generar_contrasenas_mas_seguras(contrasena_inicial):
    print("CONTRASEÑAS MÁS SEGURAS GENERADAS")
    print("-----------------------------------")

    for i in range(1, 6):
        alternativa = generar_alternativa_segura(contrasena_inicial)
        seguridad = medir_seguridad(alternativa)

        print(i, ".", alternativa, "->", seguridad)

    print("-----------------------------------")


def programa_principal():
    print("==========================================")
    print(" GENERADOR Y VALIDADOR DE CONTRASEÑAS")
    print("==========================================")
    print("La contraseña debe cumplir estos requisitos:")
    print("1. Mínimo 12 caracteres")
    print("2. Al menos una mayúscula")
    print("3. Al menos una minúscula")
    print("4. Al menos un número")
    print("5. Al menos un símbolo especial")
    print("==========================================")

    continuar = "s"

    while continuar == "s":
        contrasena = pedir_contrasena_valida()

        generar_contrasenas_mas_seguras(contrasena)

        continuar = input("¿Desea ingresar otra contraseña? (s/n): ").lower()

        while continuar != "s" and continuar != "n":
            print("Error: responda solo con s o n.")
            continuar = input("¿Desea ingresar otra contraseña? (s/n): ").lower()

    print("Gracias por usar el sistema.")


programa_principal()
