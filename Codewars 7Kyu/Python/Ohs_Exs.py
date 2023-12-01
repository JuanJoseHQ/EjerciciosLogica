"""
Check to see if a string has the same amount of 'x's and 'o's. The method must return
a boolean and be case insensitive. The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
"""
def xo(s):
    cant_o, cant_x = 0, 0
    
    for x in s.lower():
        if x == "o":
            cant_o += 1
        elif x == "x":
            cant_x += 1
    
    return True if cant_o == cant_x else False

def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')