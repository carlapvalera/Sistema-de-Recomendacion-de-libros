import json

class Json():
    def __init__(self, matrix, path):
       self.matrix = matrix
       self.path = path

    def save(self):
        # Crear una matriz
        #matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        # Convertir la matriz a un objeto JSON
        datos_json = json.dumps(self.matrix)

        # Guardar el objeto JSON en un archivo
        with open(self.path +"\\datamatriz.json", "w") as archivo:
            archivo.write(datos_json)

    def load(self):
        # Abrir el archivo JSON
        with open(self.path +"\\datamatriz.json", "r") as archivo:
            datos_json = json.load(archivo)

        # Convertir el objeto JSON a una matriz
        return datos_json

        # Imprimir la matriz
        #print(matriz)
