import matplotlib.pyplot as plt

def graficar_porcentajes(porcentajes, titulo="Distribución de grupos sanguíneos"):
    grupos = list(porcentajes.keys())
    valores = list(porcentajes.values())

    plt.figure(figsize=(6, 6))
    plt.pie(valores, labels=grupos, autopct="%1.1f%%", startangle=90)
    plt.title(titulo)
    plt.show()