import re
import sys

def lire_defines(nom_fichier):
    defines = {}
    with open(nom_fichier, 'r') as f:
        lines = f.readlines()
        for line in lines:
            match = re.match(r'#define\s+(\w+)\s+(\w+)', line.strip())
            if match:
                c_mot = match.group(1)
                caribou_mot = match.group(2)
                defines[c_mot] = caribou_mot
    return defines


def convertir_en_caribou(code_c, defines, define_file):
    res = f'#include "{define_file}"\n' + code_c
    for mot_caribou, mot_c in defines.items():
        res = re.sub(r'\b' + re.escape(mot_c) + r'\b', mot_caribou, res)
    return res


def lire_fichier(nom_fichier):
    with open(nom_fichier, 'r') as f:
        return f.read()

def ecrire_fichier(nom_fichier, code):
    with open(nom_fichier, 'w') as f:
        f.write(code)

def main():
    fichier_defines = 'cariboulib.h'
    if len(sys.argv) != 2:
        print("Usage: python converter.py <source_file>")
        sys.exit(1)

    fichier_source = sys.argv[1]

    defines = lire_defines(fichier_defines)
    code_c = lire_fichier(fichier_source)
    code_caribou = convertir_en_caribou(code_c, defines, fichier_defines)

    print(code_caribou)

if __name__ == '__main__':
    main()
