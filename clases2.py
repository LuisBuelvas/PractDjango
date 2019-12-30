class Auto:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    ###esta por reparar error de codigo
    
    def desscription(self):
        desc = "% es un %s %s. vale $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc


car1 = Auto()
car1.name = "Ford"
car1.color = "rojo"
car1.value = 123.34

print(car1.desscription())