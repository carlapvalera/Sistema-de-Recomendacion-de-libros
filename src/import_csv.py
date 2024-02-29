import pandas as pd
from dotenv import load_dotenv
import os

# Function to get the file path
def get_file_path(folder_name, file_name):
    """
    This function takes a folder name and a file name as input and returns the file path.
    """
    file_path = os.path.join('..',folder_name, file_name)
    return file_path

# Function to import a csv file
def import_csv(file_path):
    """
    This function takes a file path as input and returns a pandas DataFrame.
    """
    data = pd.read_csv(file_path)
    return data

# Function to get column names
def get_column_names(data):
    """
    This function takes a pandas DataFrame as input and returns the column names.
    """
    column_names = data.columns
    return column_names

# Function to select columns and convert to list
def select_columns_to_list(data, column_names):
    """
    This function takes a pandas DataFrame and a list of column names as input.
    It returns a list of values for the selected columns.
    """
    selected_columns = data[column_names]
    return selected_columns.values.tolist()

# Function to concatenate strings
# Function to concatenate strings
def concatenate_strings(string_list):
    """
    This function takes a list of strings as input and returns a single string
    where all the input strings are concatenated with a space in between.
    """
    # Convert each item in the list to a string before joining
    concatenated_string = ' '.join(str(item) for item in string_list)
    return concatenated_string

# Function to get data
def get_data():
    """
    This function takes a list of files as input.
    It loads environment variables from a .env file, imports a csv file,
    gets column names, selects columns to list, and concatenates selected columns.
    It returns a list of selected names and a list of concatenated columns.
    """
    # Load environment variables from .env file
    load_dotenv()
    folder_dir=os.getenv("DATAFOLDER")
    file_dir=os.getenv("DATAFILE")
    # Load DataFrame
    data=import_csv(get_file_path(folder_dir, file_dir))
    # Get column names
    names=get_column_names(data)
    # Select columns to list
    select_names=select_columns_to_list(data, names[1])
    selected_columns=select_columns_to_list(data, names[2:15])
    # Concatenate selected columns
    concatenated_columns=[]
    for i in selected_columns:
        concatenated_columns.append(concatenate_strings(i))

    return select_names, concatenated_columns



