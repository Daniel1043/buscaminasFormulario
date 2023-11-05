import random
from django.shortcuts import render, redirect
from views import coor_minas

class Casilla:
    def __init__(self, coordenadas, minas=False, minas_adyacentes=0):
        self.coordenadas = coordenadas
        self.minas = minas
        self.minas_adyacentes = minas_adyacentes

    def __str__(self):
        return f"({self.coordenadas[0]}, {self.coordenadas[1]})"

class Tablero:
    def __init__(self, columnas, filas, numMinas):
        self.num_columnas = columnas
        self.num_filas = filas
        self.num_minas = numMinas
        self.casillas = []

        for fila in range(filas):
            for columna in range(columnas):
                coordenadas = (fila, columna)
                minas = False
                casilla = Casilla(coordenadas, minas)
                self.casillas.append(casilla)

        coor_minas = set()
        for i in range(numMinas):
            randomFila = random.randint(0, filas - 1)
            randomColumna = random.randint(0, columnas - 1)
            coor_minas.add((randomFila, randomColumna))

        for casilla in self.casillas:
            fila, columna = casilla.coordenadas
            adyacentes_coords = [
                (fila-1, columna-1), (fila-1, columna), (fila-1, columna+1),
                (fila, columna-1), (fila, columna+1),
                (fila+1, columna-1), (fila+1, columna), (fila+1, columna+1)
            ]
            for coords in adyacentes_coords:
                fila_ady, columna_ady = coords
                if (0 <= fila_ady < self.num_filas) and (0 <= columna_ady < self.num_columnas):
                    adyacente = self.get_casilla(coords)
                    if adyacente.minas:
                        casilla.minas_adyacentes += 1

    def get_casilla(self, coordenadas):
        for casilla in self.casillas:
            if casilla.coordenadas == coordenadas:
                return casilla
        return None