import pandas as pd
from dotenv import load_dotenv
import os
def get_file_path(folder_name, file_name):
    file_path = os.path.join('..',folder_name, file_name)
    return file_path
def import_csv(file_path):
    data = pd.read_csv(file_path)
    return data

def get_column_names(data):
    column_names = data.columns
    return column_names




def select_columns_to_list(data, column_names):
    selected_columns = data[column_names]
    return selected_columns.values.tolist()


def concatenate_strings(string_list):
    concatenated_string = ' '.join(string_list)
    return concatenated_string


def get_data(self, files):
    # Carga las variables de entorno del archivo .env
    load_dotenv()
    folder_dir=os.getenv("DATAFOLDER")
    folder_file=os.getenv("DATAFILE")
    #Cargar el dataframe
    data=import_csv(get_file_path("input", "dataset.csv"))
    #Obtener los nombres de las columnas
    names=get_column_names(data)
    #Seleccionar las columnas a listar
    select_names=select_columns_to_list(data, names[1])
    selected_columns=select_columns_to_list(data, names[2:15])
    #Concatenar las columnas seleccionadas
    concatenated_columns=[]
    for i in selected_columns:
        concatenated_columns.append(concatenate_strings(i))

    return select_names, concatenated_columns