from zooAnimales.animal import Animal
class Anfibio(Animal):
    _listaAnfibios = []
    ranas = 0
    salamandras = 0
    def __init__(self, nombre, edad, habitat, genero, piel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = piel
        self._venenoso = venenoso
        Anfibio._listaAnfibios.append(self)
    @classmethod
    def cantidadAnfibios(cls):
        return len(cls._listaAnfibios)
    @staticmethod
    def movimiento():
        return "saltar"
    @classmethod
    def crearRana(cls, nombre, edad, genero):
        cls.ranas += 1
        return cls(nombre, edad, "selva", genero, "rojo", True)
    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        cls.salamandras += 1
        return cls(nombre, edad, "selva", genero, "negro y amarillo", False)
    @classmethod 
    def getRanas (cls):
        return cls.ranas
    @classmethod 
    def setRanas (cls, ranas):
        cls.ranas = ranas
    @classmethod 
    def getSalamandras (cls):
        return cls.salamandras
    @classmethod 
    def setSalamandras (cls, salamandras):
        cls.salamandras = salamandras
    def getColorPiel(self):
        return self._colorPiel
    def setColorPiel(self, piel):
        self._colorPiel = piel
    def isVenenoso(self):
        return self._venenoso
    def setVenenoso(self, venenoso):
        self._venenoso = venenoso