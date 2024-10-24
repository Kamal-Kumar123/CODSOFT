# -*- coding: utf-8 -*-
"""MovieGenreDetection.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18bVT5svx2bV5x6GeKbD1m-EA-RhafTzC
"""

# dataset for training:     https://drive.google.com/file/d/17eyoEZtrqIxk9y82UE8xnY0pSWSOmFno/view?usp=drive_link
# dataset for testing solution:     https://drive.google.com/file/d/1yWj_hM5u94p0K2rGhByi88FO8nkYEsZ6/view?usp=drive_link
#dataset for testing :     https://drive.google.com/file/d/1HVHwk1eJ8z-zC8thhhh-cwYmdOF2k_JM/view?usp=drive_link


# importing the python libraries
import pandas as pd    #used for importing data into this file
from sklearn.model_selection import train_test_split       # it is used to split the data into training and testing sets
from sklearn.feature_extraction.text import TfidfVectorizer    # used to convert text data into numerical vectors
from sklearn.naive_bayes import MultinomialNB      #this is a classifier
# from sklearn.linear_model import LogisticRegression
# from sklearn.svm import SVC               we don't used these two because we have to use only one model
from sklearn.metrics import accuracy_score, classification_report    #it is used for checking report of accuracy of model
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
#  The nltk (Natural Language Toolkit) library contains many useful corpora, tools, and functionalities for working with human language data (text).
nltk.download('punkt')
nltk.download('stopwords')        #these two packages if downloaded then output show True for this

# from google.colab import drive
# drive.mount('/content/drive')
# !ls /content/drive/"My Drive"/"CODESOFT PROJECTS"/"Movie Genre Detection"

# loading the dataset
data = pd.read_csv("/content/formatted_movies_genre_train.csv")             #Importing the data files from csv file
print(data.head())
data1 = pd.read_csv("/content/formatted_test_data.csv")
data2 = pd.read_csv("/content/formatted_test_data_solution.csv")

# process of text data
# Preprocess the text: lowercase, remove stop words, and tokenize
stop_words = set(stopwords.words('english'))
plot_summaries = data['Plot Summary']
plot_summaries1 = data1['Plot Summary']
plot_summaries2 = data2['Genre']
#below is just a preprocessing function used for process of data like text
def preprocess_text(text):
    # Tokenize and lowercase the text
    tokens = word_tokenize(text.lower())
    # Remove stopwords
    tokens = [word for word in tokens if word.isalpha() and word not in stop_words]
    return ' '.join(tokens)

# Apply preprocessing to the plot summaries and detection the words
data['clean_Plot_Summary'] = plot_summaries.apply(preprocess_text)
data1['clean_Plot_Summary1'] = plot_summaries1.apply(preprocess_text)
data2['Genre'] = plot_summaries2.apply(preprocess_text)

# Inspect the cleaned data
print(data['clean_Plot_Summary'].head())

# feature extraction TF-IDF
# Convert the text into numerical vectors using TF-IDF

tfidf_vectorizer = TfidfVectorizer(max_features=5000)
X = tfidf_vectorizer.fit_transform(data['clean_Plot_Summary'])
X1 = tfidf_vectorizer.fit_transform(data1['clean_Plot_Summary1'])

# Define the target variable (the genre)  and take this as a separate column and store in a variable
Y = data['Genre']
Y1 = data2['Genre']
# print(data['Genre'].isnull().sum())  # Check for missing values
# data = data.dropna(subset=['Genre'])  # Drop rows with missing genres
# print(data.columns)

# Train a Naive Bayes classifier
nb_model = MultinomialNB()
nb_model.fit(X,Y)    #Here X,Y are x_train, y_train   and X1 is x_test and Y1 is y_test

# Make predictions
y_pred_nb = nb_model.predict(X1)

# Evaluate performance
print("Naive Bayes Accuracy:", accuracy_score(Y1, y_pred_nb))
print(classification_report(Y1, y_pred_nb))