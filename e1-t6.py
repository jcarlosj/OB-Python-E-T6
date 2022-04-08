# En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos: Color, Ruedas, Puertas
class Vehiculo :
    _color = None
    _ruedas = 0
    _puertas = 0

    def __init__( self, color, ruedas, puertas ) :
        self._color = color
        self._ruedas = ruedas
        self._puertas = puertas

# Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos: Velocidad, Cilindrada
class Coche( Vehiculo ) :
    _velocidad = 0
    _cilindrada = 0
    
    def __init__( self, velocidad, cilindrada, color, ruedas, puertas ) :
        super().__init__( color, ruedas, puertas )

        self._velocidad = velocidad
        self._cilindrada = cilindrada

    def __str__( self ) :
        return f'Coche( \n  color: { self._color }, \n  ruedas: { self._ruedas }, \n  puertas: { self._puertas }, \n  velocidad: { self._velocidad }, \n  cilindrada: { self._cilindrada } \n )'

# Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.
coche = Coche( 250, 4, 'Amarillo', 4, 2 )
print( coche )