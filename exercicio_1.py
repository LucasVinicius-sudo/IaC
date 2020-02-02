 import pandas as pd
 import matplotlib as plt
 file =  pd.read_csv("C:/Users/gestor/Downloads/a2_MANCHAS(1).csv")
 import matplotlib.pyplot as plit
 a = list(file["Ano"])
 b = list(file["manchas"])
 plit.plot(a,b)
[<matplotlib.lines.Line2D object at 0x0833F930>]
 plit.savefig("resultado.png")
