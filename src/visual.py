import streamlit as st
import pandas as pd

# ... (your existing code for loading data and calculating similarity)







st.title("Hi I am Claus, I can recommend you a book based on your preferences.")
st.write(" Let me help you, what book have I already read?. Please enter the title of a book you like.")
query = st.text_input("Enter the title of a book:")
st.write("Here are some examples of books in our database:")
st.write("")


# Ask the user for their input
libro_buscado = st.text_input("Ingresa el título del libro que te interesa:")

# Check if user entered a title
'''if libro_buscado:
    # Find the index of the book in the DataFrame (if it exists)
    try:
        libro_indice = libros.index[libros["titulo"] == libro_buscado].tolist()[0]
    except IndexError:
        st.error("El libro ingresado no se encuentra en nuestra base de datos.")
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
        print 
else:
    # User didn't enter anything, display instructions or placeholders
    st.write("Ingresa el título del libro que te interesa para obtener recomendaciones.")'''
