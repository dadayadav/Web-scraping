# import all required library
import random
import urllib.request
from urllib import request
# web scraping 
from bs4 import BeautifulSoup
import urllib.request as urllib2
from urllib.request import urlopen
youtube = "https://www.youtube.com/watch?v=LKNHVDPKy7g&list=PLafSq5UblCNWC3HKFanOcnxJ8KcQ-5wxW"
page = urlopen(youtube)
bollywood = BeautifulSoup(page,"lxml")
print(bollywood.prettify())

title_movie = []
for title in bollywood.findAll('div', class_ = "playlist-video-description"):
    name_ = title.findAll('h4' ,class_="yt-ui-ellipsis yt-ui-ellipsis-2")
    for name in name_:
        title_movie.append(name.text)

# Some News article from hindi newspaper (Dainik Bhaskar)
url_dainik ="https://www.bhaskar.com/"
dainik_page = urlopen(url_dainik)
dainik = BeautifulSoup(dainik_page,"lxml")
print(dainik.prettify())
news = dainik.findAll('li')
#Indian national News from newspaper as first topic
ultimatenews = "https://www.bhaskar.com/indian-national-news-in-hindi/"
bv = urlopen(ultimatenews)
bv = BeautifulSoup(bv,"lxml")
print(bv.prettify())
# Scrap First Page of Newspaper
news_title = []
news_site = []
for div in bv.findAll('li'):
    for i in div.findAll('div', class_="list-box"):
        for para in div.findAll('h3'):
            for link in para.findAll('a'):
                news_site.append(link.get('href'))
                news_title.append(link.text)
# Description of above news
news_l = []
for x in news_site:
    sourcecode = urlopen(x)
    soup = BeautifulSoup(sourcecode, "lxml")
    p = soup.findAll('p')
    for i in p:
        news_l.append(i.text)
# Now we extract the different number of pages
dainik_title = []
# we make function which take input as number of pages 
def function_news(max_pages):
    page = 1
    while page <= max_pages:
        if page == 1:
            url = ultimatenews
        else:
            url = ultimatenews + str(page)
        sourcecode = urlopen(url)
        soup = BeautifulSoup(sourcecode, "lxml")
        for div in soup.findAll('li'):
            for i in div.findAll('div', class_="list-box"):
                for para in div.findAll('h3'):
                    for link in para.findAll('a'):
                        dainik_title.append(link.text)   
        page += 1
function_news(12)
print(dainik_title)
# News article on Google in newspaper as second topic 
url = "https://www.bhaskar.com/"
dainik = urlopen(url)
soup = BeautifulSoup(dainik, "lxml")
for goog in soup.findAll('ul', class_ = "footerlist"):
    for new in goog.findAll('li'):
        for a in new.findAll('a',{'title': "गूगल हिंदी न्यूज़"}):
            href = a.get('href')
print(href)
# Or ultenative way is just go to webite and find the link
#link = "https://www.bhaskar.com/topics/google/

# we make a function as above to scroll all the pages
google_news = []
def googl_news(max_pages):
    page = 1
    while page <= max_pages:
        url = href + "news/" + str(page) + "/"
        sourcecode = urlopen(url)
        soup = BeautifulSoup(sourcecode, "lxml")
        for ul in soup.findAll('ul', class_ = "ne-vi-ph-list"):
            print(1)                                                 # just for checking
            for li in ul.findAll('li', class_="box"):
                for para in li.findAll('h2'):
                    for link in para.findAll('a'):
                        google_news.append(link.text)   
        page += 1
googl_news(64)
print(google_news)            
# Make a DataFrame of two category of news
news_from_dainik = pd.DataFrame(dainik_title, columns = ["India_News"])
print(news_from_dainik.head(10))
news_from_dainik_goog = pd.DataFrame(google_news, columns = ["Google_news"])
print(news_from_dainik_goog.head(10))
dainik_bhaskar_news = pd.concat([news_from_dainik,news_from_dainik_goog], axis=1)
print(dainik_bhaskar_news.head(50))
# convert into xlsx
writer = pd.ExcelWriter('news.xlsx')
dainik_bhaskar_news.to_excel(writer,'Sheet1')
writer.save()

# Movie title and some detial from IMDB
imdb = "https://www.imdb.com/india/top-rated-indian-movies/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=8a7876cd-2844-4017-846a-2c0876945b7b&pf_rd_r=J22VX3EAQ895AXN10EBY&pf_rd_s=right-5&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_india_tr_rhs_1"
web = urlopen(imdb)
web = BeautifulSoup(web, "lxml")
movie_name = []
movie_site = []
release_year = []
imdb_rating = []
for table in web.findAll('table', class_ = 'chart full-width'):
    for body in table.findAll('tbody', class_ = "lister-list"):
        for row in body.findAll('tr'):
            for column in row.findAll('td', class_ = "titleColumn"):
                for link in column.findAll('a'):
                    movie_name.append(link.text)
                    b = "https://www.imdb.com"+link.get('href')
                    movie_site.append(b)
                for year in column.findAll('span', class_ = 'secondaryInfo'):
                    release_year.append(year.text)
            for imdB in row.findAll('td', class_ = "ratingColumn imdbRating"):
                imdb_rating.append(imdB.text)
#Total_number of movies list
print(len(movie_name))
for i in movie_site:
    print(i)
movie_time = []
release_date = []
for i in movie_site:
    sourcecode = urlopen(i)
    soup = BeautifulSoup(sourcecode, "lxml")
    for div in soup.findAll('div', class_ = "subtext"):
        for time in div.findAll('time'):
            movie_time.append(time.text)
        for date in div.findAll('a', {'title' : 'See more release dates'}):
            release_date.append(date.text)
rating_count = []
for i in movie_site:
    sourcecode = urlopen(i)
    soup = BeautifulSoup(sourcecode, "lxml")
    for div1 in soup.findAll('div', class_ = "imdbRating"):
        for lin in div1.findAll('span', class_ = "small"):
            rating_count.append(lin.text)
movie_genre = []
for i in movie_site:
    sourcecode = urlopen(i)
    soup = BeautifulSoup(sourcecode, "lxml")
    for div in soup.findAll('div', class_ = "subtext"): 
        for genr in div.findAll('a'):
            movie_genre.append(genr.text)
director_name = []
for i in movie_site:
    sourcecode = urlopen(i)
    soup = BeautifulSoup(sourcecode, "lxml")   
    for div2 in soup.findAll('div', class_ = "credit_summary_item"):
        for dirc in div2.findAll('span', {'itemprop' : 'director'}):
            director_name.append(dirc.text)
# Convert into CSV
import pandas as pd
movies_csv = pd.DataFrame(movie_name, columns = ['Movies_title'])
movies_csv['Release Date'] = release_date
movies_csv['Release Year'] = release_year
movies_csv['IMDB Rating'] = imdb_rating
movies_csv['Time Length'] = movie_time
movies_csv['Rating Count'] = rating_count
movies_csv['Site'] = movie_site
# convert into xlsx 
writer = pd.ExcelWriter('movies.xlsx')
movies_csv.to_excel(writer,'Sheet1')
writer.save()
print(movies_csv.head(20))
# or
movies_csv.to_csv("movieid.csv", sep='\t')                                                       