
 import matplotlib.pyplot as plt
 import pandas as pd
 file =  pd.read_csv("C:/Users/gestor/Downloads/a2_MANCHAS(1).csv")
 a = list(file["Ano"])[:10]
 b = list(file["manchas"])[:10]
 plt.plot(a,b)
[<matplotlib.lines.Line2D object at 0x0824D770>]
 plt.savefig("exercicio2.png")
 
