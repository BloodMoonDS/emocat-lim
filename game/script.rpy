# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define e = Character("Eileen")


# El juego comienza aquí.
define hugo = Character("hugo",color="#00FBFE")
define alice = Character("alice",color="#f600fe")
define kenia = Character("kenia",color="#ff7e7e")

label start:

    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.
    "Quien soy?"
    "Estoy aqui?"
    "hmmm"
    "de igual manera tengo que despertar..."
    scene bg hugoroom


    show hugo tired
    hugo "..."
    hugo "supongo que tengo que ir a la escuela"
    show hugo look
    hugo "...?"
    hugo "¿Me estas mirando?"
    show hugo happy
    hugo "¿puedes ayudarme?"
    hugo "En ese caso te doy el control de mi cuerpo"
    scene bg blackbg
    "*de la nada sientes como tomas el control de hugo y puedes ayudar a controlar sus pensamientos*"
    scene bg hugoroom
    "*abres los ojos*"
    "*en definitiva tienes el control de hugo*"
    show alice base
    alice "Hugo ya es tarde no vas a ir a la esc-"
    show alice happy
    alice "Oh ya te has despertado, Genial! pense que ibas a tardar más"
    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.
    scene bg car
    "*vas de camino a la escuela, te sientes ansioso*"
    "*este paisaje se siente raro*"
    "*Hmmmmm*"
    "*¿por que el paisaje se siente tan vacio?*"
    scene bg schoolout
    "*al fin llegamos...*"
    show kenia happy
    kenia "Holi!"
    # Presenta las líneas del diálogo.
    menu:
        "Hola ¿como estas?":
            jump choice_open_kania1
        "Hola e-e-estas linda jeje":
            jump choice_open_kania2
    label choice_open_kania1:
        kenia "Bien todo bien jeje"
        jump choice_common
    label choice_open_kania2:
        show kenia blush
        kenia "ehhhh? ese es... un cumplido? ay jeje ¡gracias!"
        show kenia happy
        jump choice_common
    label choice_common:
        kenia "como sea hay que hacer varios trabajos asi que bueno entremps al salon"
    # Finaliza el juego:

    return
