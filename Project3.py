"""
@author Andrei & Adrian

ETcTI Anul 2, Sg 3.1, Seria B, 2022-2024
Cautare automata pe YouToube - dintr-o lista deja existenta

Profesor coordonator: Bogdan Dragulescu, Razvan Vilceanu
Universitatea Politehnica Timisoara
"""

import urllib.request
import re
from selenium import webdriver
import speech_recognition as sr
import time

path = "chromedriver.exe"                                        # Locatia pentru browser

speak = sr.Recognizer()                                          # Procesul de inregistrare audio

try:
    with sr.Microphone() as speaky:

        speak.adjust_for_ambient_noise(speaky, duration=0.2)
        print("listening...")

        # Asculta persoana care vorbeste
        searchquery = speak.listen(speaky)

        # Se foloseste Google pentru recunoastere audio
        MyText = speak.recognize_google(searchquery)
        MyText = MyText.lower()

except sr.RequestError as e:
    print("Nu am gasit rezultate; {0}".format(e))

except sr.UnknownValueError:
    print("Am intampinat o eroare!")

print("Ati rostit: ", MyText)

search_keyword = MyText                                         # Stocarea intr-o variabila a cuvantului rostit
html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword) #generarea link-ului
video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())

print("Link-ul generat: https://www.youtube.com/watch?v=" + video_ids[0])

print("Se asteapta deschidere Youtube...")
time.sleep(10)
url = 'https://www.youtube.com/watch?v=' + video_ids[0]

driver = webdriver.Chrome(path)                                 # Deschiderea browser-ului
driver.get(url)                                                 # Accesarea link-ului generat

time.sleep(200)                                                 # Timp de acces in browser -> 200s

# print("Ati rostit: ", MyText)
# print("Link-ul generat: https://www.youtube.com/watch?v=" + video_ids[0])



                                                # @@@ Notebook @@@ #
"""
1 - microfon -> returneaza text
gen: 'search youtube metallica'

2. comanda - search youtube => 
comanda - search youtube
cautare - metallica

3. declansarea comenzii
automateYoutube(metallica)



Organizare cod

functie_speach_to_text
functie_comanda (automateYoutube)



if __name__ == '__main__':
    txt_comanda = functie_speach_to_text # 1        
    comenzi = {'search youtube': automateYoutube, 'close': closeBrowser}
    comenzi.keys()

"""