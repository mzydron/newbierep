import urllib
from urllib import request
#This is simple client which conects to server and gets info from given site:

#Define adress which querry will be given


def get_url(url):

    page = urllib.request.urlopen(url)
    output = page.read()
    return output



if __name__ == '__main__':
    url = "http://127.0.0.1:5000/AI_turn"
    print(get_url(url))