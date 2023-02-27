from typing import Any, Union

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas import Series, DataFrame
from pandas.io.parsers import TextFileReader

gatitos: Union[Union[TextFileReader, Series, DataFrame, None], Any] = pd.read_csv('/Users/alelealg/PycharmProjects/corepy/Gatitos/UNOTRES.csv')
print(gatitos)
gatitospeso = gatitos[["UNO PESO"]]
gatitosfecha = gatitos["FECHA"]
gatitosporc = gatitos[["UNO PORC"]]
print(gatitosporc)
print(gatitospeso)
print(gatitosfecha)
plt.scatter(x = gatitosfecha, y = gatitospeso, s = np.array(gatitosporc))
plt.xlabel("Día")
plt.ylabel("Peso (g)")
plt.title("Crecimiento gatitos")
plt.yticks([80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200], ['80g', '90g', '100g', '110g', '120g', '130g', '140g', '150g', '160g', '170g', '180g', '190g', '200g'])
plt.show()