# En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga como atributos su nombre y su nota. Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.
class Alumno :
    _nombre = None
    _nota = 0
    _nota_minima = 3.5

    def __init__( self, nombre, nota ) :
        self._nombre = nombre
        self._nota = nota

    def resultado( self ) :
        return f'{ self._nombre } con una nota de { self._nota } { "ha aprobado" if self._nota >= self._nota_minima else f"NO aprobó, la nota minima es de { self._nota_minima }" } '

juan = Alumno( 'Juan', 4.5 )
print( juan.resultado() )

juliana = Alumno( 'Juliana', 3 )
print( juliana.resultado() )