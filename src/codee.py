# Import libraries
import csv
import os
import re, os
import nltk
from gensim import corpora
import pandas as pd
from gensim.models import TfidfModel
from gensim import similarities
from scipy.cluster import hierarchy
import matplotlib.pyplot as plt
import import_csv as imp
class Process():
    def __init__(self, path):
        self.path = path
        self.txts = []
        self.titles = []
        self.dictionary = {}
     


    def title_text(self):
        global txts 
        global titles 

        titless, texts=imp.get_data()

        self.titles=titless[0:10]
        self.txts=texts[0:10]

                
        


    def remove_noise(self):
        texts = [
                [word.lower() for word in doc if word.isalpha()] for doc in self.txts]
        self.txts = texts

    #remove stopwords
    def remove_stopwords(self):
        # Define a list of stop words
        stoplist = set('for a of the and to in to be which some is at that we i who whom show via may my our might as well'.split())
        # Remove tokens which are part of the list of stop words
        self.txts = [[word for word in txt if word not in stoplist] for txt in self.txts]
        

    #tokenize
    def tokenization(self):
        return[t.split(' ') for t in self.txts]

    #morphological_reduction
    def morphological_reduction(tokenized_docs, use_lemmatization=True):
        stemmer = nltk.stem.PorterStemmer()
        return [
            [token.lemma_ if use_lemmatization else stemmer.stem(token.text) for token in doc]
            for doc in tokenized_docs
        ]

    def normalize_text(self,texts):
        # Convert the text to lower case 
        txts_lower_case = [t.lower() for t in texts ]
        self.txts = txts_lower_case
        # Transform the text into tokens 
        txts = self.tokenization()

        #Remove noise
        txts = self.remove_noise()
        # remove stopwords
        txts = self.remove_stopwords()
        #morphological_reduction
        #txts = morphological_reduction(txts)
        # Print the first 20 tokens for the "On the Origin of Species" book
        return self.txts

    #print(normalize_text(txts))

    def update_dictionary(self):
        global dictionary
        # Create a dictionary from the stemmed tokens
        dictionary = corpora.Dictionary(self.txts)

    def generate_bow(self):
        self.update_dictionary()
        # Create a bag-of-words model for each book, using the previously generated dictionary
        bows = [dictionary.doc2bow(t) for t in self.txts]
        return bows

    def Dataframe(self,texts):
        bows = self.generate_bow(texts)
        for ori in range(len(texts)):
            # Convert the BoW model for "On the Origin of Species" into a DataFrame
            df_bow_origin = pd.DataFrame(bows[ori])

            # Add the column names to the DataFrame
            df_bow_origin.columns = ['index', 'occurrences']

            # Add a column containing the token corresponding to the dictionary index
            df_bow_origin['token'] = df_bow_origin['index'].apply(lambda x: dictionary[x])

            # Sort the DataFrame by descending number of occurrences and print the first 10 values
            df_bow_origin = df_bow_origin.sort_values('occurrences', ascending=False)
            print(df_bow_origin.head(10))
            # Convert the BoW model for "On the Origin of Species" into a DataFrame
            df_bow_origin = pd.DataFrame(bows[ori])

            # Add the column names to the DataFrame
            df_bow_origin.columns = ['index', 'occurrences']

            # Add a column containing the token corresponding to the dictionary index
            df_bow_origin['token'] = df_bow_origin['index'].apply(lambda x: dictionary[x])

            # Sort the DataFrame by descending number of occurrences and print the first 10 values
            df_bow_origin = df_bow_origin.sort_values('occurrences', ascending=False)
            print(df_bow_origin.head(10))

    #Dataframe(normalize_text(txts))

    #create tf-idf model
    def tf_idf(self,texts):
        bows = self.generate_bow(texts)
        self.update_dictionary(texts)
        # Generate the tf-idf model
        model = TfidfModel(bows)
        ori=0
        # Print the model for "On the Origin of Species"
        print(model[bows[ori]][:5])

        # Convert the tf-idf model for "On the Origin of Species" into a DataFrame
        df_tfidf = pd.DataFrame(model[bows[ori]])

        # Name the columns of the DataFrame id and score
        df_tfidf.columns = ['id', 'score']

        # Add the tokens corresponding to the numerical indices for better readability
        df_tfidf['token'] = df_tfidf['id'].apply(lambda x: dictionary[x])

        # Sort the DataFrame by descending tf-idf score and print the first 10 rows.
        df_tfidf = df_tfidf.sort_values('score', ascending=False)
        print(df_tfidf.head(10))


    #similarity matrix
    def create_similarity_matrix(self):
        bows = self.generate_bow()
        # Generate the tf-idf model
        model = TfidfModel(bows)
    
        # Compute the similarity matrix (pairwise distance between all texts)
        sims = similarities.MatrixSimilarity(model[bows])

        # Transform the resulting list into a dataframe
        sim_df = pd.DataFrame(list(sims))

        # Add the titles of the books as columns and index of the dataframe
        sim_df.columns = self.titles
        sim_df.index = self.titles
        return sim_df

    #sim_df = create_similarity_matrix(normalize_text(txts))

    # Print the resulting matrix
    #print(sim_df)


  # This is needed to display plots in a notebook

    def plot_val(self,sim_df,query):

        # Select the column corresponding to "query" and 
        v = sim_df[query]

        # Sort by ascending scores
        v_sorted = v.sort_values(ascending=True)
        # Sort by ascending scores
        #v_sorted =sorted(v.items(), key=lambda x: x[1], reverse=True)


        # Plot this data has a horizontal bar plot
        v_sorted.plot.barh(x='lab', y='val', rot=0).plot()

        # Modify the axes labels and plot title for better readability
        plt.xlabel("Cosine distance")
        plt.ylabel("")
        plt.title("Most similar books to "+query)

        # Show the plot
        plt.show()
    #plot_val(sim_df)

   
    def plot_dendrogram(self,sim_df):
        # Compute the clusters from the similarity matrix,
        # using the Ward variance minimization algorithm
        Z = hierarchy.linkage(sim_df, 'ward')

        # Display this result as a horizontal dendrogram
        a = hierarchy.dendrogram(Z,  leaf_font_size=8, labels=sim_df.index,  orientation="left")
        plt.show()
        
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
        # Load the JSON data into a DataFrame
        matriz = pd.read_json(self.path+"\\datamatriz.json")
        #Imprimir la matriz
        print(matriz)
        return matriz