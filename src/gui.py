# Import libraries
from codee import Json
from codee import Process
import os
import streamlit as st
import pandas as pd

# ... (your existing code for loading data and calculating similarity)

# Obtener la ruta del archivo actual
file_root = os.path.abspath(__file__)

# Obtener la ruta de la carpeta que contiene el archivo
folder_root= os.path.dirname(file_root)
folder_root = os.path.dirname(folder_root)
# Crear una instancia de la clase "Process"
process = Process(folder_root+"\\data")
# Crear una instancia de la clase "Json"
json = Json(None,folder_root+"\\data")
# Imprimir la ruta
#print(ruta_carpeta)
# Importar los archivos .txt y almacenarlos en una lista title y text
process.title_text()
token = process.normalize_text(process.txts)

def import_json(root):
        # Lista para almacenar los archivos .json
        files_json = []

        # Obtener una lista de los archivos en la carpeta
        files = os.listdir(root)

        # Filtrar solo los archivos .txt
        for file in files:
            if file.endswith(".json"):
                files_json.append(file)

        # Imprimir la lista de archivos .txt
        return(files_json) 

if len(import_json(folder_root+"\\data"))==1:
    print("El archivo similarity_matrix.index existe")
    json.matrix = json.load()

else:
    # Crear la matriz de similitud
    matrix = process.create_similarity_matrix()
    print("Se ha creado la matriz de similitud")
    # Guardar la matriz de similitud en un archivo .json
    json.matrix = matrix
    json.save()
    
#print (json.matrix)



def Levenshtein_Distance(string1, string2):
    """
    Implementation of the iterative Levenshtein algorithm.
    """
    m, n = len(string1), len(string2)
    distance_matrix = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Initialize the distance matrix
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                distance_matrix[i][j] = j
            elif j == 0:
                distance_matrix[i][j] = i
            else:
                cost = 0 if string1[i - 1] == string2[j - 1] else 1
                distance_matrix[i][j] = min(
                    distance_matrix[i - 1][j] + 1,  # Insertion
                    distance_matrix[i][j - 1] + 1,  # Deletion
                    distance_matrix[i - 1][j - 1] + cost,  # Substitution
                )

    return distance_matrix[m][n]




st.title("Hi I am Claus, I can recommend you a book based on your preferences.")
st.write(" Let me help you, what book have I already read?. Please enter the title of a book you like.")
query = st.text_input("Enter the title of a book:")
st.write("Here are some examples of books in our database:")
st.write("")
# Assuming you have the similarity matrix 'sim_df' ready
st.subheader("Similarity Matrix Dendrogram")
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot(process.plot_dendrogram(json.matrix))
#st.pyplot(process.plot_dendrogram(json.matrix))


if( query != ""):
    # Find the index of the book in the DataFrame (if it exists)
    try:
        libro_indice = process.titles.index(query)
    except ValueError:
        st.error("El libro ingresado no se encuentra en nuestra base de datos.")
        st.write("Tal vez te interesen estos libros:")
        levenshtein_distance = {}
        for libro in process.titles:
            levenshtein_distance[libro] = Levenshtein_Distance(query, libro)    

        levenshtein = sorted(levenshtein_distance.items(), key=lambda x: x[1])
        st.write(levenshtein[0])
        #st.pyplot(process.plot_val(json.matrix,query))
        # Optionally: Offer suggestions based on user input
        # sugerencias = ... (implement logic to suggest similar books)
        # st.write("Tal vez te interesen estos libros:")
        # for libro in sugerencias:
        #     st.write(f"- {libro}")
        libro_indice = None  # Set to None to avoid errors in subsequent code

    # Proceed with recommendations if a valid book was found
    if libro_indice is not None:
        # ... (your existing code for calculating recommendations based on the selected book)
        # ... (your existing code for displaying the selected book information and recommendations)
        dict = json.matrix[query]
        dict_sorted = sorted(dict.items(), key=lambda x: x[1], reverse=True)
        count = 0
        for key in dict_sorted:
            if count < 10:
                st.write(f"{key}")
                count += 1
            else:
                break
        #Call the plot_val function
        st.subheader("Plot of most similar books")
        st.pyplot(process.plot_val(json.matrix,query))

        # ... your code defining the `plot_val` function ...

        # Assuming you have the DataFrame 'sim_df' and a query ready

        # 1. Display the DataFrame
        st.dataframe(dict)

        # 2. Call the plot_val function
        #st.subheader("Plot of most similar books")

        # 3. Use st.pyplot to display the plot
        #st.pyplot(process.plot_val(query))
        #print(dict)
else:
    # User didn't enter anything, display instructions or placeholders
    st.write("Ingresa el título del libro que te interesa para obtener recomendaciones.")




