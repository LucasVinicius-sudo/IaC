 import matplotlib.pyplot as plt
 import pandas as pd
 file =  pd.read_csv("C:/Users/gestor/Downloads/a2_MANCHAS(1).csv")
 x = list(file["Ano"])[-10:]
 y = list(file["manchas"])[-10:]
 x_2 = list(file["Ano"])[0:10]
 y_2 = list(file["manchas"])[0:10]

 plt.subplot(2,1,1)


 plt.title("Qtd de manchas (10 ultimos)",fontsize=15,color="green",style="oblique")

 plt.plot(x,y,color="black")

 plt.xlabel("Ano",color="blue",style="italic")

 plt.ylabel("Manchas",color="green",style="italic")

 plt.subplot(2,1,2)

 plt.title("Qtd de manchas solares(10 primeiros anos)",fontsize=15,color="green",style="oblique")

 plt.plot(x_2,y_2,color = "green")

 plt.xlabel("Ano",color="blue",style="italic")

 plt.ylabel("Manchas",color="blue",style="italic")
 plt.tight_layout()
 plt.savefig("dezprimeiros.png")
