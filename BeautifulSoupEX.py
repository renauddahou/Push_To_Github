#source code Keith Galli (youtube)
import requests
import bs4 
from bs4 import BeautifulSoup #import bs4 and BeatufilSoup to scrape web data
r = requests.get('https://en.wikipedia.org/wiki/Toy_Story_3') #pass the url into 'requests.get()'
soup = BeautifulSoup(r.content, features="lxml") #remember to add 'features="lxml"' incase
contents = soup.prettify() #'.prettify()' cleans up the contents/ make it readable
#print(contents)
info_box = soup.find(class_='infobox vevent') #'.find()' scrapes page to find what you wish
info_rows = info_box.find_all("tr") #'.find_all()' finds all instances of what you pass into parameters
#for row in info_rows:
#    print(row.prettify())
def get_content_value(row_data):
    if row_data.find("li"):
        return [li.get_text(" ", strip=True).replace("\xa0", " ") for li in row_data.find_all("li")]
    else:
        return row_data.get_text(" ", strip=True).replace("\xa0", " ")
movie_info = {}
for index, row in enumerate(info_rows):
    if index == 0:
        movie_info['title'] = row.find("th").get_text(" ", strip=True)
    elif index == 1:
        continue
    else:
        content_key = row.find("th").get_text(" ", strip=True)
        content_value = get_content_value(row.find("td"))
        movie_info[content_key] = content_value
print(movie_info)