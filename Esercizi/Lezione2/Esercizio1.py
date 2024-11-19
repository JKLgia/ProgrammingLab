"""
Questo programma permette di stampare a video 
l'orario, partendo dai minuti.

Calcolo l'ora dividendo (//) i minuti trascorsi per  60.
Calcolo i minuti con il modulo (%) della divisione per 60.
"""

startMinute = 685

hour = startMinute//60
minute = startMinute%60

print("L'ora da stampare e' " + '{:d}:{:02d}'.format(hour, minute))
