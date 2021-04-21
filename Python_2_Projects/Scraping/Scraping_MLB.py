import pandas as pd
import numpy as np
import requests
import time
from bs4 import BeautifulSoup

# NOTE THAT THE WASHINGTON NATIONALS ARE NOT INCLUDED BECAUSE THEIR PAGE IS BROKEN IN THE CURRENT BUILD of ESPN.COM(4/20/21)


column_names = ["Team", "ABV", "Schedule"]
abbreviations = pd.read_csv("schedule_urls.csv", names=column_names)
team = abbreviations.ABV.to_list()
teamb = sorted(team, reverse=True)
teamp = sorted(team, reverse=True)
team2=sorted(team)
team_df = pd.DataFrame(team)
# Goal is to scrape all teams in the MLB for pitching and batting statitics and find the leader in the categories of average and strikeouts(K's)
def Batting():
    start_time = time.time()
    while len(teamb) > 0:
        #scrape data and create readable data
        url = f'https://www.espn.com/mlb/team/stats/_/name/{teamb[-1]}/season/2021/seasontype/2'
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        # Creates elements from html that will be the base for the Data Frame
        team_name_object = soup.find('span', attrs= {'class': 'flex flex-wrap'})
        table = soup.find('div', attrs = {'class':'ResponsiveTable ResponsiveTable--fixed-left mt5 remove_capitalize'})
        table2 = soup.find('div', attrs = {'class':'Table__Scroller'})
        #ex_table = soup.find_all('table')[3]
        
        #Creates Pandas dataframes
        #ex_df = pd.read_html(str(ex_table))[0]
        df= pd.read_html(str(table))[0]
        df2= pd.read_html(str(table2))[0]
        
        # Combines tables to create readable data
        resultB = df.join(df2)
        #result2B = df.join(ex_df)
        
        #print functions
        #print(f'Player Batting Stats - All Splits\n{resultB}\n')
        #print(f'\n\n\nExpanded Batting Stats - All Splits\n{result2B}')
        
        #Sends data to 2 different CSV's for better munipulation(not using extended data at this time)
        resultB.to_csv(f'Batting_Stats{teamb[-1]}.csv')
        #result2B.to_csv(f'ExpandedPlayer_Batting_{teamb[0]}.csv')
        index = resultB.index
        resultB = resultB.drop(resultB.index[len(index) - 1])
        resultB = resultB.loc[(resultB["AB"] >=35)]
        leader_row = resultB["AVG"].argmax()
        row = resultB.loc[[leader_row]]
        try:
            leader_frame = leader_frame.append(row,ignore_index=True)
            
        except UnboundLocalError:
            leader_frame = pd.DataFrame
            leader_frame = row.copy()
                  
        del teamb[-1]
        
        if len(teamb) < 1:
            break
    leader_frame2 = leader_frame.assign(Team = team2)
    leader_frame2 = leader_frame2.sort_values(by="AVG",ascending=False)
    leader_frame2.to_csv("Batting_League_Leaders.csv")
    clock = "{:.3f}".format(time.time() - start_time)
    print("Inquiry took:", clock ,"seconds.\n")
    #leader has a minimum at bat count of 35 at bats
    outputB = f'League Leader for Average:\n{leader_frame2[leader_frame2.AVG == leader_frame2.AVG.max()]}'
    return outputB
    
    
    
    
    
def Pitching():
    
    start_time = time.time()
    while len(teamp) > 0:
        
        #scrape data and create readable data
        url = f'https://www.espn.com/mlb/team/stats/_/type/pitching/name/{teamp[-1]}/season/2021/seasontype/2'
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        # Creates elements from html that will be the base for the Data Frame
        table = soup.find('div', attrs = {'class':'ResponsiveTable ResponsiveTable--fixed-left mt5 remove_capitalize'})
        table2 = soup.find('div', attrs = {'class':'Table__Scroller'})
        #ex_table = soup.find_all('table')[3]
        
        #Creates Pandas dataframes 
        #ex_df = pd.read_html(str(ex_table))[0]
        df= pd.read_html(str(table))[0]
        df2= pd.read_html(str(table2))[0]
        
        # Combines tables to create readable data
        resultP = df.join(df2)
        #result2P = df.join(ex_df) 
        
        #print functions
        #print(f'\n\n\nPlayer Pitching Stats - All Splits\n{resultP}')
        #print(f'\n\n\nBatting Against Stats - All Splits\n{result2P}')
        
        #Sends data to 2 different CSV's for better munipulation(not using expanded data at this time)
        resultP.to_csv(f'Pitching_Stats{teamp[-1]}.csv')
        #result2P.to_csv(f'Batting_Against_Pitching_{teamp}.csv')
        
        #creates a dataframe with the strikeout leader from each team
        index = resultP.index
        resultP = resultP.drop(resultP.index[len(index) - 1])
        leader_row = resultP["K"].argmax()
        row = resultP.loc[[leader_row]]
        try:
            leader_frame = leader_frame.append(row,ignore_index=True)
            
        except UnboundLocalError:
            leader_frame = pd.DataFrame
            leader_frame = row.copy()
                  
        del teamp[-1]
        
        if len(team) < 1:
            break
    leader_frame2 = leader_frame.assign(Team = team2)
    leader_frame2 = leader_frame2.sort_values(by="K",ascending=False)
    leader_frame2.to_csv("Pitching_League_Leaders.csv")
    clock = "{:.3f}".format(time.time() - start_time)
    #set this up because there has to be a way to make this more efficient, not sure how.
    print("Inquiry took:", clock ,"seconds.\n")
    outputP= f'League Leader for Stikeouts:\n{leader_frame2[leader_frame2.K == leader_frame2.K.max()]}'   
    return outputP

def main():
    print("Lets take a look at some statistics from around the MLB.")
    print("Each teams data will be printed in a csv in the folder this program is stored!(Please note that this program will take a minute to spit out your results!)")
    bat = input("Would you also like to know who the league leader in Average is while we are at it?(Y or N)")
    bat = bat.lower()
    if bat == 'y':
        print("Fetching Data....\n")
        answer = Batting()
        print(answer)
        print("\nAll your data has been uploaded to a CSV for each team, now lets move on to pitching data!\n")
    else:
        print("Fetching Data....\n")        
        Batting()
        print("\nAll your data has been uploaded to a CSV for each team, now lets move on to pitching data!\n")
    pitch = input("Would you also like to know who the league leader in strikeouts is while we are at it?(Y or N)")
    pitch = pitch.lower()
    if pitch == 'y':
        print("Fetching Data....\n")
        answer = Pitching()
        print(answer)
        print("\nAll your data has been uploaded to a CSV for each team! Thanks for checking out my program!")
    else:
        print("Fetching Data....\n")          
        Pitching()
        print("\nAll your data has been uploaded to a CSV for each team! Thanks for checking out my program!")
main()