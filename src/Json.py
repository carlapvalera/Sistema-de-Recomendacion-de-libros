import json

class Json():
    def __init__(self, matrix, path):
       self.matrix = matrix
       self.path = path

    def save(self):
        # Crear una matriz
        #matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        # Convertir la matriz a un objeto JSON
        self.matrix.to_json(self.path +"\\datamatriz.json")

    def load(self):
        # Abrir el archivo JSON
        with open(self.path +"\\datamatriz.json", "r") as archivo:
            datos_json = json.load(archivo)

        # Convertir el objeto JSON a una matriz
        return datos_json

        # Imprimir la matriz
        #print(matriz)
