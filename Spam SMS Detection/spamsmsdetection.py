# -*- coding: utf-8 -*-
"""SpamSMSdetection.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cyhaY3uvJOM4IqNKoGnlBEkGVz5p6Qbz
"""

# dataset link:    https://drive.google.com/file/d/1A2ySkoOIaAdSA_Bx-QX6BV2RBK-XamgX/view?usp=drive_link

# importing all the required libraries for analyzing text

import pandas as pd   #for importing data into ipynb file
import numpy as np     #for making matrix and used of confusion matrix
from sklearn.model_selection import train_test_split    #for splitting data into train and test
from sklearn.feature_extraction.text import TfidfVectorizer    #for seperating features from text
from sklearn.naive_bayes import MultinomialNB     #this is a classification model
from sklearn.linear_model import LogisticRegression     #this is a classification model
from sklearn.svm import SVC           #this is also a classification model
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix      #checking last accuracy of model and whole report

# Load the dataset (assuming it's in CSV format)
data = pd.read_csv('/content/spam.csv', encoding='latin-1')     #The use of encoding='latin-1' is relevant when loading datasets that contain special characters or non-ASCII content.

# Clean the data (keep only relevant columns)
data = data[['v1', 'v2']]
data.columns = ['label', 'message']    #here we just change name of original columns and replace these by label and message

# Convert labels to binary: ham -> 0, spam -> 1
data['label'] = data['label'].map({'ham': 0, 'spam': 1})     #here we convert label column into binary 0 or 1 output
print(data.head())    #it is just for printing starting 5 rows

X = data['message']   #X is a full message column data
y = data['label']     #y is a full label column data

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)    #here we separate data for training and testing like 80% and 20%  respectively

vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
# it converts SMS text into numerical features using TF-IDF
# Fit and transform on training data, only transform on test data
X_train_tfidf = vectorizer.fit_transform(X_train)         #fit_transform does both:

    # Learns from the data (fit),
    # Applies the transformation (transform) on the training set to convert it into TF-IDF vectors.
X_test_tfidf = vectorizer.transform(X_test)            # we use only transform because the TfidfVectorizer has already learned the vocabulary and IDF values from X_train during the fitting stage.

nb_model = MultinomialNB()    #here we used naive bays classifier
nb_model.fit(X_train_tfidf, y_train)   #here we train our model by providing input and output like x_train and y_train

nb_predictions = nb_model.predict(X_test_tfidf)   #now we provide input to trained model and making predictions
print("Naive Bayes Accuracy:", accuracy_score(y_test, nb_predictions))    #this is final step for this model and this is the result