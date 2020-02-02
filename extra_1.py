import pandas as pd
import matplotlib.pyplot as plt
file =  pd.read_csv("C:/Users/gestor/Downloads/a2_MANCHAS(1).csv")
file.plot(x="Ano", y="manchas" ,label="Manchas", color="pink")
plt.title("Aparecimento de manchas de ano em ano",fontsize=12,color="black",style="italic",family="monospace")
plt.xticks(rotation="vertical")
plt.xlabel("Ano",fontsize=13,style="oblique",color="blue")
plt.ylabel("Quantidade de Manchas",fontsize=13,style="oblique",color="red")
plt.grid()
plt.tight_layout()
plt.savefig("extra_1.png")
