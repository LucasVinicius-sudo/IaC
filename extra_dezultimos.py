 import pandas as pd
 import matplotlib.pyplot as plt
 file =  pd.read_csv("C:/Users/gestor/Downloads/a2_MANCHAS(1).csv")
 x = list(file["Ano"])[-10:]
 y = list(file["manchas"])[-10:]
 plt.title("Qtd de manchas (10 ultimos anos)",fontsize=15,color="green",style="oblique")
 plt.plot(x,y,color="green")
 plt.xlabel("Ano",style="italic",fontsize=10)
 plt.ylabel("Qtd Manchas",style ="italic",fontsize=10)
 plt.legend(["Manchas"])
 plt.savefig("dezultimos.png")
