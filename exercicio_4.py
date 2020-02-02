 import pandas as pd

 import matplotlib.pyplot as plt
 file =  pd.read_csv("C:/Users/gestor/Downloads/a2_MANCHAS(1).csv")
 plt.boxplot(file["manchas"])
{'whiskers': [<matplotlib.lines.Line2D object at 0x0AFDD4F0>, <matplotlib.lines.Line2D object at 0x0AFDD890>], 'caps': [<matplotlib.lines.Line2D object at 0x0AFDDB10>, <matplotlib.lines.Line2D object at 0x0AFDDD70>], 'boxes': [<matplotlib.lines.Line2D object at 0x0AFDD4D0>], 'medians': [<matplotlib.lines.Line2D object at 0x0AFF5270>], 'fliers': [<matplotlib.lines.Line2D object at 0x0AFF54D0>], 'means': []}
 plt.savefig("boxplot")
 
