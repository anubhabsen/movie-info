import urllib
from urllib2 import Request, urlopen
import json
import pandas as pd
from guessit import guessit
import os
import sys

title = []
genre = []
plot = []
run_time = []
rottentomatoes_consensus = []
imdb_ratings = []

def get_info(name):
	response = urlopen(Request('https://www.omdbapi.com?t=' + urllib.quote_plus(name) + '&y&plot=short&tomatoes=true&r=json'))
	data = response.read()
	data1 = json.loads(data)
	if data1['Response'] == "False":
		print "movie doesnt exist"
	else:
		title.append(data1['Title'])
		genre.append(data1['Genre'])
		plot.append(data1['Plot'])
		run_time.append(data1['Runtime'])
		rottentomatoes_consensus.append(data1['tomatoMeter'])
		imdb_ratings.append(data1['imdbRating'])

def main():
    filepath = raw_input("Enter the filepath: ")
    for file in os.listdir(filepath):
        file = guessit(file)['title']
        print file
        get_info(file)
    df = pd.DataFrame({'Title': title, ' Genre': genre, 'Plot': plot, 'Run Time': run_time, 'Tomatometer': rottentomatoes_consensus, 'IMDB Rating': imdb_ratings})
    df.to_csv('movies.csv', index=False)

if __name__ == "__main__":
    main()
