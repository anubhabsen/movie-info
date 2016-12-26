Movie/ TV Series Data Scraper
=============================

A python script that looks up all movies/ TV shows in a folder, parses the title from the file name and looks it up on IMDb and gets the  genre, runtime, plot and IMDB and RottenTomatoes ratings of the movie and stores it as a csv file.

####Installation
    git clone https://github.com/anubhabsen/movie-info
    cd movie-info
    bash setup.sh
    
Running the shell script will install the necessary python packages and run the script for the first time. After setup has been executed once, just use
     
     python getInfo.py

to execute.

Note: The path to the folder MUST BE absolute (relative path won't work).
