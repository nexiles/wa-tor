# -*- coding: utf-8 -*-

def simulationsschritt(t, welt):
    """
    simulationsschritt(t, welt) -> welt

    Simuliert die welt und gibt die neue welt
    als ergebnis.
    """
    return welt

def display(t, welt):
    """
    display(t, welt) -> None

    Stelle die aktuelle welt und zeit dar.
    """
    print "Zeit: ", t, "Welt: ", welt

def mainloop(t_start, dt, t_stopp):
    """
    mainloop

    The main loop of wa-tor.
    """
    # initialisiere die zeit
    t = t_start

    # initialisiere eine welt
    welt = None

    fertig = False
    # solange nicht fertig:
    while not fertig:
        # simuliere die welt
        welt = simulationsschritt(t, welt)

        # welt darstellen
        display(t, welt)

        # zeit erhöhen
        t = t + dt

        # Wenn die Zeit t_stopp erreicht ist, bitte aufhoeren
        if t >= t_stopp:
            fertig = True

    return t

print "Lauf 1"
mainloop(0, 1, 10)

print "Lauf 2"
mainloop(0, 0.1, 10)
