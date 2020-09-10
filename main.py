#!/usr/bin/env python
# coding: utf-8

# In[16]:


import requests
import bs4

def find_movie(min_rating = 6, released_year = 2015, num_of_page = 10):
    movie_list = []

    for page_number in range(1,num_of_page+1):
        print(f'Scanning Page {page_number} of {num_of_page}...')
        res = requests.get(f'https://yts.mx/browse-movies?page={page_number}')
        soup = bs4.BeautifulSoup(res.text,'lxml')
        movies = soup.select('.browse-movie-wrap.col-xs-10.col-sm-4.col-md-5.col-lg-4')

        in_rating = 7
        in_year = 2017

        for movie in movies:
            movie_name_contents = movie.select('.browse-movie-bottom')[0].select('a')[0].contents

            # check the movie is rated or not
            if(movie.select('.rating') == []):
                continue

            rating = float(movie.select('.rating')[0].contents[0].split(' ')[0])
            year = int(movie.select('.browse-movie-year')[0].contents[0])
            if rating >= min_rating and year == released_year:

                # some movie include [CN] or [JA] but other don't
                # eg. [<span style="color: #ACD7DE; font-size: 75%;">[JA]</span>,' Gamera 3: Revenge of Iris'] or
                # [' Gamera 3: Revenge of Iris']
                # check the length to get the name of movie 

                if len(movie_name_contents) < 2:
                    movie_list.append((movie_name_contents[0].strip(),rating,year))

                else:
                    movie_list.append((movie_name_contents[1].strip(),rating,year))
                    
    return movie_list


# In[ ]:


print('Welcome to YIFY Movie Scrapping\n')
rating = float(input('Enter the minimum rating: '))
year = int(input('Enter the released year: '))
page = int(input('How many pages you want to search?(max = 1013): '))
print('Finding...')

movies = find_movie(rating,year,page)

print(f'-----\n{len(movies)} Results.\n')
for movie in movies:
    print(movie)


# In[ ]:




