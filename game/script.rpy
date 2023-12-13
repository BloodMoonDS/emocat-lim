# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define e = Character("Eileen")
define sounds = ["audio/Voices/voice_hugo.ogg","audio/Voices/voice_alice.ogg","audio/Voices/voice_kenia.ogg","audio/Voices/voice_camacho.ogg","audio/Voices/voice_nick.ogg","audio/Voices/Voice_Leo.ogg"]

init python:
    def type_sound(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show": #if text's being written by character, spam typing sounds until the text ends
            snd = sounds[0]
            renpy.sound.play(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            
        elif event == "slow_done" or event == "end":
            renpy.sound.stop()
            #dumb way to do it but it works, dunno if it causes memory leaks but it's almost 6AM :v
    def type_sound_Alice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show": #if text's being written by character, spam typing sounds until the text ends
            snd = sounds[1]
            renpy.sound.play(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            
           


        elif event == "slow_done" or event == "end":
            renpy.sound.stop()
        
    def type_sound_kenia(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show": #if text's being written by character, spam typing sounds until the text ends
            snd = sounds[2]
            renpy.sound.play(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            
           


        elif event == "slow_done" or event == "end":
            renpy.sound.stop()

    def type_sound_camacho(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show": #if text's being written by character, spam typing sounds until the text ends
            snd = sounds[3]
            renpy.sound.play(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            
           


        elif event == "slow_done" or event == "end":
            renpy.sound.stop()
    def type_sound_nick(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show": #if text's being written by character, spam typing sounds until the text ends
            snd = sounds[4]
            renpy.sound.play(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            
           


        elif event == "slow_done" or event == "end":
            renpy.sound.stop()

    def type_sound_leo(event, interact=True, **kwargs):
            if not interact:
                return

            if event == "show": #if text's being written by character, spam typing sounds until the text ends
                snd = sounds[5]
                renpy.sound.play(snd)
                renpy.sound.queue(snd)
                renpy.sound.queue(snd)
                renpy.sound.queue(snd)
                renpy.sound.queue(snd)
                renpy.sound.queue(snd)
                renpy.sound.queue(snd)
                renpy.sound.queue(snd)
                renpy.sound.queue(snd)
                renpy.sound.queue(snd)
                renpy.sound.queue(snd)
                renpy.sound.queue(snd)
                renpy.sound.queue(snd)
                renpy.sound.queue(snd)
                renpy.sound.queue(snd)
                renpy.sound.queue(snd)
                renpy.sound.queue(snd)
                renpy.sound.queue(snd)
                renpy.sound.queue(snd)
                renpy.sound.queue(snd)
                renpy.sound.queue(snd)
                renpy.sound.queue(snd)
                renpy.sound.queue(snd)
                renpy.sound.queue(snd)
                renpy.sound.queue(snd)
                renpy.sound.queue(snd)
                renpy.sound.queue(snd)
                renpy.sound.queue(snd)
                renpy.sound.queue(snd)
                renpy.sound.queue(snd)
                renpy.sound.queue(snd)
                
            


            elif event == "slow_done" or event == "end":
                renpy.sound.stop()
# El juego comienza aquí.
define hugo = Character("hugo",color="#00FBFE",callback=type_sound)
define nick = Character("Nick",color="#fe0000",callback=type_sound_nick)
define alice = Character("alice",color="#f600fe",callback=type_sound_Alice)
define kenia = Character("kenia",color="#ff7e7e",callback=type_sound_kenia)
define camacho = Character("camacho",color="#73ff00",callback=type_sound_camacho)
define Leo = Character("Leo",color="#ff9900",callback=type_sound_leo)
label start:
    play music "audio/onestop.ogg" volume 0.5
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
    stop music
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
    play music "audio/city.ogg"  volume 0.5
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
        play sound "audio/SFX/choice_good2.ogg"
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
                jump work
            "pensemos eso mas tarde":
                jump work
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
        show camacho happy at right
        show kenia think
        camacho "¿Hola me puedo unir?"
        menu:
            "Si":
                jump camacho_join_yes
            "No":
                jump Camacho_join_no

    label camacho_join_yes:
        play sound "audio/SFX/choice_good.ogg"
        "¡Vale! Me agrada la idea"
        camacho "Vale jeje"
        jump work_camacho
    label Camacho_join_no:
        "No, Creo que estamos mejor los dos solos"
        camacho "El hugo ya tiene novia ¿eh? jeje"
        hide camacho happy
        kenia "..."
        "*tomas en cuenta la hazaña de camacho*"
        "*¿Te arriesgas?*"
        menu:
            "Si":
                jump risk1
            "No":
                jump risk2

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
        play sound "audio/SFX/choice_good1.ogg"
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
            "hehehe..."
        jump work
        label date:
            scene bg blackbg
            with fade
            "*Te preparas para la cita*"
            "*esperas a que todo salga genial*"
            play music "audio/date.ogg"
            scene bg dinnerrestaurant
            with fade
            "*Esperas*"
            show kenia dress smile
            kenia "Hola jeje"
            "H- Hola jeje"
            kenia "¿Como me veo?"
            menu:
                "Te vez hermosa":
                    jump youlookgreat_date
                "Te vez bien jeje":
                    jump youlooknice_date
                "Estas horrible xd":
                    jump youlookhorrible_date
    label youlookgreat_date:
        show kenia dress blush
        kenia "¿en verdad? gracias jeje"
        "si asi es jeje"

        jump date_continue
    label youlooknice_date:
        show kenia dress smile
        kenia "Gracias tu tambien te vez bien"
        "(deberia decir algo mas que eso)"
        "(si algo tenia hugo es que era muy callado y nadamas se la pasaba en el telefono)"
        jump date_continue
    label youlookhorrible_date:
        show kenia dress angry
        play sound "audio/SFX/choice_bad2.ogg"
        play music "audio/Music/B/mus_notperfect_chase.ogg"
        kenia ">:v"
        "(creo que tampoco deberia de ser TAN sincero)"
        "(en serio me pasé de sincero)"
        "(creo que debo pedirle una disculpa)"
        play music "audio/date.ogg"
        show kenia dress smile
        kenia "bueno supongo que nadie es perfecto :C"
        "*¿Le pides perdon?*"
        menu:
            "si":
                jump doyouspareme_date
            "no":
                jump dontspareher
        label doyouspareme_date:
            "¿Me perdonas? me he pasado de sincero"
            kenia "Si jeje yo tambien a veces me paso de sincera jeje"
            "(tenemos tanto en comun...)"
            jump date_continue

        jump game_end
        label dontspareher:
        play sound "audio/SFX/bad_decision.ogg"
        "..."
        scene bg hugoroom depressed
        play music "audio/Music/B/mus_act9.ogg"
        "(por que soy asi de idiota, no puedo creerlo)"
        scene bg blackbg
        "BAD ENDING: Hugo La ha regado con su posible primer pareja"
        "Y eso es TU CULPA"
        jump game_end
        label date_continue:
            kenia "jijijiji"
            "Que quieres hacer?"
            kenia "Vamos a ver una pelicula va?"
            "vale me agrada la idea"

        jump moviewatch

        label moviewatch:
            play music "audio/Music/B/mus_kindandfair.ogg"
            scene bg keniahouse
            show kenia Happy
            kenia "muy bien preparemos todo para ver una peli jeje"
            jump game_end
        label work:
        show kenia Happy
        kenia "Bueno a ponernos a trabajar"
        kenia "hagamoslo de animales salvajes"
        label work_camacho:
            camacho "Bueno lo hacemos de.."
            show kenia happy
            kenia "Animales salvajes"
            "Vale me agrada la idea"
            camacho "A mi tambien me gussta la idea jeje"
            show nick happy at left
            nick "Hola me puedo unir?"
            menu:
                "Si":
                    jump nick_join_yes
                "No":
                    jump nick_join_no
            label nick_join_yes:
                show nick super happy at left
                nick "gracias jeje"
                jump work_start
            label nick_join_no:
                show nick cry
                nick "oh...."
                jump not_nick
    label work_start:
        "jeje"
        nick "¿Puedo meter a Leo?"
        kenia "Vale jeje"
        play music "audio/Fight.ogg"
        hide nick
        show leo base at left
        Leo "Hola"
        jump game_end
    label not_nick:

    label game_end:

    return
