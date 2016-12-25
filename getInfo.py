import urllib
from urllib2 import Request, urlopen
import json
import pandas as pd
from guessit import guessit
import os
import sys
import requests
from lxml import html

title = []
genre = []
plot = []
run_time = []
rottentomatoes_consensus = []
imdb_ratings = []

def get_imdb_id(name):
    query = urllib.quote_plus(name)
    url = "http://www.imdb.com/find?ref_=nv_sr_fn&q="+query+"&s=all"
    page = requests.get(url)
    DOM_tree = html.fromstring(page.content)
    if "No results found for" in (DOM_tree.xpath('//h1[@class="findHeader"]/text()')[0]):
        imdb_id = "Notfound"
    else:
        imdb_id = (DOM_tree.xpath('//td[@class="result_text"]//a')[0].get('href'))
        imdb_id = imdb_id.replace('/title/','')
        imdb_id = imdb_id.replace('/?ref_=fn_al_tt_1','')
    return (imdb_id)

def get_info(name):
	response = urlopen(Request('https://www.omdbapi.com?i=' + urllib.quote_plus(name) + '&y&plot=short&tomatoes=true&r=json'))
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
        print file
        if(guessit(file).has_key('title')):
            file = guessit(file)['title']
            print "Extracted title: " + file
            get_info(get_imdb_id(file))
        else:
            print "Video name not detected from filename: " + file
    df = pd.DataFrame({'Title': title, ' Genre': genre, 'Plot': plot, 'Run Time': run_time, 'Tomatometer': rottentomatoes_consensus, 'IMDB Rating': imdb_ratings})
    df.to_csv('movies.csv', index=False, encoding='utf-8')

if __name__ == "__main__":
    main()
