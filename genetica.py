def generar_combinaciones(padre,madre):
    resultados = []
    for gen_padre in padre.genotipo:
        for alelo_padre in gen_padre:
            for gen_madre in madre.genotipo:
                for alelo_madre in gen_madre:
                    # combinación ordenada para evitar duplicados como "OA"
                    combinacion = ''.join(sorted([alelo_padre, alelo_madre]))
                    (resultados.append(combinacion))
    return resultados


def calcular_probabilidades(padre,madre):
    combinaciones = generar_combinaciones(padre,madre) #se generan las combinaciones posibles llamando a la función

    #Mapeo de combinaciones a grupos sanguíneos
    map_grupo = {"AA": "A", "AO": "A", "OA": "A",
                "BB": "B", "BO": "B", "OB": "B",
                "AB": "AB", "BA": "AB",
                "OO": "O"}
    conteo_grupos = {"A": 0, "B": 0, "AB": 0, "O": 0} #inicialización del conteo

    for comb in combinaciones:
        grupo  = map_grupo.get(comb)
        if grupo:
            conteo_grupos[grupo] += 1

    total = sum(conteo_grupos.values())
    if total == 0:
        return {k: 0 for k in conteo_grupos.keys()}

    porcentajes = {k: (v / total) * 100 for k, v in conteo_grupos.items()}

    return porcentajes