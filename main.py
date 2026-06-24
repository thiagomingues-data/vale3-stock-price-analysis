# VALE3 Stock Price Analysis
# Period: November 2024 to February 2025

import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Read dataset
# -----------------------------
vale3 = pd.read_csv("Vale3.csv")

pd.set_option("display.max_columns", None)

# -----------------------------
# Data preparation
# -----------------------------
vale3resumo = pd.DataFrame(vale3[["DATA", "FECHAMENTO"]]).copy()
vale3resumo.columns = ["Data", "Fechamento"]

vale3resumo["Fechamento"] = (
    vale3resumo["Fechamento"]
    .str.replace(",", ".")
    .astype(float)
)

vale3resumo.to_csv("Vale3_resumo.csv", index=False)

# -----------------------------
# Average closing price
# -----------------------------
preco_med = vale3resumo["Fechamento"].mean()

print(f"Preço médio das ações: R$ {preco_med:.2f}")
print("►◄" * 19)

# -----------------------------
# Minimum and maximum prices
# -----------------------------
preco_min = vale3resumo["Fechamento"].min()
data_min = vale3resumo.loc[
    vale3resumo["Fechamento"].idxmin(),
    "Data"
]

print(f"Preço mínimo: R$ {preco_min:.2f} em {data_min}")

print("►◄" * 28)

preco_max = vale3resumo["Fechamento"].max()
data_max = vale3resumo.loc[
    vale3resumo["Fechamento"].idxmax(),
    "Data"
]

print(f"Preço máximo: R$ {preco_max:.2f} em {data_max}")

print("►◄" * 28)

# -----------------------------
# Investment simulation
# -----------------------------
num_acoes = 2000

data_compra = vale3resumo.loc[69, "Data"]
preco_compra = vale3resumo.loc[69, "Fechamento"]

data_venda = vale3resumo.loc[9, "Data"]
preco_venda = vale3resumo.loc[9, "Fechamento"]

valor_investido = num_acoes * preco_compra
valor_venda = num_acoes * preco_venda

retorno_final = valor_venda - valor_investido

print(f"Valor investido: R$ {valor_investido:.2f}")
print(f"Valor de venda: R$ {valor_venda:.2f}")

resultado = "lucro" if retorno_final > 0 else "prejuízo"

print(f"O investidor obteve {resultado} de R$ {abs(retorno_final):.2f}")

print("►◄" * 23)

# -----------------------------
# Convert date column
# -----------------------------
vale3resumo["Data"] = pd.to_datetime(
    vale3resumo["Data"],
    format="%d/%m/%Y"
)

# -----------------------------
# Closing price chart
# -----------------------------
plt.figure(figsize=(11, 6))

plt.plot(
    vale3resumo["Data"],
    vale3resumo["Fechamento"],
    label="VALE3",
    color="blue"
)

plt.title("VALE3 Closing Price (Nov/2024 - Feb/2025)")
plt.xlabel("Date")
plt.ylabel("Closing Price (R$)")
plt.legend()
plt.grid(True)

# Save figure (recommended for GitHub)
# plt.savefig("images/vale3_price_analysis.png", dpi=300, bbox_inches="tight")

plt.show()
