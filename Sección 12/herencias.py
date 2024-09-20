class Animal:
    def comer(self):
        print('Come muchas veces al dias')

    def dormir(self):
        print('Duerme muchas horas')

class Perro(Animal):
    def hace_ruid0(self):
        print('Puede ladrar')

#Programa pincipal

print('*** Ejemplo de Herencia en Python ***')
print('Clase Padre, soy un animal')
animal1 = Animal()
animal1.comer()
animal1.dormir()
