# Books Cosine Similarites Recommendation System

## Authors:
- Carla Sunami Perez Valera(carlapvalera)
- Francisco Suarez Bellon(fvsb)

To this purpose, we will develop the bases of a content-based book recommendation system, which will determine which books are close to each other based on how similar the discussed topics are. The methods we will use are commonly used in text- or documents-heavy industries such as legal, tech or customer support to perform some common task such as text classification or handling search engine queries.

Let's take a look at the books we'll use in our recommendation system.

## Load the contents of each book into Python
As a first step, we need to load the content of these books into Python and do some basic pre-processing to facilitate the downstream analyses. We call such a collection of texts a corpus. We will also store the titles for these books for future reference and print their respective length to get a gauge for their contents.


## Tokenize the corpus
As a next step, we need to transform the corpus into a format that is easier to deal with for the downstream analyses. We will tokenize our corpus, i.e., transform each text into a list of the individual words (called tokens) it is made of. To check the output of our process.


## Stemming of the tokenized corpus
If you have read On the Origin of Species, you will have noticed that Charles Darwin can use different words to refer to a similar concept. For example, the concept of selection can be described by words such as selection, selective, select or selects. This will dilute the weight given to this concept in the book and potentially bias the results of the analysis.

To solve this issue, it is a common practice to use a stemming process, which will group together the inflected forms of a word so they can be analysed as a single item: the stem. 


## Building a bag-of-words model
Now that we have transformed the texts into stemmed tokens, we need to build models that will be useable by downstream algorithms.

First, we need to will create a universe of all words contained in our corpus , which we call a dictionary. Then, using the stemmed tokens and the dictionary, we will create bag-of-words models (BoW) of each of our texts. The BoW models will represent our books as a list of all uniques tokens they contain associated with their respective number of occurrences.


## The most common words of a given book
The results returned by the bag-of-words model is certainly easy to use for a computer but hard to interpret for a human. It is not straightforward to understand which stemmed tokens are present in a given book , and how many occurrences we can find.

In order to better understand how the model has been generated and visualize its content, we will transform it into a DataFrame and display 


## Build a tf-idf model
If it wasn't for the presence of the stem "speci", we would have a hard time to guess this BoW model comes . The most recurring words are, apart from few exceptions, very common and unlikely to carry any information peculiar to the given book. We need to use an additional step in order to determine which tokens are the most specific to a book.

To do so, we will use a tf-idf model (term frequency–inverse document frequency). This model defines the importance of each word depending on how frequent it is in this text and how infrequent it is in all the other documents. As a result, a high tf-idf score for a word will indicate that this word is specific to this text.

After computing those scores, we will print the 10 words most specific to the book (i.e., the 10 words with the highest tf-idf score).


## Compute distance between texts
The results of the tf-idf algorithm now return stemmed tokens which are specific to each book. We can, for example, see that topics such as selection. Now that we have a model associating tokens to how specific they are to each book, we can measure how related to books are between each other.

To this purpose, we will use a measure of similarity called cosine similarity and we will visualize the results as a distance matrix, i.e., a matrix showing all pairwise distances between  books.


## The book most similar 
We now have a matrix containing all the similarity measures between any pair of books! We can now use this matrix to quickly extract the information we need, i.e., the distance between one book and one or several others.


## Which books have similar content? EXTRA
This turns out to be extremely useful if we want to determine a given book's most similar work. 

However, we now want to have a better understanding of the big picture and see how  books are generally related to each other (in terms of topics discussed). To this purpose, we will represent the whole similarity matrix as a dendrogram, which is a standard tool to display such data. This last approach will display all the information about book similarities at once. For example, we can find a book's closest relative but, also, we can visualize which groups of books have similar topics (e.g., the cluster about Charles Darwin personal life with his autobiography and letters). If you are familiar with Darwin's bibliography, the results should not surprise you too much, which indicates the method gives good results. Otherwise, next time you read one of the author's book, you will know which other books to read next in order to learn more about the topics it addressed.



## Levenshtein distance EXTRA
The Levenshtein distance measures the difference between two strings by counting the minimum number of edit operations (insertions, deletions, and substitutions) required to transform one string into the other.
We use it to guide the user in the event that they make a mistake when communicating with Claus.
