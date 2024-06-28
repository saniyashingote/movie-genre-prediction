# -*- coding: utf-8 -*-
"""Movie Genre Prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1v03Ica5L_YIfS3vIQKuilvjnJoGxAko0

**Installing required libraries**
"""

!pip install spacy
!python -m spacy download en_core_web_sm

import pandas as pd
import numpy as np
import spacy
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

"""**Load the dataset**"""

df = pd.read_csv('/content/wiki_movie_plots_deduped.csv')

print(df.head())

df['Genre'] = df['Genre'].apply(lambda x: x.split(',')[0] if pd.notnull(x) else 'Unknown')

df = df[df['Genre'] != 'Unknown']

nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    return " ".join(tokens)

df['processed_plot'] = df['Plot'].apply(preprocess_text)

vectorizer = TfidfVectorizer(max_features=1000)
X = vectorizer.fit_transform(df['processed_plot']).toarray()

from sklearn.naive_bayes import MultinomialNB

model = MultinomialNB()
model.fit(X_train, y_train)

df_sample = df.sample(frac=0.1, random_state=42)
X = vectorizer.fit_transform(df_sample['processed_plot']).toarray()
y = df_sample['Genre']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=200, solver='saga')
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
print(classification_report(y_test, y_pred))

def predict_genre(plot):
    processed_plot = preprocess_text(plot)
    vectorized_plot = vectorizer.transform([processed_plot]).toarray()
    return model.predict(vectorized_plot)[0]

new_plot = "A young boy discovers he has magical powers and attends a school for wizards."
predicted_genre = predict_genre(new_plot)
print(f"Predicted Genre: {predicted_genre}")
