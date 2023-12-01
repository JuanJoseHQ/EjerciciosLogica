"""
¡Los trolls están atacando tu sección de comentarios!

Una forma habitual de afrontar esta situación es eliminar todas las vocales de los comentarios
de los trolls, neutralizando la amenaza.

Tu tarea es escribir una función que tome una cadena y devuelva una nueva cadena sin todas las
vocales.

Por ejemplo, la cadena "¡Este sitio web es para perdedores LOL!" se convertiría en "¡Ths wbst
s fr lsrs LL!".

Nota: para este kata yno se considera una vocal.
"""
def disemvowel(string_):
    y = ""
    voc = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U",]
    for x in string_:
        if x not in voc:
            y += x
    return y

def disemvowel(string):
    return string.translate(None, 'aAeEuUoOiI')