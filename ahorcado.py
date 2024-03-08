# Juego del ahorcado en phyton
# 1 - Definir una palabra
# 2 - Numero definido de intentos
# 3 - Pedri al usuario que ingrese una letra a la vez
# Resultado de acierto o de partida

def ahorcado ():
    #Definimos palabra secreta
    palabra_secreta="barbaro"
    letras_adivinadas=[]
    #lista es pa almacenar las letras que concuerden con mi palabra
    intentos=5 #numero de intentos

    while intentos> 0:
        palabra_mostrada=""
        for letra in palabra_secreta:
            if letra in letras_adivinadas:
                palabra_mostrada += letra
            else:
                palabra_mostrada +="_ "
        print(palabra_mostrada)

        if palabra_mostrada == palabra_secreta:
                print("haz adivinado la palabra")
                break
            #pedir al usuario una letra
        letra_usuario=input("ingrese una letra: ")

            #verificar si la letra ha sido adivinada en letras adivinadas
        if letra_usuario in letras_adivinadas:
                print("ya has adivinado esa letra")
                continue
        if letra_usuario in palabra_secreta:
                print("bien, tu letra esta en la palabra")
                letras_adivinadas. append(letra_usuario)
        else:
                intentos -= 1
                print("incorrecto, pierdes un intento" + str(intentos))

        if intentos == 0:
                print("Lo siento, has agotado todos los intentos, la palabra era" + palabra_secreta)

#Llamar a la funcion
ahorcado()