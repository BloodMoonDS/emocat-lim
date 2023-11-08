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
    with fade

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
    play music "audio/city.ogg" 
    with fade
    "*vas de camino a la escuela, te sientes ansioso*"
    "*este paisaje se siente raro*"
    "*Hmmmmm*"
    "*¿por que el paisaje se siente tan vacio?*"
    scene bg schoolout
    "*al fin llegamos...*"
    show kenia happy
    kenia "Holi!"
    "*Sentiriras mariposas en el estomago*"
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
        jump choice_love
    label choice_common:
        scene bg classroom
        with fade
        kenia "como sea hay que hacer varios trabajos asi que bueno entremos al salon"
        show kenia happy
        kenia "bien empezemos a hacer el proyecto"
        "Y de que va el proyecto"
        kenia "De lo que sea"
        menu:
            "Crisis Existenciales":
                jump crisis
            "No se":
                jump idk_notlove
            "pensemos eso mas tarde":
                jump laternotlove
        jump game_end
    label choice_love:
        show kenia happy
        kenia "bien hay que hacer varios trabajos asi vamonos"
        scene bg classroom
        with fade
        show kenia happy
        kenia "hay que empezar el proyecto"
        kenia "jeje..."
        "Y de que va el proyecto"
        kenia "Hay que hacer un cartel sobre... la verdad dijo de lo que sea jiji"
        jump game_end
    # Finaliza el juego:
    label love_project:

    label common_project:

 
    label crisis:
        kenia "Hmmmmmm..."
        kenia "Esta interesante el tema"
        "*Se te hace muy atractiva pero... al tener los recuerdos de hugo...*"
        "*sientes que algo va a salir mal*"
        "*¿Te arriesgas?*"
        menu:
            "Si":
                jump risk1
            "No":
                jump risk2
    label idk_notlove:

    label laternotlove:


    
    label risk1:
        "Oye quiero decirte algo..."
        kenia "¿que sucede?"
        kenia "¿todo bien?"
        "Quiero decirte que..."
        kenia "uh?"
        "Te me haces atractiva jeje"
        "*Sonries sonrojado y nervioso*"
        play music "audio/PairTension.ogg"
        show kenia think
        kenia "..."
        kenia "jeje"
        kenia "ehhh sabes yo tambien queria decirte algo jeje"
        kenia "hmmmmm"
        kenia "ehhhh..."
        show kenia blush
        kenia "Tu tambien me gustas jeje"
        kenia "solo que no sabia como decirtelo jeje"
        kenia "a mi me cuesta decir lo que siento por traumas"
        "oh..."
        kenia "ehhh"
        "¿sabes?"
        "Yo dudé si en decirtelo o no jeje"
        "Tambien tengo traumas"
        "unos bastante fuertes"
        "pero..."
        "¿quieres hacer algo?"
        kenia "vamos a relajarnos un poco jeje"
        "Vale! me agrada la idea!"
        jump date
        label risk2:

        label date:
            scene bg blackbg
            with fade
            "*Te preparas para la cita*"
            "*esperas a que todo salga genial*"
            play music "audio/city.ogg"
            scene bg dinnerrestaurant
            with fade
            "*Esperas*"
    label game_end:

    return
