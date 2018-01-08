#This program started to determine average rating of all films in which Adam Sandler started as actor using IMDB website.
# Now it can check more actors. Changes can be found at the bottom of the page
from bs4 import BeautifulSoup #Importing needed libraries and utilities:
import urllib.request
import re

#mother_url = "http://www.imdb.com/name/nm0424848/?ref_=tt_cl_t1" #Dakota Jhonson
mother_url = "http://www.imdb.com/name/nm0001191/?ref_=nv_sr_1" #Adam Sandler
 #desired url - homepage of Adam Sandler in IMDB
# Defining functions to get url an later convert it to BeautifulSoup object to scrap information needed
def get_url(url):
    site = urllib.request.urlopen(url)
    read_site = site.read()
    return read_site

def soup_it(http):
    soup = BeautifulSoup(http,"html5lib")
    return soup

def url_to_soup(adress): #Previous funtcions in one, used to get right to the sweetspot
    url = get_url(adress)
    soup_rdy = soup_it(url)
    return soup_rdy


def get_links(mother_site): #This function returns list of links to movies sites we want to take rating from
    soup = url_to_soup(mother_site)
    titles = soup.find("div",class_="filmo-category-section")
    titles_str = str(titles)
    #links_matches = re.finditer('<b><a href="(.+)"', titles_str)
    links_matches = re.finditer('<b><a href="(.+)">(.+)</a>', titles_str)
    links_list = []
    titles_list = []
    missing_part = "http://www.imdb.com"
    for i in links_matches: #Loop to create a list of quasi-final links to get rating from
        I = i.group(1)
        II = i.group(2)
        links_list.append(missing_part+I)
        titles_list.append(II)
    return links_list,titles_list
# Function to determine rating of chosen movie / To be ran on movie links to get their rating
def get_rating(movie_soup):
    rating_block = movie_soup.find_all("div", class_="imdbRating")
    string = str(rating_block)
    rating = re.search("<span itemprop=\"ratingValue\">(\d[\.,]\d)<\/span>",string)
    rating_compl = rating.group(1)
    return rating_compl

def main():
    links_list,titles_list = get_links(mother_url)
    count = 1
    sum_ratings = 0.0
    final_count = 0
    for link in links_list:
        try:
            movie = url_to_soup(link)
            rating = get_rating(movie)
            print(count,"Title: ",titles_list[count]," rating is: ",rating)
            count += 1
            final_count += 1
            sum_ratings += float(rating)
        except:
            print("Can't get rating for element",count,"(No Rating): ",link)
            count += 1

    print("Average rating value of movies in which Adam Sandler's played is equal to: ",sum_ratings/final_count, "Final count: ",final_count)
main()

#Version 1.1 changes:
# Features:
# 1. Added movie titles in place of "Movie 1,2,3 etc."
# 2. Version checked to work on other actors as well !
#
# Bugfixes (?):
# 1. Deleted unneeded loop in get_links()
# 2. Fixed regex in order to get rid of [:-2] element while creating links_list  [33]
# 3. Removed unneeded loop in main converting spaces to lowerspace in linkslist [46]
# 4. Counting elements properly now starting from Movie no.1
# 5. Added final_count to last print to check if count is valid with IMDB (actor credtis no.)