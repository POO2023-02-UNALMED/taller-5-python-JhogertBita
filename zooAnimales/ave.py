from zooAnimales.animal import Animal
class Ave(Animal):
    _listaAves = []
    halcones = 0
    aguilas = 0
    def __init__(self, nombre, edad, habitat, genero, pluma):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = pluma
        Ave._listaAves.append(self)
    @classmethod
    def cantidadAves(cls):
        return len(cls._listaAves)
    @staticmethod
    def movimiento():
        return "volar"
    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        cls.halcones += 1
        return cls(nombre, edad, "montana", genero, "cafe glorioso")
    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        cls.aguilas += 1
        return cls(nombre, edad, "montana", genero, "blanco y amarillo")
    @classmethod
    def getHalcones (cls):
        return cls.halcones
    @classmethod
    def setHalcones (cls, halcones):
        cls.halcones = halcones
    @classmethod
    def getAguilas (cls):
        return cls.aguilas
    @classmethod
    def setAguilas (cls, aguilas):
        cls.aguilas = aguilas
    def getColorPlumas(self):
        return self._colorPlumas
    def setColorPlumas(self, colorPlumas):
        self._colorPlumas = colorPlumas