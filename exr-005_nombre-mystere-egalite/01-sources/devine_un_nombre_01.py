min_val = 0
max_val = 10
nombre_mystere = 7
tries = 0

def str_to_integer(str_v: str) -> str or int:
    try:
        int(str_v)
        return int(str_v)
    except ValueError:
        return str_v

def in_range(number:int, min_val: int, max_val: int):
    if (number < min_val or number > max_val):
        print(f"Le nombre {str(number)} est en dehors des limites !")
        return False
    return True

def get_user_number():
    while (True):
        number = str_to_integer(input("Entre un nombre entre 0 et 10 : "))
        if (type(number) is int) and in_range(number, min_val, max_val):
            return number
        elif (type(number) is not int):
            print(f"Entrée invalide : {str(number)} !")

def end_game(tries: int):
    print()
    print("Félicitation, vous avez trouvé le bon nombre !")
    if (tries == 1):
        print(f"En {tries} tentative !")
    else:
        print(f"En {tries} tentatives !")

print("Bienvenue !")
print("Le but du jeu est de trouver le nombre choisit entre 0 et 10")
print("Vous êtes pret ?")
print("C'est parti !")
print()

while (True):
    nombre_utilisateur = get_user_number()
    tries += 1
    if (nombre_utilisateur == nombre_mystere):
        end_game(tries)
        break

print()
print("Merci d'avoir joué !")