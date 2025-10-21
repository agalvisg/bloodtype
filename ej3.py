

class GrupoSangDescriptor:  #Se usa para controlar cómo se asignan los valores
    def __set__(self,instance, value):
        if value not in ["A","B","AB","O"]:
            raise ValueError("grupo Sanguíneo inválido")
        instance.__dict__["grupo_sanguineo"] = value

    def __get__(self, instance, owner):
        return instance.__dict__["grupo_sanguineo"]

class Persona:
    grupo_sanguineo = GrupoSangDescriptor()
    genotipos_map = {"A": ["AA", "AO"],
                     "B": ["BB", "BO"],
                     "AB": ["AB"],
                     "O": ["OO"]}


    def __init__(self, nombre, grupo):
        self.nombre = nombre
        self.grupo_sanguineo = grupo


    @property
    def genotipo(self):
        return Persona.genotipos_map[self.grupo_sanguineo]

    @staticmethod
    def validar_grupo(grupo):
        if grupo not in Persona.genotipos_map:
            raise ValueError("Grupo sanguíneo invalido")

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
    

