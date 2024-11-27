import time
import numpy as np
import sys

#imprimir con demora
def imprimir_con_retraso(s):
    #imprimir una letra a la vez
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

#crear la clase
class Pokemon:
    def __init__(self, nombre, tipos, movimientos, EVs, puntos_de_salud='===================='):
        #guardar las variables como atributos
        self.nombre = nombre
        self.tipos = tipos
        self.movimientos = movimientos
        self.ataque = EVs['ataque']
        self.defensa = EVs['defensa']
        self.puntos_de_salud= puntos_de_salud
        self.barras = 20 #amount of puntos de salud barras

    def impresa(self, Pokemon2):
        '''Imprimir información de lucha
        '''
        print("----BATALLA POKEMON----")
        print(f'\n{self.nombre}')
        print("tipo/", self.tipos)
        print("ataque/", self.ataque)
        print("defensa/", self.defensa)
        print("Nv./", 3*(1+np.mean([self.ataque, self.defensa])))
        print("\nVs")
        print(f'\n{self.nombre}')
        print("tipo/", Pokemon2.tipos)
        print("ataque/", Pokemon2.ataque)
        print("defensa/", Pokemon2.defensa)
        print("Nv./", 3*(1+np.mean([Pokemon2.ataque, Pokemon2.defensa])))
        time.sleep(2)

    def ventaja(self, Pokemon2):
        '''Considerar la ventaja de tipo
        Actualiza poderes de ataque y defensa
        Devuelve dos cadenas de información
        '''
        version= ['fuego', 'agua', 'planta']
        for i,k in enumerate(version):

            if self.tipos == k:
                #son mismo tipo
                if Pokemon2.tipos == k:
                    cadena_1_ataque = '\nNo es muy efectivo...'
                    cadena_2_ataque = '\nNo es muy efectivo...'

                #Pokemon es FUERTE
                if Pokemon2.tipos == version[(i+1)%3]:
                    Pokemon2.ataque *= 2
                    Pokemon2.defensa *= 2
                    self.ataque /= 2
                    self.defensa /= 2
                    cadena_1_ataque = '\nNo es muy efectivo...'
                    cadena_2_ataque = '\nEs muy efectivo...'

                #Pokemon es DEBIL
                if Pokemon2.tipos == version[(i+2)%3]:
                    self.ataque *= 2
                    self.defensa *= 2
                    Pokemon2.ataque /=2
                    Pokemon2.defensa/= 2
                    cadena_1_ataque = '\nEs muy efectivo...'
                    cadena_2_ataque = '\nNo es muy efectivo...'

        return cadena_1_ataque, cadena_2_ataque

    def turno(self, Pokemon2, cadena_1_ataque, cadena_2_ataque):
        '''Empieza con Pokemon1, elige ataque y calcular
        los nuevos puntos de salud
        Hace lo mismo con pokemon2. Hasta que los puntos de salud
        de uno de los pokemon son <0
        Actualizar los datos.
        '''
        while (self.barras>0) and (Pokemon2.barras>0):

            #imprimir los puntos de salud de cada pokemon
            print(f"\n{self.nombre}\t\tPS\t{self.puntos_de_salud}")
            print(f"\n{Pokemon2.nombre}\t\tPS\t{Pokemon2.puntos_de_salud}\n")

            #Pokemon 1
            print(f"Adelante {self.nombre}")
            for i, x in enumerate(self.movimientos):
                print(f"{i+i}.", x)
            index = int(input('Elige un movimiento: '))
            imprimir_con_retraso(f"\n{self.nombre} uso {self.movimientos[index-1]}!")
            time.sleep(1)
            imprimir_con_retraso(cadena_1_ataque)

            #determinar el daño
            Pokemon2.barras -= self.ataque
            Pokemon2.puntos_de_salud=""

            #agregar barras adicionales mas defensa boost
            for j in range(int(Pokemon2.barras+.1*Pokemon2.defensa)):
                Pokemon2.puntos_de_salud += "="

            time.sleep(1)
            print(f"\n{self.nombre}\t\tPS\t{self.puntos_de_salud}")
            print(f"\n{Pokemon2.nombre}\t\tPS\t{Pokemon2.puntos_de_salud}")
            time.sleep(.5)

            #Comprueba si pokemon se debilitó
            if Pokemon2.barras <= 0:
                imprimir_con_retraso("\n..." + Pokemon2.nombre + ' se debilito')
                break

            # Pokemon 2
            print(f"Adelante {Pokemon2.nombre}")
            for i, x in enumerate(Pokemon2.movimientos):
                print(f"{i + i}.", x)
            index = int(input('Elige un movimiento: '))
            imprimir_con_retraso(f"\n{Pokemon2.nombre} uso {Pokemon2.movimientos[index - 1]}!")
            time.sleep(1)
            imprimir_con_retraso(cadena_2_ataque)

            # determinar el daño
            self.barras -= Pokemon2.ataque
            self.puntos_de_salud = ""

            # agregar barras adicionales mas defensa boost
            for j in range(int(self.barras + .1 * self.defensa)):
                self.puntos_de_salud += "="

            time.sleep(1)
            print(f"\n{self.nombre}\t\tPS\t{self.puntos_de_salud}")
            print(f"\n{Pokemon2.nombre}\t\tPS\t{Pokemon2.puntos_de_salud}")
            time.sleep(.5)

            # Comprueba si pokemon se debilitó
            if self.barras <= 0:
                imprimir_con_retraso("\n..." + self.nombre + ' se debilito')
                break

    def lucha(self, Pokemon2):
        '''Permitir que dos pokemon luchen entre ellos
        '''

        #Imprimir información de lucha
        self.impresa(Pokemon2)

        #Considerar la ventaja de tipo
        cadena_1_ataque, cadena_2_ataque = self.ventaja(Pokemon2)

        #Ahora para la lucha real
        #Continua mientras POkemon aun tenga mas puntos de salud
        self.turno(Pokemon2, cadena_1_ataque, cadena_2_ataque)

        #Recibir dinero (premio)
        money = np.random.choice(5000)
        imprimir_con_retraso(f"\nEl oponente te pago ${money}.\n")

if __name__ == '__main__':
    #Crear Pokemon objeto
    Charizard = Pokemon('Charizard', 'fuego', ["Lanzallamas", "Pirotecnia", "Giro Fuego", "Ascuas"], {'ataque':12, 'defensa':8})
    Blastoise = Pokemon('Blastoise', 'agua', ["Pistola Agua", "Burbuja", "Hidropulso", "Hidrobomba"], {'ataque':10, 'defensa':10})
    Venusaur = Pokemon('Venusaur', 'planta', ["Latigo Cepa", "Hoja afilada", "Somnifero", "Rayo Solar"], {'ataque':10, 'defensa':10})
    Venusaur.lucha(Blastoise)
