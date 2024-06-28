# Movie Genre Prediction

This project predicts the genre of a movie based on its plot summary using natural language processing (NLP) techniques. 
It uses the IMDb dataset, processes the text data, and applies machine learning algorithms to classify the genre.

## Project Description

The project involves the following steps:
1. **Data Collection**: Load the dataset containing movie plot summaries and genres.
2. **Data Preprocessing**: Clean and preprocess the text data using NLP techniques.
3. **Feature Extraction**: Convert the plot summaries into numerical features using TF-IDF.
4. **Model Training**: Train a machine learning model on the training data.
5. **Model Evaluation**: Evaluate the model's performance on the test data.
6. **Prediction**: Use the trained model to predict the genre of new movie plot summaries.

## Dataset
The dataset is from [Kaggle](https://www.kaggle.com/datasets/jrobischon/wikipedia-movie-plots)
The dataset contains descriptions of 34,886 movies from around the world with the following columns:
- `Release Year`: Year in which the movie was released
- `Title`: Movie title
- `Origin/Ethnicity`: Origin of the movie (e.g., American, Bollywood, Tamil, etc.)
- `Director`: Director(s)
- `Plot`: Long form description of the movie plot
- `Genre`: Movie Genre(s)
- `Wiki Page`: URL of the Wikipedia page from which the plot description was scraped

## Installation

To run the project, you need to install the following libraries:

```bash
pip install numpy pandas scikit-learn nltk spacy
python -m spacy download en_core_web_sm
