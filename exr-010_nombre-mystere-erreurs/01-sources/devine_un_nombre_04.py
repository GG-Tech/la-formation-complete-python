import random

def str_to_integer(str_v: str) -> str or int:
    try:
        int(str_v)
        return int(str_v)
    except ValueError:
        return str_v

nombre_mystere = random.randint(0, 10)
nombre = input("Quel est le nombre mystère ? ")
nombre = str_to_integer(nombre)

if nombre > nombre_mystere:
    print(f"Le nombre mystère est plus petit que {str(nombre)}")
elif nombre < nombre_mystere:
    print(f"Le nombre mystère est plus grand que {str(nombre)}")
else:
    print("Bravo, vous avez trouvé le nombre mystère !")
