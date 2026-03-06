from data import Data

data1 = Data(1, 1, 2023)
print(data1)

# Deve imprimir:
# 01/01/2023

data4 = Data(1,2,2023)
data4.setData(2, 2, 2023)
print(data4)

# Deve imprimir:
# 02/02/2023
