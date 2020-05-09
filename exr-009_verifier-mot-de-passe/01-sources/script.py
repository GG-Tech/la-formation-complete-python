mdp = input("Entrez un mot de passe (min 8 caractères) : ")
mdp_trop_court = "votre mot de passe est trop court."
result = ""

if len(mdp) < 8:
    result = mdp_trop_court.capitalize()
    if len(mdp) == 0:
        result = mdp_trop_court.upper()
elif mdp.isdigit():
    result = "Votre mot de passe ne contient que des nombres."
else:
    result = "Inscription terminée."

print(result)