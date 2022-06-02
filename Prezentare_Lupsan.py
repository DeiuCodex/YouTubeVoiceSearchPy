"""
@author DeiuCodex & Adrian & Andrei
Contributed By @bansalshubhamcse21, @CLAUDIO SABATO
ETcTI Anul 2, Sg 3.1, Seria B, 2022-2024
Cautare automata pe YouToube - dintr-o lista deja existenta
Profesor coordonator: Bogdan Dragulescu, Razvan Vilceanu
Universitatea Politehnica Timisoara
Echipa: 31-E1
Studenti: Lupşan Adrian-Florin, Matală Andrei, Matieş Andrei-Mihai
Tema proiect: D4-T2 | Detecție comanda vocală.
Implementarea unui script ce căută un videoclip pe platforma youtube folosind o comandă vocală în
care se precizează numele videoclipului.
"""

import urllib.request                                                               # definește funcții și clase care ajută la deschiderea URL-urilor
import pyttsx3                                                                      # este o bibliotecă de conversie text în vorbire în Python
import re                                                                           # verificare dacă un anumit șir se potrivește cu o anumită expresie regulată
import selenium                                                                     # este folosit pentru a automatiza interacțiunea cu browserul web din Python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import speech_recognition as sr                                                  # folosit pentru recnoașterii vorbirii cu API-ul Google Speech Recognition
import time

try:
    def voice(message1):
        """
        Functie pentru Voice Assistant
        """
        en = pyttsx3.init()
        en.say(message1)
        en.runAndWait()


    voice("Please say a music that you want to search")


    def automateYoutube(comanda):
        """
        Functia ce realizeaza cautarea automatizata pe YouTube
        Procesul de inregistrare audio este inclus in functie alaturi de tratarile de exceptii
        """
        boo = False

        while not boo:
            speak = sr.Recognizer()                                 # procesul de inregistrare audio

            try:
                with sr.Microphone() as speaky:
                    speak.adjust_for_ambient_noise(speaky, duration=0.2)
                    print("listening...")
                    searchquery = speak.listen(speaky)                            # inregistrarea vocii
                    MyText = speak.recognize_google(
                        searchquery)                                  # utilizarea Google Speech Recognition pentru prelucrare audio
                    MyText = MyText.lower()

            except sr.RequestError as e:
                print("Nu am gasit rezultate; {0}".format(e))

            except sr.UnknownValueError:
                print("Am intampinat o eroare!")

            print("Ati rostit: ", MyText)

            var1 = "search youtube for rammstein du hast"
            var2 = "search youtube for lady gaga poker face"
            var3 = "search youtube for metallica the unforgiven"

            if not (MyText == var1 or MyText == var2 or MyText == var3):
                voice("Try Again")
                time.sleep(2)
                boo = False

            else:
                boo = True
                print("OK")
                search_keyword = MyText                                      # stocarea melodiei rostite intr-o variabila
                search_keyword_clear = search_keyword.replace(' ','+')            # in loc de spatiu dintre cuvinte, se adauga "+" specific sintaxei
                html = urllib.request.urlopen(
                    "https://www.youtube.com/results?search_query=" + search_keyword_clear)    # generarea link-ului
                video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())

                print("Link-ul generat: https://www.youtube.com/watch?v=" + video_ids[0])

                print("Se asteapta deschidere Youtube...")
                voice("I found what you want. This might take a while, please wait!")

                time.sleep(10)
                voice("Now I'm ready! Enjoy!")
                print("Enjoy!")
                url = 'https://www.youtube.com/watch?v=' + video_ids[0]

                try:
                    service_obj = Service("chromedriver.exe")
                    driver = webdriver.Chrome(service=service_obj)
                    driver.get(url)                                                             # accesarea link-ului generat
                except (selenium.common.exceptions.WebDriverException) as e:
                    print("Nu gasesc chromedrive! Te rog verifica integritatea proiectului!")
                    time.sleep(2)
                    print("Programul se inchide dupa 10 secunde!")
                    time.sleep(10)
                    exit()

                time.sleep(200)                                                            # timp de acces in browser -> 200s

                                                         # @@@ Main Function @@@

    if __name__ == '__main__':
        comenzi = {
            'search youtube': automateYoutube}                                           # dictionar configurat in prealabil - ( comanda vocala: comanda exec sistem)
        txt = 'search youtube for rammstein' or 'search youtube for lady gaga' or 'search youtube for metallica'
        txt_curat = txt.replace('', '+')
        txt_curat.split('for')
        comanda = ['search youtube', 'rammstein du hast', 'lady gaga poker face',
                   'metallica the unforgiven']                                          # lista cu melodii
        executa_comanda = comenzi[comanda[0]]
        executa_comanda(comanda[1])

except(KeyboardInterrupt, MemoryError, ResourceWarning, ModuleNotFoundError, ConnectionError) as e:
        print("Script-ul a fost inchis de catre utilizator sau din alt motiv.")
