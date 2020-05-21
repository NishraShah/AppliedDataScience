import csv


# from descartes.patch import PolygonPatch
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
# import seaborn as sns
# import explode as ex
from pandas import DataFrame
from pylab import *
import numpy as np
import pandas as pd
# import geopandas as gpd
# from shapely import geos
# from shapely.geometry import Point
# import fiona
import matplotlib.pyplot as plt
# from fiona.crs import from_epsg,from_string
import datetime

#table in Chinese , data display
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)


def data_adress():
    texi_sample = pd.read_csv('addressed_data/posts_bodysenti.csv', index_col=0, parse_dates=True)
    texi_sample = texi_sample.reset_index()

    time_start = texi_sample['CreationDate']
    time_end = texi_sample['ClosedDate']
    file = open('interval/time_start.txt', 'w')
    for i in range(0, len(time_start)):
        file.write(str(time_start[i]) + "\n")

    file.close();

    file = open('interval/time_end.txt', 'w')
    for i in range(0, len(time_end)):
        file.write(str(time_end[i]) + "\n")

    file.close();
    # #







def main():
    data_adress()


if __name__ ==  '__main__':

    main()