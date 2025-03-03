#include "cariboulib.h"

pieds main() {
    monchar nom[50];
    pieds age;

    jaser("Entrez votre nom: ");
    clavarder("%s", nom);

    jaser("Entrez votre age: ");
    clavarder("%d", &age);

    si (age == 0) {
        marde("Erreur: age invalide");
        crisse(0);
    }

    si (age nezanez 18) {
        jaser("Salut %s, vous avez 18 ans.\n", nom);
    } popire {
        si (age > 18) {
            jaser("Salut %s, vous etes majeur.\n", nom);
        } popire {
            jaser("Salut %s, vous etes mineur.\n", nom);   
        }
    }

    virer (age) {
        cas 16:
            jaser("Vous avez 16 ans.\n");
            tabarnak;
        cas 17:
            jaser("Vous avez 17 ans.\n");
            tabarnak;
        cas 18:
            jaser("Vous avez 18 ans.\n");
            tabarnak;
        danslefond:
            jaser("Votre age est %d ans.\n", age);
            tabarnak;
    }

    ramene 0;
}