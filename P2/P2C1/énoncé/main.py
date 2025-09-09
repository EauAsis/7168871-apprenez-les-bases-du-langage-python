nombre1 = input("entre un nombre")
nombre2 = input("entre un deuxieme nombre")
resultat = 0
if not nombre1.isnumeric and not nombre2.isnumeric:
    print("les nombres sont en chaines de caracteres")
    raise SystemExit("fin du programme")
nombre2 = int(nombre2)
nombre1 = int(nombre1)

operation = str(input("choisissez l'operation + - / *"))

match operation:
    case "+ ":
        resultat = nombre1 + nombre2
    case "- ":
        resultat = nombre1 - nombre2
    case "/ ":
        if nombre2 == 0 :
            raise SystemExit("division par 0 impossible")
        else :
            resultat = nombre1 / nombre2
    case "* ":
        resultat = nombre1 * nombre2
print(f"le resultat est: {round(resultat)}")
