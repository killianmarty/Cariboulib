# Caribou Lib

Librairie C simple pour coder en Québécois.

![Caribou Icon](icon.webp){ width=50% }

## Utilisation

```C
#include "cariboulib.h"
```

## Programmer en Caribou

### Convertisseur automatique

Un convertisseur de C vers Caribou est disponible via la commande suivante :

```bash
python3 converter.py source_file.c > output_file.c
```

### Lexique

Si vous préférez programmer directement en Caribou, voici une comparaison entre le lexique du Caribou et celui du C.

**NOTE: le lexique C est compatible avec le Caribou**

#### Mots clés

| **C Standard**  | **Caribou**  |
|-----------------|-----------------|
| `return`        | `ramene`        |
| `if`            | `si`            |
| `else`          | `popire`        |
| `while`         | `tantot`        |
| `for`           | `pour`          |
| `switch`        | `virer`         |
| `case`          | `cas`           |
| `break`         | `tabarnak`      |
| `continue`      | `poursuis`      |
| `default`       | `danslefond`    |
| `typedef`       | `definitletype` |
| `do`            | `faire`         |
| `volatile`      | `volant`        |
| `static`        | `fige`          |
| `extern`        | `externe`       |
| `const`         | `constant`      |
| `short`         | `pobenlong`       |
| `long`          | `benlong`       |
| `unsigned`      | `posigne`       |
| `signed`        | `signe`         |
| `struct`        | `bidule`        |
| `enum`          | `enumere`       |

#### Types

| **C Standard**  | **Caribou**  |
|-----------------|-----------------|
| `void`          | `fuckall`       |
| `char`          | `monchar`       |
| `int`           | `pieds`         |
| `float`         | `flotte`        |
| `double`        | `bigflotte`     |

#### Valeurs

| **C Standard**  | **Caribou**  |
|-----------------|-----------------|
| `NULL`          | `poche`         |
| `true`          | `correc`        |
| `false`         | `pantoute`      |

#### Opérateurs

| **C Standard**  | **Caribou**  |
|-----------------|-----------------|
| `&&`            | `et`            |
| `\|\|`            | `ou`            |
| `+`             | `pis`           |
| `==`            | `nezanez`       |

#### Fonctions

| **C Standard**  | **Caribou**  |
|-----------------|-----------------|
| `printf`        | `jaser`         |
| `scanf`         | `clavarder`     |
| `sleep`         | `niaiser`       |
| `free`          | `vidange`       |
| `malloc`        | `pogner`        |
| `realloc`       | `repogner`       |
| `sizeof`        | `grandeur`      |
| `typeof`        | `type`          |
| `exit`          | `crisse`        |
| `perror`        | `marde`         |