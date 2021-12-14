import pandas as pd # https://pandas.pydata.org/docs/
import requests # https://docs.python-requests.org/en/latest/
import json # https://docs.python.org/3.9/library/json.html
import folium # http://python-visualization.github.io/folium/
import os # https://docs.python.org/3.9/library/os.html

os.chdir("C:/Users/kgilb/PycharmProjects/python-practice/python-practice/python-virtual-environments/wimlds/")

data = pd.read_csv("data/Water_Main_Breaks.csv")
data.head()

# run with command: jupyter notebook