import urllib
from urllib2 import Request, urlopen
import json

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

name = raw_input("Enter the movie/show name: ")
get_info(name)

print title
print genre
print plot
print run_time
print rottentomatoes_consensus
print imdb_ratings