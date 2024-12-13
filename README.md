# strath

## FRANÇAIS

Cette bibliothèque aide à assurer qu'un chemin de fichier soit de type `str` ou
`pathlib.Path`.

En Python, il est possible de représenter des chemins de fichier au moyen de
chaînes de caractères (`str`) ou d'instances de `pathlib.Path`. Ces types
étant employés de façons fort différentes, un développeur peut avoir besoin de
vérifier le type des objets et d'effectuer des conversions.

La bibliothèque `strath` permet de faire ces deux tâches en un seul appel de
fonction.

### Contenu

#### `ensure_path_is_pathlib`

Si l'objet passé à cette fonction est une chaîne de caractères, la fonction le
convertit en une instance de `pathlib.Path` et la renvoie. Si l'objet est une
instance de `pathlib.Path`, la fonction renvoie l'objet.

#### `ensure_path_is_str`

Si l'objet passé à cette fonction est une instance de `pathlib.Path`, la
fonction le convertit en chaîne de caractères et la renvoie. Si l'objet est une
chaîne de caractères, la fonction renvoie l'objet.

#### Paramètes et exception

Les fonctions ci-dessus ont les mêmes paramètres.

`some_path` (`str` or `pathlib.Path`): le chemin d'un fichier ou d'un dossier.

`is_none_allowed` (`bool`): determine si `some_path` peut être `None`.

Si l'argument `some_path` est `None` et l'argument `is_none_allowed` est vrai
(`True`), les fonctions renvoient `None`. Par contre, si `is_none_allowed` est
faux (`False`), une exception `TypeError` est levée.

### Dépendances

Cette commande installe les dépendances nécessaires au développement.

```
pip install -r requirements-dev.txt
```

### Tests automatiques

Cette commande exécute les tests automatiques.

```
pytest tests
```

## ENGLISH

This library helps ensuring that a file path is of type `str` or
`pathlib.Path`.

In Python, it is possible to represent file paths with character strings
(`str`) or `pathlib.Path` instances. Since these types are used in very
different ways, a developer might need to verify the objects' type and to
perform conversions.

Library `strath` allows to do both tasks in one function call.

### Content

#### `ensure_path_is_pathlib`

If the object passed to this function is a string, the function converts it to
a `pathlib.Path` instance, which it returns. If the object is a `pathlib.Path`
instance, the function returns the object.

#### `ensure_path_is_str`

If the object passed to this function is a `pathlib.Path` instance, this
function converts it to a string, which it returns. If the object is a string,
this function returns the object.

#### Parameters and exception

The above functions have the same parameters.

`some_path` (`str` or `pathlib.Path`): the path to a file or directory.

`is_none_allowed` (`bool`): determines whether `some_path` can be `None`.

If argument `some_path` is `None` and argument `is_none_allowed` is `True`, the
functions return `None`. However, if `is_none_allowed` is `False`, a
`TypeError` is raised.

### Dependencies

This command installs the dependencies necessary for development.

```
pip install -r requirements-dev.txt
```

### Automated tests

This command executes the automated tests.

```
pytest tests
```
