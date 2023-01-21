import pyttsx3
import speech_recognition as sr
import pywhatkit
import pyjokes
import datetime
import wikipedia
import webbrowser
import numpy
import pyaudio




# Escucha de microfono y reconocimiento de voz - Transcripción de voz a texto

def transcribir_voz_texto():

    # Almacenar la voz en una variable
    r = sr.Recognizer()


    # configurar el microfono
    with sr.Microphone() as source:


        # tiempo de espera para que el usuario hable
        r.pause_threshold = 0.8


        # informar de inicio de escucha
        print("Escuchando...")

        # guardar la voz
        audio = r.listen(source)

        try:
            # buscar en google
            pedido = r.recognize_google(audio, language="es-ES")
            # Prueba de que pudo ingresar el texto
            print("Dijiste" + pedido)
            # Devolver el texto
            return pedido

        # en caso de que no se pueda reconocer el texto
        except sr.UnknownValueError:

            # informar de error
            print("No te he entendido")
            # devolver un texto vacio
            return ""

        # en caso de que no se pueda reconocer el texto
        except sr.RequestError:

                # informar de error
                print("No te he entendido")
                # devolver un texto vacio
                return ""


        # error inexperado
        except:

                # informar de error
                print("No te he entendido")
                # devolver un texto vacio
                return ""


# Funcion para que el asistente hable

def hablar(texto):

        # Inicializar el motor de voz
        engine = pyttsx3.init()

        # configurar el motor de voz
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 0.9)

        # hacer que el asistente hable
        engine.say(texto)

        # guardar el audio
        engine.runAndWait()


# Saludo inicial



hablar("Welcome Mister Infantes, I am Jarvis your personal assistant, how can I help you today sir?")



# Funcion para pedir cosas

def pedir_cosas():

    comenzar = True

    # loop central
    while True:

        # activar el micro y guardar el pedido en un string
        pedido = transcribir_voz_texto().lower()


        if "abrir youtube" in pedido:
            habalr("Abriendo youtube")
            webbrowser.open("https://www.youtube.com/")
            continue
        elif "abrir google" in pedido:
            hablar("Abriendo google")
            webbrowser.open("https://www.google.com/")
            continue
        elif "abrir gmail" in pedido:
            hablar("Abriendo gmail")
            webbrowser.open("https://mail.google.com/")
            continue
        elif "abrir facebook" in pedido:
            hablar("Abriendo facebook")
            webbrowser.open("https://www.facebook.com/")
            continue


pedir_cosas()







def pedir_hora():

    # obtener la hora actual
    hora = datetime.datetime.now().strftime('%H:%M')
    # devolver la hora
    return hora

def pedir_fecha():

        # obtener la fecha actual
        fecha = datetime.datetime.now().strftime('%d/%m/%Y')

        # devolver la fecha
        return fecha


def pedir_dia():

    calendario = {0: "Lunes",
                  1: "Martes",
                  2: "Miercoles",
                  3: "Jueves",
                  4: "Viernes",
                  5: "Sabado",
                  6: "Domingo"}

    # obtener la fecha actual
    hablar("Hoy es " + calendario[datetime.datetime.today().weekday()])


    # Informar de la hora actual

    hablar("Son las " + pedir_hora())

    # obtener el dia actual
    dia = datetime.datetime.now().strftime('%A')

    # devolver el dia
    return dia

pedir_dia()


