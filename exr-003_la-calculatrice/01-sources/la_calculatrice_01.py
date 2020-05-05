# Demander à l'utilisateur d'entrer un premier nombre
# Demander à l'utilisateur d'entrer un deuxième nombre
# Afficher à l'écran le résultat de l'addition (exemple : 'Le résultat de l'addition de 5 + 10 est égal à 15')

def str_to_float(str_v: str) -> str or float:
    try:
        float(str_v)
        return float(str_v)
    except ValueError:
        return str_v

def str_to_integer(str_v: str) -> str or int:
    try:
        int(str_v)
        return int(str_v)
    except ValueError:
        return str_v

def str_to_number(str_v: str) -> float or int or str:
    result = str_to_integer(str_v)
    if result == str_v:
        result = str_to_float(str_v)
    return result

a = str_to_number(input("Entre un nombre : "))
b = str_to_number(input("Entre un autre nombre : "))

error = False

if type(a) == str:
    print(f"La valeur '{a}' donné est incorrecte !")
    error = True
if type(b) == str:
    print(f"La valeur '{b}' donné est incorrecte !")
    error = True
if not error:
    print(f"Le résultat de {a} + {b} est : {a + b}")