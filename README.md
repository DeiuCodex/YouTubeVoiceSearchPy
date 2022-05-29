# YouTubeVoiceSearchPy
Implementarea unui script ce căută un videoclip pe platforma youtube folosind o comandă vocală în care se precizează numele videoclipului.

@@@ Detecție comanda vocală @@@

1. Se va folosi un microfon pentru a capta comanda vocală.
2. Scriptul trebuie să identifice o anumită comandă vocală dintr-o listă configurată în prealabil.
   Lista conține perechi de valori de tipul: (comanda vocală, comanda de executat pe sistem)
3. Dacă comanda vocală a fost identificată, script-ul va căuta videoclipul respectiv pe youtube.


Se rulează script-ul iar asistentul vocal va solicita pașii ce trebuie urmați.
Erorile ce pot apărea în recunoașterea vocii, sunt tratate - Asistentul va cere să repetați fraza.
Se rostește ” search youtube for *** ”

*** = cele trei melodii introduse în lista predefinită (conform cerinței), anume:

1. rammstein du hast
2. lady gaga poker face
3. metallica the unforgiven


!!! Recomand o încăpere fără multe zgomote care pot perturba înregistrarea vocii. Recomand trecerea pe mut a microfonului după ce se rostește fraza.
!!! Timpul de acces este de 200 secunde. După 200 secunde, programul se finalizează.

