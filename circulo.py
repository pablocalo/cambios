from math import pi

"""Este es mi pull request a Pablo"""
class Circulo:

    _radio:float

    def __init__(self,radio:float):
        self._radio = radio
    
    #Método área del círculo
    def area(self):
        area = self._radio **2 * pi
        return area

    #Método circunferencia del círculo
    def circunferencia(self, _radio):
        circunferencia = self._radio * 2 * pi
        return circunferencia