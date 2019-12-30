class Persona:
    def saludo_general(self):
        return "hola persona"
    

class Estudiante(Persona):
    def __init__(self, nombre, edad):
        
        self.nombre = nombre
        self.edad = edad
    
    def hola(self):
        return "mi nombre es %s" % self.nombre  


e = Estudiante("luis",30)
print(e.hola())
print(e.saludo_general())

