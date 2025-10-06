#### Imports et définition des variables globales

# Mandatory for the recursive solution to work on large inputs
import sys
sys.setrecursionlimit(2000)


#### Fonctions secondaires


def artcode_i(s):
    if not s:  # chaîne vide
        return []

    C = [s[0]]  # liste des caractères
    O = [1]     # occurrences
    for k in range(1, len(s)):
        if s[k] == s[k-1]:
            O[-1] += 1
        else:
            C.append(s[k])
            O.append(1)
    return list(zip(C, O))



def artcode_r(s):
    if not s:
        return []

    first_char = s[0]
    count = 1
    # compter les caractères identiques au début
    while count < len(s) and s[count] == first_char:
        count += 1

    # créer le tuple et concaténer avec le résultat récursif
    return [(first_char, count)] + artcode_r(s[count:])

    

#### Fonction principale


def main():
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
