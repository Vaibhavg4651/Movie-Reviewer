from bs4 import BeautifulSoup
import requests
import pandas as pd
import json
import os
from PyMovieDb import IMDB

# Setting up session
s = requests.session()  
imdb = IMDB()
# List contaiting all the films for which data has to be scraped from IMDB
films = []

# Lists contaiting web scraped data
names = []
ratings = []
genres = []

# Define path where your films are present 
# For eg: "/Users/utkarsh/Desktop/films"
path = input("Enter the path where your films are: ")

# Films with extensions
filmswe = os.listdir(path)

for film in filmswe:
    # Append into my films list (without extensions)
    films.append(os.path.splitext(film)[0])
    # print(os.path.splitext(film)[0])

for line in films:
    # x = line.split(", ")
    title = line.lower()
    # release = x[1]
    # print(release)
    try: 
    # query = "+".join(title.split()) 
       
    # release = x[1]
        query = "+".join(title.split()) 
    # print(release)
        print(query)
        response = imdb.get_by_name(query)
        print(response)
        data= json.loads(response)

        #getting contect from IMDB Website

        # print(response.status_code) 
        #searching all films containers found
        name = data['name']
        genre = data['genre']
        rating = data['rating']

                #appending name, rating and genre to individual lists
        names.append(name)
        ratings.append(rating)
        genres.append(genre)
                
        print(name, rating, genre)

    except Exception:
        print("Try again with valid combination of tile and release year")

#storing in pandas dataframe
df = pd.DataFrame({'Film Name':names,'Rating':ratings,'Genre':genres}) 

#making csv using pandas
df.to_csv('film_ratings.csv', index=False, encoding='utf-8')