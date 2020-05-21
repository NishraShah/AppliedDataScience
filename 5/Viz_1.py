"""

        
        date：2019.12.10
        function：insight1
        edition：1.0

"""

import csv
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import codecs
import numpy as np
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import sys
import  io
from wordcloud import WordCloud
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
# from vaderSentiment.vaderSentiment import sentiment as vaderSentiment
# table in Chinese , data display
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)


def data_adress():
    # a = pd.read_csv('addressed_data/aboutme.csv', encoding="ISO-8859-1", error_bad_lines=False)
    # file = open('addressed_data/body.txt', 'w', encoding='utf-8')
    #
    # str2 = ','.join(str(i) for i in file)

    aboutme = ' questions learn  clean questions learn  clean  questions learn  clean  questions learn  clean  USA questions USA questions USA questions USA questions USA questions USA questions USA questions  questions learn  clean USA questions learn  clean  questions learn  clean  questions learn  clean project questions learn project questions learn project questions learn project questions learn project data science computer robot language work  process cook project data science computer robot language work  process cookproject data science computer robot language work  process cookproject data science computer robot language work  process cookproject data science computer robot language work  process cook engineering  downvotes on spam/evil posts community questions and answers so nobody gets unnecessary reputation from them  that get permanently deleted downvotes on spam evil posts that get permanently deletedquestions,computer,engineering,Randomly poke old unanswered questions every hour so they get some attention'
    wordcloud = WordCloud(background_color='white',)
    wordcloud.generate(aboutme)
    plt.figure()
    plt.max_words = 200
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()
    # import re
    # from collections import Counter
    # from matplotlib.pyplot import pie, show
    # f = 'aboutme.txt'
    # c = Counter(re.findall(r'(\w{3,})', open(f).read().lower())).most_common(20)
    # pie([i[1] for i in c], labels=[i[0] for i in c])
    # show()
    #
    #
    # troll = pd.read_csv('original_data/posts.csv', encoding="ISO-8859-1", error_bad_lines=False)
    # list = troll['Body']
    # file = open('addressed_data/body.txt',  'w',encoding='utf-8')
    # for i in range(0, len(list)):
    #     file.write(str(list[i]) + "\n")
    # file.close();
    # data = pd.read_csv('addressed_data/Users_accept_ml.csv',encoding="ISO-8859-1",  error_bad_lines=False )
    # data = data
    # #,index_col=0
    # # # data.dropna(axis=0, how='any', inplace=True)
    # data = data.fillna(0)
    # index = data['AcceptedAnswerId']
    # index = index.fillna(0)
    # for i in range(0, len(index) - 1):
    #     index[i] = int(index[i])
    # #
    # #
    # sentid_result = []
    # for i in range(0, len(data) - 1):
    #     sentid_result.append(data['AboutMe'][index[i]])
    #
    # #
    # senti_result = pd.DataFrame(sentid_result, columns=['name'])
    # senti_result.to_csv('addressed_data/aboutme.csv', header=1)
    # troll = pd.read_csv('addressed_data/aboutme.csv', index_col=0 )
    #
    # file = open('aboutme.txt', 'w')
    # for i in range(0, len(troll)):
    #     file.write(str(list[i]) + "\n")
    # file.close();
    # data1 = pd.read_csv('addressed_data/posts_bodysenti.csv',encoding="ISO-8859-1",  error_bad_lines=False ,index_col=0)
    # data1 = pd.read_csv('original_data/posts.csv', encoding="ISO-8859-1", error_bad_lines=False)
    # data2 = data1.join(data)
    # data2.to_csv('addressed_data/posts_bodysenti.csv', header=1)
    # data['sentiment'][39928] = -0.6782
    # data.to_csv('addressed_data/posts_senti.csv', header=1, index =False)
    # data = data.append([{'sentiment': -0.6782}], ignore_index=True)
    # data.to_csv('addressed_data/posts_senti.csv', header=1)
    # 
    # 
    # a = "<p>Here's one thing i noticed. In Elementary Real Analysis, when we say that a sequence converges to a point  we first set an such that for large <span class=$N \in \mathbb{N} $</span>Why don't we set up the convergence of loss functions that way? i. e. We don't have a hyperparameterhyperparameter $\epsilon$</span> to ensure our convergence. </p>v"
    # analyzer = SentimentIntensityAnalyzer()
    # b =analyzer.polarity_scores(str(a))
    # print(b["compound"])
    
    # data = data
    # senti_result = []
    # for i in range(0  , len(data)-1):
    #     analyzer = SentimentIntensityAnalyzer()
    #     senti_result.append(analyzer.polarity_scores(str(data['AboutMe'][i]))["compound"])
    # #
    # #     # print(str(vs))
    # #     # print(str(vs["compound"]))
    # senti_result = pd.DataFrame(senti_result, columns=['sentiment'])
    # senti_result.to_csv('addressed_data/users_senti.csv', header=1)
    # senti_sign_result = []
    # for i in range(0  , len(data)-1):
    #     if(data['sentiment'][i] < 0):
    #         senti_sign_result.append(-1)
    #     if (data['sentiment'][i] > 0):
    #         senti_sign_result.append(1)
    #     if(data['sentiment'][i] == 0):
    #         senti_sign_result.append(0)
    # senti_sign_result = pd.DataFrame(senti_sign_result, columns=['sentiment_sign'])
    #
    # posts_bodysenti = senti_sign_result.join(data)
    # posts_bodysenti.to_csv('addressed_data/user_sentiment.csv', header=1)

    # data = pd.read_csv('original_data/posts.csv',encoding="ISO-8859-1",  error_bad_lines=False )
    # data1 = pd.read_csv('original_data/Users.csv', encoding="ISO-8859-1", error_bad_lines=False)
    # data1.rename(columns={'Id':'PostId'}, inplace = True)
    # #
    # two_data = data.merge(data1, on='PostId')
    # two_data.to_csv('addressed_data/posts_comments.csv', header=1)
    # print(two_data)
    # # data['AnswerCount'].isin(['1'])|data['AnswerCount'].isin(['2'])|data['AnswerCount'].isin(['3'])]
    #
    # # print(data)
    # print(two_data.head())
    # print(two_data.info())
    # Answer50_questions = data.groupby('AnswerCount').size()
    # A = ['A','B','C']
    # #     # B = [1,2,3]
    # print(Answer50_questions)
    # Answer50_questions.plot(kind='pie',
    #                             figsize=(5, 6),
    #                             autopct='%1.f%%', # add in percentages
    #                             startangle=90,     # start angle 90° (Africa)
    #                             shadow=True,       # add shadow
    #                             )
    # plt.title('1')
    # plt.axis('equal') # Sets the pie chart to look like a circle.
    # plt.show()
    # # print(type(data))-
    # data.to_csv('original_data/posts.csv', header=1)

    # data = pd.read_csv('original_data/postss.csv',encoding="ISO-8859-1", error_bad_lines=False )
    # data.to_csv('original_data/posts.csv',encoding="utf-8", header=1)
    # print(data.head())
    # print(data.info())
    # Answer50_questions = data.groupby('AnswerCount').size()
    # active_data = data.index[Answer50_questions >= 5]
    #
    # title50_movies = title50_movies.ix[active_data]
    # print(title50_movies)
    # Answer50_questions = Answer50_questions.sort_values(ascending=False)
    #
    # print(Answer50_questions)




def data_visualisation(data):
    pass




def main():
    data_adress()


if __name__ == '__main__':
    main()
