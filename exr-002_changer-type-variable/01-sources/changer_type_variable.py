# Demander à l'utilisateur d'entrer un nombre
# Afficher le résultat de l'addition de ce nombre avec le nombre a.
# Par exemple : "Le résultat de l'opération est 15" (dans le cas où l'utilisateur entre le nombre 5)

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

a = 10
b = str_to_number(input("Entre un nombre : "))

if type(b) == str:
    print(f"La valeur '{b}' donné est incorrecte !")
else:
    print(f"Le résultat de {a} + {b} est : {a + b}")