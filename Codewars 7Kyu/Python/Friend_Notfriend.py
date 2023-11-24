"""
Cree un programa que filtre una lista de cadenas y devuelva una lista que contenga 
solo el nombre de sus amigos.

Si un nombre tiene exactamente 4 letras, ¡puedes estar seguro de que tiene que ser un 
amigo tuyo! De lo contrario, puedes estar seguro de que no...

Ejemplo: Entrada = ["Ryan", "Kieran", "Jason", "Tú"], Salida = ["Ryan", "Tú"]

es decir

friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]
Nota: mantenga el orden original de los nombres en la salida.
"""
def friend(x):
    shouldBe = []
    for y in x:
        if(len(str(y)) == 4):
            shouldBe.append(y)
    return shouldBe

def friend(x):
    return [f for f in x if len(f) == 4]