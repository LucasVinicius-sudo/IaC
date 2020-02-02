import pandas as pd
import matplotlib.pyplot as plt
file =  pd.read_csv("C:/Users/gestor/Downloads/a2_MANCHAS(1).csv")
x_2 = (file["Ano"])[0:10]
y_2 = (file["manchas"])[:10]
plt.title("Qnt de manchas solares(10 anos)",fontsize=15,color="green",style="oblique")
plt.plot(x_2,y_2,color = "green")
plt.xlabel("Ano",color="blue",style="italic")
plt.ylabel("Manchas",color="black",style="italic")
plt.legend(["Manchas"])
plt.savefig("dez_primeiros_anos.png")
