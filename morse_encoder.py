#!/usr/bin/env python3
morse_dict = {
                    "a" : ".-", "b" : "-...", "c" : "-.-.",
                    "d" : "-..", "e" : ".", "f" : "..-.",
                    "g" : "--.", "h" : "....", "i" : "..",
                    "j" : ".---", "k" : "-.-", "l" : ".-..",
                    "m" : "--", "n" : "-.", "o" : "---",
                    "p" : ".--.", "q" : "--.-", "r" : ".-.",
                    "s" : "...", "t" : "-", "u" : "..-",
                    "v" : "...-", "w" : ".--", "x" : "-..-",
                    "y" : "-.--", "z" : "--..", "1" : ".----",
                    "2" : "..---", "3" : "...--", "4" : "....-",
                    "5" : ".....", "6" : "-....", "7" : "--...",
                    "8" : "---..", "9" : "----.", "0" : "-----",
                    " " : "/"
                    }

def traductor_morse(val):
    separador = []
    morse = []

    for x in val:
        separador.append(x)
    for s in separador:
        if s == " ":
            morse.append("/")
        elif s in morse_dict:
            morse.append(morse_dict[s]+" ")


    palabra_morse = "".join(morse)
    
    return(palabra_morse)

