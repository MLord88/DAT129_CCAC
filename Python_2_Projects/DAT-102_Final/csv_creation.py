import pandas as pd
import numpy as np
import requests

import sqlite3
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from bs4 import BeautifulSoup

def csv_creation():
    years = {'Years':[2019,2018,2017,2016,2015,2014,2013,2012,2011,2010]}
    pd.DataFrame(years).to_csv('years.csv', index=False)
def main():
    csv_creation()
    
main()