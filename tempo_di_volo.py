#tempo_di_volo.py

#prima stampa
print "Tempo di Volo"
print "Determina la duata massima di volo conoscendo"
print "la quantita' di carburante ed il consumo orario.\n"

#variabili
ca = input("Carburante (in galloni): ")

co = input("Consumo Orario (in galloni/h): ")

#verifica variabili
if ca < 0:
    print "Il carburante deve essere maggiore o uguale a  0"
elif co <= 0:
    print "Il consumo orario deve essere maggiore di 0"
else:
    #tempo
    t = float(ca) / float(co)
    h = int(t)
    t = t - h
    t = t * 60
    m = int(t)
    t = t - m
    t = t * 60
    s = int(t)
    #ultima stampa
    print "Durata volo: ", h, "h", m, "min", s, "sec"
