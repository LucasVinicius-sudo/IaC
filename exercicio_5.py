import matplotlib.pyplot as plt
import pandas as pd 
file =  pd.read_csv("C:/Users/gestor/Downloads/a2_MANCHAS(1).csv")
x = list(file["Ano"])
y = list(file["manchas"])
plt.plot(x,y)
plt.tile("Demonstrando as manchas solares de ano em ano(30 primeiros)",fontsize = 15,color ="r",style="italic",family="monospace")
plt.title("Demonstrando as manchas solares de ano em ano(30 primeiros)",fontsize = 15,color ="r",style="italic",family="monospace")
plt.xlabel("Ano",size=12); plt.ylabel("Manchas",size=12)
plt.grid()
plt.tight_layout()
plt.savefig("30first.jpg")
plt.savefig("30first.png")
 
