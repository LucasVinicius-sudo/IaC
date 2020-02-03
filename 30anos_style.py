 import pandas as pd
 import matplotlib.pyplot as plt
 file =  pd.read_csv("C:/Users/gestor/Downloads/a2_MANCHAS(1).csv")
 file[:30].plot("Ano","manchas", label="Manchas", grid=True)
 plt.title("Aparecimento de manchas solares ano a ano (30 Primeiros Anos)", fontsize=12, color="blue", style="italic", family="monospace")
 plt.xlabel("Ano", fontsize=13); plt.ylabel("Quntidade de manchas", fontsize=14)
 plt.xticks(rotation="vertical")
 plt.tight_layout()
 plt.savefig("TrintaPrimeiros_Anos_Styles.png")
