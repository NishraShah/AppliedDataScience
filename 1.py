"""

        author：Ming
        date：2019.9.26
        function：IMBD
        edition：10.0

"""
import csv

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import seaborn as sns
from wordcloud import WordCloud

import explode as ex
from pylab import *
import numpy as np
import wordcloud

#table in Chinese , data display
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)








def data_adress():



    two_data_rating = pd.read_csv('two_data_rating.csv', header=0)
    directors_select = two_data_rating.groupby('directors').size()
    active_data = directors_select.index[directors_select >= 2]
    directors_top = two_data_rating.ix[active_data]
    directors_top = directors_top.sort_values(ascending=False)
    directors_top = directors_top.to_frame()
    print(directors_top)

    # direcotes = pd.read_csv('title.crew.csv', header=0)
    # direcotes['imdbId'] = direcotes.tconst.str.extract("(\d{7})", expand=True)
    # direcotes.to_csv('direcotes.csv', header=1)
    # direcotes = pd.read_csv('direcotes.csv', header=0)
    # two_data_rating = two_data_rating.merge(direcotes, on='imdbId')
    # two_data_rating.to_csv('two_data_rating.csv', header=1)


    # _genre_1995=two_data_rating[two_data_rating['year'].isin([1995])]
    # _genre_2017 = two_data_rating[two_data_rating['year'].isin([2016])]


















    # heat_title = pd.read_csv('heat_title.csv', header=0)
    # two_data_rating = two_data_rating.merge(heat_title, on='title')
    # two_data_rating.to_csv('two_data_rating.csv', header=1)
    #
    # title_episode = pd.read_csv('title.episode.csv', header=0)
    # title_episode['imdbId'] = title_episode.tconst.str.extract("(\d{7})", expand=True)
    # title_episode.to_csv('title_episode.csv', header=1)

    #     # title_episode = pd.read_csv('title_episode.csv', header=0)
    #     # two_data_rating = title_episode.merge(two_data_rating, on='imdbId')
    #     #
    #     # print(two_data_rating)
    #     # two_data_rating.to_csv('two_data_rating.csv', header=1)
    #Document_movies_links1 = pd.read_csv('Document_movies_links1.csv', header=0)
    # Document_movies_links = pd.read_csv('Document_movies_links.csv', header=0)
    # Document_movies_links1 = Document_movies_links.merge(title_meanRating, on='title')
    # Document_movies_links1.to_csv('Document_movies_links1.csv', header=1)
    # Document_movies_links1 = Document_movies_links1.sort_values(by=['rating'], ascending=False)


    #two_data_rating = Document_movies_links1.merge(title_rating_IMDB1, on='imdbId')
    #two_data_rating.to_csv('two_data_rating.csv', header=1)

    # title_rating_IMDB['imdbId'] = title_rating_IMDB.tconst.str.extract("(\d{7})", expand=True)
    # title_rating_IMDB.to_csv('title_rating_IMDB1.csv', header = 1)


    # imdb_movieslens = title_meanRating.merge(data_imdb_1000, on='title')
    # print(imdb_movieslens)

    #data_visualisation(_genre_2017)





def data_visualisation(data):

    #word cloud
    genre = data['genres'].str.split('|')
    str2 =','.join(str(i) for  i in genre)
    print(str2)
    wordcloud = WordCloud()
    wordcloud.generate(str2)
    plt.figure()
    plt.max_words = 200
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()





    # # ##Comparison of two rating line graph
    # data = data.sort_values(by=['hit'], ascending=False)
    # data = data[:10]
    # # MOVIELENS RATING
    # ax1 = plt.subplot(121)
    # #ax1.set_xticklabels('', rotation=270)
    # plt.xticks(rotation=270)
    # plt.xlabel('Title')
    # plt.ylabel("Popularity of MovieLens'")
    # ax1.plot(data.title, data.hit, color='r')
    # plt.title("hit")
    # # IMDB AVERAGERATING
    # ax2 = plt.subplot(122)
    # plt.xlabel('Title')
    # plt.ylabel("Popularity of Imdb")
    # #ax2.set_xticklabels('', rotation=270)
    # ax2.plot(data.title, data.numVotes, color='r')
    # plt.title("hit")
    # plt.xticks(rotation=270)
    # plt.delaxes(ax2)
    # plt.subplot(ax2)
    # plt.show()


def main():

    data_adress()



if __name__ ==  '__main__':
    main()