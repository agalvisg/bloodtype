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
        self.grupo_sanguineo = self.normalizar_grupo(grupo)


    @property
    def genotipo(self):
        return Persona.genotipos_map[self.grupo_sanguineo]

    @staticmethod
    def normalizar_grupo(grupo):
        try:
            # Normalización de tipo
            if grupo is None:
                raise ValueError("El grupo sanguíneo está vacío (None).") #Controla Valor nulo
            elif isinstance(grupo, int):
                if grupo == 0:
                    return "O"
                else:
                    raise ValueError(f"Número no válido como grupo sanguíneo: {grupo}") # Controla números inválidos
            elif isinstance(grupo, str):
                grupo = grupo.strip().upper()
                if grupo == "0":
                    grupo = "O"
                elif grupo not in ["A", "B", "AB", "O"]:
                    raise ValueError(f"Valor no válido: '{grupo}'") # Controla cadenas inválidas
                return grupo
            raise TypeError(f"Tipo de dato inesperado para grupo sanguíneo: {type(grupo)}") # Controla tipos de datos inesperados
        except Exception as e:
            print(f"[Error al procesar grupo sanguíneo] {e}") #se guarda y printa el error para debug
            raise