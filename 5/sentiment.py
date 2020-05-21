"""

        author：Ming
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
import matplotlib.dates as mdates
import ggplot
# from vaderSentiment.vaderSentiment import sentiment as vaderSentiment
# table in Chinese , data display
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)


def data_adress():
    data = pd.read_csv('addressed_data/posts_bodysenti.csv', encoding="ISO-8859-1", error_bad_lines=False, index_col=0)





    # data1 = pd.read_csv('original_data/Comments.csv', encoding="ISO-8859-1", error_bad_lines=False, index_col=0)
    # data= data
    # # ggplot((x="CreationDate", y="sentiment_sign", data=data) + geom_point() + geom_line(color='blue') + scale_x_date(
    # #     labels=date_format("%Y-%m-%d"))
    # # xs = [datetime.strptime(d, '%Y/%m/%d').date() for d in l_time]
    # # data['CreationDate'] = pd.to_datetime(['CreationDate'])
    # # data.set_index('CreationDate')
    # # data['sentiment_sign'].plot()
    # #
    # # data_date_str = data.CreationDate[:100]
    # #
    # # data_date = list(map(parser.parse, data_date_str))
    # # plt.plot(data_date, data.sentiment_sign, color='blue', linewidth=1.0, linestyle='-', label='predict')
    # # plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y/%m/%d %H/%M'))
    # #
    # # plt.gca().xaxis.set_major_locator(mdates.MonthLocator())  # 按月显示,按日显示的话，将MonthLocator()改成DayLocator()
    # #
    # # # plt.gcf().autofmt_xdate()  # 自动旋转日期标记
    # #
    # # plt.title('Temperation constraction')
    # #
    # # plt.savefig('temper.png')
    # #
    # # plt.show()



    '''
    semtiment
    '''
    senti_result = []
    for i in range(0  , len(data)):
        analyzer = SentimentIntensityAnalyzer()
        senti_result.append(analyzer.polarity_scores(str(data['Title'][i]))["compound"])

        # print(str(vs))
        # print(str(vs["compound"]))
    senti_result = pd.DataFrame(senti_result, columns=['sentiment'])
    senti_result.to_csv('addressed_data/title_senti.csv', header=1)
    # senti_sign_result = []
    # for i in range(0, len(data) - 1):
    #     if (data['sentiment'][i] <= 0):
    #         senti_sign_result.append(-1)
    #     if (data['sentiment'][i] > 0):
    #         senti_sign_result.append(1)
    #
    # senti_sign_result = pd.DataFrame(senti_sign_result, columns=['sentiment_sign'])

    # posts_bodysenti = data1.join(data)
    # posts_bodysenti.to_csv('addressed_data/comments_senti.csv', header=1 )



    # ##Comparison of two rating line graph


    # MOVIELENS RATING
    # ax1 = plt.subplot(121)
    # #ax1.set_xticklabels('', rotation=270)
    # plt.xticks(rotation=270)
    # plt.xlabel('Title')
    # plt.ylabel("Popularity of MovieLens'")
    # ax1.plot(data.CreationDate, data.sentiment_sign, color='r')
    # plt.title("hit")
    # # IMDB AVERAGERATING
    # ax2 = plt.subplot(122)
    # plt.xlabel('Title')
    # plt.ylabel("Popularity of Imdb")
    # #ax2.set_xticklabels('', rotation=270)
    # ax2.plot(data.CreationDate, data.sentiment_sign, color='r')
    # plt.title("hit")
    # plt.xticks(rotation=270)
    # plt.delaxes(ax2)
    # plt.subplot(ax2)
    # plt.show()


def data_visualisation(data):
    pass


def main():
    data_adress()


if __name__ == '__main__':
    main()