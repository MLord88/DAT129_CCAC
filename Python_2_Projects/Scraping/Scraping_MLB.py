import pandas as pd
import re
import requests
from bs4 import BeautifulSoup

# Goal is to scrape pirates stats and form them into my own table for the current year
def Batting():
    #scrape data and create readable data
    url = 'https://www.espn.com/mlb/team/stats/_/name/pit/season/2021/seasontype/2'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    # Creates elements from html that will be the base for the Data Frame
    table = soup.find('div', attrs = {'class':'ResponsiveTable ResponsiveTable--fixed-left mt5 remove_capitalize'})
    table2 = soup.find('div', attrs = {'class':'Table__Scroller'})
    ex_table = soup.find_all('table')[3]
    
    #Creates Pandas dataframes 
    ex_df = pd.read_html(str(ex_table))[0]
    df= pd.read_html(str(table))[0]
    df2= pd.read_html(str(table2))[0]
    
    # Combines tables to create readable data
    result = df.join(df2)
    result2 = df.join(ex_df)
    
    #print functions
    print(f'Player Batting Stats - All Splits\n{result}')
    print(f'\n\n\nExpanded Batting Stats - All Splits\n{result2}')
    
    #Sends data to 2 different CSV's for better munipulation
    result.to_csv('Player_Batting.csv')
    result2.to_csv('ExpandedPlayer_Batting.csv')

def Pitching():
    #scrape data and create readable data
    url = 'https://www.espn.com/mlb/team/stats/_/type/pitching/name/pit/season/2021/seasontype/2'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    # Creates elements from html that will be the base for the Data Frame
    table = soup.find('div', attrs = {'class':'ResponsiveTable ResponsiveTable--fixed-left mt5 remove_capitalize'})
    table2 = soup.find('div', attrs = {'class':'Table__Scroller'})
    ex_table = soup.find_all('table')[3]
    
    #Creates Pandas dataframes 
    ex_df = pd.read_html(str(ex_table))[0]
    df= pd.read_html(str(table))[0]
    df2= pd.read_html(str(table2))[0]
    
    # Combines tables to create readable data
    result = df.join(df2)
    result2 = df.join(ex_df)
    print(f'\n\n\nPlayer Pitching Stats - All Splits\n{result}')
    print(f'\n\n\nBatting Against Stats - All Splits\n{result2}')
    
    #Sends data to 2 different CSV's for better munipulation
    result.to_csv('Player_Pitching.csv')
    result2.to_csv('Batting_Against_Pitching.csv')    

def main():
    Batting()
    Pitching()


main()


