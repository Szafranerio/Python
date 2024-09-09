from bs4 import BeautifulSoup
import requests

#with open('./data/Day045/website.html') as file:
#    content = file.read()
#
#soup = BeautifulSoup(content, 'html.parser')
#
##Simply chang the a with what you want to find
#all_anchors = soup.find_all(name='a')
#all_anchors
#
#for tag in all_anchors:
#    print(tag.get('href'))
#    
#heading = soup.find(name='h1', id='name')
#heading

content = requests.get('https://appbrewery.github.io/news.ycombinator.com/')
yc_webpage = content.text

yc = BeautifulSoup(yc_webpage, 'html.parser')
articles = yc.find_all(name = 'a', class_='storylink')
#article_tag = articles.getText()
#print(article_tag)
#
#article_link = yc.find('a', class_='storylink')
#print(article_link)
#
#article_upvote = yc.find(name='span', class_='score')
#article_upvote = article_upvote.getText()
#print(article_upvote)
#

article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get('href')
    article_links.append(link)

    
    
article_texts = [text.getText() for text in yc.find_all(name='a', class_='storylink')]
article_links = [link.get('href') for link in yc.find_all('a')]    
article_upvotes = [int(score.getText().split()[0]) for score in yc.find_all(name='span', class_='score')]

print(article_texts)
print(article_links)
print(article_upvotes)

highest = sorted(article_upvotes, reverse=True)
print(highest)
article_upvotes_index = article_upvotes.index(1312)
print(article_upvotes_index)

text = article_texts[27]
print(text)

link = article_links[27]
print(link)

#Top Movies
movies = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
movies = movies.text


soup = BeautifulSoup(movies, 'html.parser')
title = soup.find_all(name='h3', class_='title')


titles = [title.getText() for title in soup.find_all(name='h3', class_='title')]
print(titles)

titles.reverse()
print(titles)

with open('movie_list.txt', 'w') as movie_list:
    for movie in titles:
        movie_list.write(f"{movie}\n")

import random 
print(random.choice(titles))