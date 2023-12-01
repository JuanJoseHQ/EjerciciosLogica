"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word.
Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""
def pig_it(text):
    out = ""
    end = "ay"
    z = ""
    for word in text.split():
        if word.isalpha():
            for y in word:
                z = y[0] + end
                out += word[1:len(word)] + "" + z + " "
                break
        else:
            out += word + " "
    return out[:-1] if out.endswith(" ") else out

def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])