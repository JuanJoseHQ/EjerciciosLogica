"""
Simplemente busque el valor más cercano a cero en la lista. 
Observe que hay aspectos negativos en la lista.

La lista no siempre está vacía y contiene solo números enteros. 
Regrese Nonesi no es posible definir solo uno de dichos valores. Y, por supuesto, 
esperamos que 0 sea el valor más cercano a cero.

Ejemplos:

[2, 4, -1, -3]  => -1
[5, 2, -2]      => None
[5, 2, 2]       => 2
[13, 0, -6]     => 0
"""
def closest(lst):
    min = 999
    bol = True
    for x in lst:
        if(abs(min) - abs(x) > 0 or x == min):
            min = x
            
        elif (abs(min) == abs(x)):
            bol = False
            min_ = x
    return None if (bol == False and abs(min_) == abs(min)) else min

def closest(lst):
    m = min(lst, key=abs)
    return m if m == 0 or -m not in lst else None