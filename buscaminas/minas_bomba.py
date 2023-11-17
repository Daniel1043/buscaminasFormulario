import random

class Casilla: #Es una clase que representa cada celda del tablero
    def __init__(self):
        self.contiene_mina = False 
        self.minas_adyacentes = 0
        self.adyacentes = [] #Una lista que contiene las coordenadas de las casillas adyacentes.

class Tablero:
    def __init__(self, filas, columnas, num_minas): #inicializa el tablero con las dimensiones dadas y el número de minas especificadas.
        self.filas = filas
        self.columnas = columnas
        self.num_minas = num_minas
        self.tablero = [[Casilla() for _ in range(columnas)] for _ in range(filas)] #Una matriz que contiene objetos de la clase Casilla.
        self.generar_minas() # Coloca aleatoriamente las minas en el tablero.
        self.calcular_minas_adyacentes() #Calcula el número de minas adyacentes para cada casilla del tablero.

    def generar_minas(self):
        minas_generadas = 0
        while minas_generadas < self.num_minas:
            fila = random.randint(0, self.filas - 1)
            columna = random.randint(0, self.columnas - 1)
            if not self.tablero[fila][columna].contiene_mina:
                self.tablero[fila][columna].contiene_mina = True
                minas_generadas += 1

    def calcular_minas_adyacentes(self):
        for fila in range(self.filas):
            for columna in range(self.columnas):
                casilla = self.tablero[fila][columna]
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if 0 <= fila + i < self.filas and 0 <= columna + j < self.columnas:
                            casilla.adyacentes.append((fila + i, columna + j))
                            if self.tablero[fila + i][columna + j].contiene_mina:
                                casilla.minas_adyacentes += 1

    def mostrar_tablero(self): #crea una representación del tablero en forma de una lista de listas. Para cada casilla, se representa 'M' si contiene una mina, se muestra el número de minas adyacentes si es mayor que cero, y se deja en blanco si no hay minas adyacentes.
        tablero_html = []
        for fila in range(self.filas):
            fila_html = []
            for columna in range(self.columnas):
                casilla = self.tablero[fila][columna]
                if casilla.contiene_mina:
                    fila_html.append('M')
                elif casilla.minas_adyacentes > 0:
                    fila_html.append(str(casilla.minas_adyacentes))
                else:
                    fila_html.append('')
            tablero_html.append(fila_html)

        return tablero_html


