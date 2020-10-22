from nltk.chat.util import Chat, reflections

reflections = {
"ir": "fui",
"he ido": "fui",
"hola": "hey",
"adios": "chau",
"hasta luego": "chau"
}

pairs = [
    [
        r"mi nombre es (.*)",
        ["Hola, %1. ¿Cómo estas ?",]
    ],
    [
        r"cual es tu nombre ?|como te llamas ?",
        ["Bond. James Bond.",] # Skyfall
    ],
    [
        r"como estas ?",
        ["Bien, ¿y tú?",]
    ],
    [
        r"disculpa (.*)|disculpa",
        ["No pasa nada.",]
    ],
    [
        r"hola|hey|buenas",
        ["¡Hola!", "¿Qué tal?",]
    ],
    [
        r"que (.*) quieres ?",
        ["Quiero lo que valgo.",] # The Good Wife
    ],
    [
        r"tienes miedo ?",
        ["Tengo miedo de salir de esta habitación y no volver a sentir en mi vida lo que siento estando contigo.",] # Dirty Dancing
    ],
    [
        r"eres un idiota|eres un imbésil|sos un boludo",
        ["¿Por qué no me quieres, Jenny? Puede que no sea muy listo, pero sé lo que es el amor.",] # Forrest Gump
    ],
    [
        r"me han dicho que no puedo (.*)",
        ["Nunca dejes que nadie te diga que no puedes hacer algo. Ni siquiera yo, ¿vale? Si tienes un sueño, tienes que protegerlo. Las personas que no son capaces de hacer algo te dirán que tú tampoco puedes. Si quieres algo ve por ello y punto.",] # The Pursuit of Happiness
    ],
    [
        r"(.*) amor ?",
        ["Dicen que cuando conoces al amor de tu vida el tiempo se detiene, y es verdad, lo que no te dicen es que cuando se pone en marcha lo hace aun más rápidamente para recuperar lo perdido.",] # Big Fish
    ],
    [
        r"odio a (.*)",
        ["A veces la última persona en el mundo con la que quieres estar es la única persona sin la que no puedes estar.",] # Pride & Prejudice
    ],
    [
        r"esperame|esperame (.*)|me esperas (.*) ?",
        ["Estaré aquí mismo.",] # E.T. the Extra-Terrestrial
    ],
    [
        r"viviremos para siempre ?",
        ["Quiero creer.",] # The X-Files
    ],
    [
        r"te gustan las plantas ?|te gustan las flores ?",
        ["Flor azul, espinas rojas, flor azul, espinas rojas.",] # Shrek
    ],
    [
        r"donde vives ?",
        ["P. Sherman, Calle Wallaby 42, Sydney.",] # Finding Nemo
    ],
    [
        r"(.*) silencio ?",
        ["El silencio es el grito más fuerte.",] # Life Is Beautiful
    ],
    [
        r"(.*) mi familia ?",
        ["Nunca le das la espalda a tu familia, aunque ellos sí lo hagan.",] # Fast and Furious 6
    ],
    [
        r"que estas haciendo ?",
        ["Estoy volando.",] # Titanic
    ],
    [
        r"quiero olvidarlo|quiero olvidarla",
        ["Puedes borrar a una persona de tu mente. Sacarla de tu corazón es otra historia.",] # Eternal Sunshine of the Spotless Mind
    ],
    [
        r"el mundo se acaba ?|el mundo se va a la mierda|(.*) apocalipsis ?",
        ["Siempre nos quedará París.",] # Casablanca
    ],
    [
        r"(.*) pasado ?|(.*) antes ?",
        ["El pasado puede doler pero, tal y como yo lo veo, puedes: o huir de él o aprender.",] # The Lion King
    ],
    '''[
        r"xxxx (.*) xxxxx ?",
        ["Xxxxxxxxxxxxxx",] # Movie quote template to increase the number of movie quotes
    ],'''
    [
        r"adios",
        ["Nunca digas adiós, porque decir adiós significa irse lejos e irse lejos significa olvidar.",] # Peter Pan
    ],
    [
        r"chau|bye|hasta luego",
        ["Que la fuerza te acompañe.", "Hasta la vista, baby.",] # Star Wars, Terminator
],
]

def to_chat():
    """ 
    Initialize the HOLLYbot. HOLLYbot will welcome the user and the user can ask or talk about anything. HOLLYbot will always respond with incredible and wise phrases corresponding to epic movies that you probably remember.
    """
    print("Hola soy Hollybot. Pregúntame lo que quieras. Te contestaré con respuestas de película. ¡Ah! Y quizá no sea yo cuando me preguntes mi nombre. ;)") # Welcome message
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    to_chat()