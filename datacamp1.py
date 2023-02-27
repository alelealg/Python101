lista_super = ["nopal", 1, "aguacates", 4, "tomates", 6, "cebolla", 4, "betabel", 2, "plátanos", 4, "manzanas", 4, "espinacas", 1, "calabazas", 2, "pimientos", 2]
print(lista_super)

lista_super1 = lista_super[:]
lista_super1 = lista_super1 + ["salmas", 1, "pasta colgate roja", 1]
print(lista_super)
print(lista_super1)

print(lista_super1.index("aguacates"))
print(lista_super.count(1))
lista_super1.append("bolillo")
lista_super1.append(2)
lista_super1.reverse()
print(lista_super1)

import numpy as np
prueba = (1, 2, 3, 4, 5)
np_prueba = np.array(prueba)
print(type(np_prueba))
print(prueba + prueba)
print (np_prueba + np_prueba)
print(4*prueba)
print(3*np_prueba)

import matplotlib.pyplot as plt
year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]
#add data
year = [1800, 1850, 1900] + year
pop = [1.0, 1.262, 1.650] + pop
plt.plot(year, pop, c = "green")
plt.xlabel("Year")
plt.ylabel("Population")
plt.title("World Population Projections")
plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8],
           ["0", "1B", "2B", "3B", "4B", "5B", "6B", "7B", "8B"])
plt.grid(True)
plt.show()
plt.scatter(year, pop)


values = [0, 0.6, 1.4, 1.6, 2.2, 2.5, 2.6, 3.2, 3.5, 3.9, 4.2, 6]
plt.hist(values, bins = 3)
plt.show()
#cleans plot so you can start fresh again
plt.clf()
# bins son 10 si no especificas
plt.hist(values)
plt.show()

paises_eu = {"españa":"madrid", "francia":"paris", "alemania":"berlin", "italia":"roma"}
#llamar a 1 valor con su key
print(paises_eu["francia"])
# agregar 1 valor
paises_eu["brasil"] = "rio de janeiro"
print(paises_eu)
# ups es brasilia
paises_eu["brasil"] = "brasilia"
print(paises_eu)
# ah pero es paises de europa. mejor eliminar brasil y agregar portugal
del(paises_eu["brasil"])
paises_eu["protugal"] = "lisboa"
print(paises_eu)

# + diccionarios: más de 1 valor por par
paises = {"españa": {'capital':'madrid', 'continente':'europa'},'francia':{'capital':'paris', 'continente':'europa'}, 'alemania':{'capital':'berlin', 'continente':'europa'}, 'brasil':{'capital':'brasilia', 'continente':'america'}, 'australia':{'capital':'sydney', 'continente':'oceania'}}
print(paises['alemania']['capital'])

# pandas!
import pandas as pd
dict = {
    'country':['Brasil', 'Russia', 'India', 'China', 'South Africa'],
    'capital':['Brasilia', 'Moscow', 'New Dehli', 'Beijing', 'Pretoria'],
    'area': [8.516, 17.10, 3.826, 9.597, 1.221],
    'population': [200.4, 143.5, 1252, 1357, 52.98]}
brics = pd.DataFrame(dict)
# agregar índice o labels a cada fila de paises (si no, 0, 1, 2...)
brics.index = ['BR', 'RU', 'IN', 'CH', 'SA']

# archivo debe estar en mismo folder que archivo python con instrucciones
brics2 = pd.read_csv('/Users/alelealg/PycharmProjects/corepy/brics.csv')
print(brics2)

#row labels (BR, RU, IN, etc) seen as a column instead of labels. Tell python that 1st row contains row indexes
brics2 = pd.read_csv('/Users/alelealg/PycharmProjects/corepy/brics.csv', index_col = 0)
print(brics2)

# seleccionar solo 1 columna (se imprime también "row labels". dobles [[]] para que siga siendo dataframe
print(brics[['country', 'population']])

# seleccionar parte del array. loc basado en labels, iloc position-based
print(brics.loc[['SA']])
# doble [] permite tener un DataFrame vs series (en DF vienen nombres de columnas, etc)
print(brics.loc[['RU', 'IN', 'SA'], ['country', 'area']])

# Column access brics[['country', 'capital']
# Row access: only through slicing brics[1:4]
# loc(label-based) row: brics.loc[['RU', 'IN']] (salen todas las columnas de esas filas),
    # column: brics.loc[:, ['country', 'capital']] salen todas las filas de columnas country capital
    # rows and columns, slicing, brics.loc[['RU', 'IN'], ['country', 'capital']]

#igual que loc, pero en vez de labels, nombres filas con iloc
    # brics.loc[['RU']] = brics.iloc[[1]]

# and or not para arrays (np) es logical_and(), logical_or(), logical_not()
prueba = (1, 2, 3, 4, 5)
np_prueba = np.array(prueba)
print(np.logical_and(np_prueba < 5, np_prueba > 2))

# seleccionar países con area > 8
# 1: seleccionar columna area: se necesita serie, NO data frame
brics["area"]
#2: seleccionar países con área > 8, tenemos booleans
print(brics["area"] > 8)
#3: pedir que imprima esos países. puedes darle nombre a expresión pasada, o pedir directo
print(brics[brics["area"] > 8])
print(brics[np.logical_and(brics["area"] >8, brics["area"] < 10)])

# for loop: para sacar el index de una lista, enumerate:
fam = [1.73, 1.68, 1.71, 1.89]
for index, height in enumerate(fam):
    #llamé con enumerate(fam), función es enumerate. index y height puedo cambiar nombres
    print("index " + str(index)+ ": " + str(height))

#se puede usar para strings también, acceder a cada letra.
for c in "family":
    print(c.capitalize())

# for dictionaries, llamas diccionario.items(). No sigue orden especial para iterar
for key, value in paises_eu.items():
    print("La capital de " + key + " es " + value)

#for para numpy arrays (2D, o sea, 2 arrays  combinados), para accesar a cada elemento por separado se usa np.nditer

#for para Pandas Dataframes: ___.iterrows():
for lab, row in brics.iterrows():
    print(lab)
    print(row)
#Por cada Label (RU, BR, etc), imprime su info (row) con el nombre de la info
#Para seleccionar solo cierta info (capital, por ejemplo), usas subsetting
for lab, row in brics.iterrows():
    print(lab + ": " + row["capital"])


def numberOfSteps (self, num: int) -> int:
    numberOfSteps(0, 14)
    count = 0
    while True:
        if num == 0:
            count = 0
        elif num % 2 == 0:
            num = num / 2
        else:
            num = num - 1
        count = count + 1

        count = 0
        while True:
            if num == 0:
                count = 0
            elif num % 2 == 0:
                num = num / 2
            else:
                num = num - 1
            count = count + 1