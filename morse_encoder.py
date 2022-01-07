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
    for i in val:
        if i in morse_dict:
            pass
        else:
            return(False)

    separador = [x for x in val]
    morse = [morse_dict[s]+" " for s in separador]
    palabra_morse = "".join(morse)
    
    return(palabra_morse)
