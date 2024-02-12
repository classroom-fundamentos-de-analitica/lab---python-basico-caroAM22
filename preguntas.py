"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    suma = 0
    with open("data.csv", "r") as file:
        for line in file:
            values = line.strip().split()
            suma += int(values[1])
    return suma


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    word = {}
    with open("data.csv", "r") as file:
        for line in file:
            values = line.strip().split()
            if values[0] in word:
                word[values[0]] += 1
            else:
                word[values[0]] = 1
        word = sorted(word.items())
    return word


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    word = {}
    with open("data.csv", "r") as file:
        for line in file:
            values = line.strip().split()
            if values[0] in word:
                word[values[0]] += int(values[1])
            else:
                word[values[0]] = int(values[1])
        word = sorted(word.items())
    return word


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    mes = {}
    with open("data.csv", "r") as file:
        for line in file:
            values = line.strip().split()
            m = values[2].split("-")[1]
            if m in mes:
                mes[m] += 1
            else:
                mes[m] = 1
        mes = sorted(mes.items())
    return mes


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    max_min = {}
    with open("data.csv", "r") as file:
        for line in file:
            values = line.strip().split()
            if values[0] in max_min:
                if int(values[1]) > max_min[values[0]][0]:
                    max_min[values[0]][0] = int(values[1])
                elif int(values[1]) < max_min[values[0]][1]:
                    max_min[values[0]][1] = int(values[1])
            else:
                max_min[values[0]] = [int(values[1]), int(values[1])]
    max_min_sorted = sorted(max_min.items())
    mm = []
    for item in max_min_sorted:
        mm.append((item[0], item[1][0], item[1][1]))
    return mm


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres word corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    max_min = {}
    with open("data.csv", "r") as file:
        for line in file:
            values = line.strip().split()[4].split(",")
            for value in values:
                v = value.split(":")
                if v[0] in max_min:
                    if int(v[1]) > max_min[v[0]][1]:
                        max_min[v[0]][1] = int(v[1])
                    elif int(v[1]) < max_min[v[0]][0]:
                        max_min[v[0]][0] = int(v[1])
                else:
                    max_min[v[0]] = [int(v[1]), int(v[1])]

    max_min_sorted = sorted(max_min.items())
    mm = []
    for item in max_min_sorted:
        mm.append((item[0], item[1][0], item[1][1]))
    return mm


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las word asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    numbers = {}
    with open("data.csv", "r") as file:
        for line in file:
            values = line.strip().split()
            values[1] = int(values[1])
            if values[1] in numbers:
                numbers[values[1]].append(values[0])
            else:
                numbers[values[1]] = [values[0]]
    numbers = sorted(numbers.items())
    return numbers


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las word
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    numbers = {}
    with open("data.csv", "r") as file:
        for line in file:
            values = line.strip().split()
            values[1] = int(values[1])
            if values[1] in numbers:
                numbers[values[1]].add(values[0])
            else:
                numbers[values[1]] = {values[0]}
    numbers = sorted(numbers.items())
    for i in range(len(numbers)):
        numbers[i] = (numbers[i][0], sorted(numbers[i][1]))
    return numbers


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    dic = {}
    with open("data.csv", "r") as file:
        for line in file:
            values = line.strip().split()[4].split(",")
            for value in values:
                v = value.split(":")
                if v[0] in dic:
                    dic[v[0]] += 1
                else:
                    dic[v[0]] = 1
    dic = dict(sorted(dic.items()))
    return dic


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    total = []
    with open("data.csv", "r") as file:
        for line in file:
            values = line.strip().split()
            first = len(values[3].split(","))
            second = len(values[4].split(","))
            total.append((values[0], first, second))
    return total


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    dic = {}
    with open("data.csv", "r") as file:
        for line in file:
            values = line.strip().split()
            second_column = int(values[1])
            values = values[3].split(",")
            for value in values:
                if value in dic:
                    dic[value] += second_column
                else:
                    dic[value] = second_column
    dic = dict(sorted(dic.items()))
    return dic


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    words = {}
    with open("data.csv", "r") as file:
        for line in file:
            values = line.strip().split()
            if values[0] in words:
                total = sum([int(x.split(":")[1]) for x in values[4].split(",")])
                words[values[0]] += total
            else:
                words[values[0]] = sum(
                    [int(x.split(":")[1]) for x in values[4].split(",")]
                )
    words = dict(sorted(words.items()))
    return words
