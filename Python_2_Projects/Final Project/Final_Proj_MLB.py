import pandas as pd
import numpy as np
import requests
import time
import sqlite3
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from bs4 import BeautifulSoup

column_names = ["Team", "ABV", "Schedule"]
abbreviations = pd.read_csv("schedule_urls.csv", names=column_names)
team = abbreviations.ABV.to_list()
teamb = sorted(team, reverse=True)
teamp = sorted(team, reverse=True)
team2=sorted(team)
graph_List = sorted(team, reverse=True)
team_df = pd.DataFrame(team)
# Goal is to scrape all teams in the MLB for pitching and batting statitics and find the leader in the categories of average and strikeouts(K's)
def Batting(): # Creates database table for every hitter in the major league with up to date statistics for 2021 from espn.com
    start_time = time.time()
    aggrigate_teams = pd.DataFrame()
    while len(teamb) > 0:
        #scrape data and create readable data
        url = f'https://www.espn.com/mlb/team/stats/_/name/{teamb[-1]}/season/2021/seasontype/2'
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        # Creates elements from html that will be the base for the Data Frame
        team_name_object = soup.find('span', attrs= {'class': 'flex flex-wrap'})
        table = soup.find('div', attrs = {'class':'ResponsiveTable ResponsiveTable--fixed-left mt5 remove_capitalize'})
        table2 = soup.find('div', attrs = {'class':'Table__Scroller'})
        
        #Creates Pandas dataframes
        df= pd.read_html(str(table))[0]
        df2= pd.read_html(str(table2))[0]
        
        # Combines tables to create readable data
        resultB = df.join(df2)
        index = resultB.index
        resultB = resultB.drop(resultB.index[len(index) - 1])
        resultB = resultB.assign(Team = teamb[-1])
        aggrigate_teams = aggrigate_teams.append(resultB)
         
        del teamb[-1]
        
        if len(teamb) < 1:
            break
    #Sends data to database 
    con = sqlite3.connect("MLB_Stats.sqlite") # change to 'sqlite:///your_filename.db'
    cur = con.cursor()    
    aggrigate_teams.to_sql("Batting_Stats", con, if_exists='replace', index=False)
    con.commit()
    con.close()
    #ends timer for inquary
    clock = "{:.3f}".format(time.time() - start_time)
    print("Inquiry took:", clock ,"seconds.\n")
    return aggrigate_teams
    
    
    
def Pitching():
    
    start_time = time.time()
    aggrigate_teams = pd.DataFrame()
    while len(teamp) > 0:
        
        #scrape data and create readable data
        url = f'https://www.espn.com/mlb/team/stats/_/type/pitching/name/{teamp[-1]}/season/2021/seasontype/2'
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        # Creates elements from html that will be the base for the Data Frame
        table = soup.find('div', attrs = {'class':'ResponsiveTable ResponsiveTable--fixed-left mt5 remove_capitalize'})
        table2 = soup.find('div', attrs = {'class':'Table__Scroller'})
        
        #Creates Pandas dataframes 
        df= pd.read_html(str(table))[0]
        df2= pd.read_html(str(table2))[0]
        
        # Combines tables to create readable data
        resultP = df.join(df2)
        index = resultP.index
        resultP = resultP.drop(resultP.index[len(index) - 1])
        resultP = resultP.assign(Team = teamp[-1])
        aggrigate_teams = aggrigate_teams.append(resultP)        
        del teamp[-1]
        
        if len(team) < 1:
            break
    #Sends data to database 
    con = sqlite3.connect("MLB_Stats.sqlite") # change to 'sqlite:///your_filename.db'
    cur = con.cursor()    
    aggrigate_teams.to_sql("Pitching_Stats", con, if_exists='replace', index=False)         
    con.commit()
    con.close()     
    # stops timer of the inquary and ouputs total time taken for pitching scrape
    clock = "{:.3f}".format(time.time() - start_time)
    #set this up because there has to be a way to make this more efficient, not sure how.
    print("Inquiry took:", clock ,"seconds.\n")
    return aggrigate_teams
def team_hitting(team):
    con = sqlite3.connect("MLB_Stats.sqlite") # connecting to database
    print("Hitting Statistics for you chosen team: \n")
    pd.set_option('display.max_columns', None)
    print(pd.read_sql_query("Select Name, AB, R, H , HR, RBI, BB, SO, AVG, OBP, OPS FROM Batting_Stats WHERE Team == ('%s')" % (team), con))
def team_pitching(team):
    con = sqlite3.connect("MLB_Stats.sqlite") # connecting to database
    print("Pitching Statistics for you chosen team: \n")
    pd.set_option('display.max_columns', None)
    print(pd.read_sql_query("Select Name, GP, W, L, SV, IP, H, ER, HR, BB, K, WHIP, ERA FROM Pitching_Stats WHERE Team == ('%s')" % (team), con))    
def Average_query():
    con = sqlite3.connect("MLB_Stats.sqlite") # connecting to database
    print("Top 5 for Batting Average with at least 45 at bats:\n")
    pd.set_option('display.max_columns', None)
    print(pd.read_sql_query("SELECT Name, AB, AVG, Team FROM Batting_Stats WHERE AB >=45 ORDER BY AVG DESC LIMIT 5", con))

def Strikeout_query():
    con = sqlite3.connect("MLB_Stats.sqlite") # connecting to database
    print("Top 5 for Strikeouts: \n")
    pd.set_option('display.max_columns', None)
    print(pd.read_sql_query("SELECT Name, GP, GS, W, L, SV, IP, K, ERA, Team FROM Pitching_Stats ORDER BY K DESC LIMIT 5", con),"\n")
def ERA_query():
    con = sqlite3.connect("MLB_Stats.sqlite") # connecting to database
    print("ERA Leaders with at least 40 innings pitched: \n")
    print(pd.read_sql_query("SELECT Name, GP, W, L, SV, IP, K, ERA, Team FROM Pitching_Stats WHERE IP >=40 ORDER BY ERA ASC LIMIT 5", con),"\n")
def Homerun_query():
    con = sqlite3.connect("MLB_Stats.sqlite") # connecting to database
    print("Top 5 for Home Runs: \n")
    print(pd.read_sql_query("SELECT Name, AB, HR, Team FROM Batting_Stats ORDER BY HR DESC LIMIT 5",con),"\n")
    
def Hitting_league_leaders():
    con = sqlite3.connect("MLB_Stats.sqlite") #connect to database
    print("Hitting leaders from around the league:\n")
    AVG = pd.read_sql_query("SELECT Name, AVG, Team FROM Batting_Stats WHERE AB >45 ORDER BY AVG DESC LIMIT 1",con)
    H = pd.read_sql_query("SELECT Name, H, Team FROM Batting_Stats ORDER BY H DESC LIMIT 1",con)
    Dbl = pd.read_sql_query('SELECT Name, "2B", Team FROM Batting_Stats ORDER BY "2B" DESC LIMIT 1',con)
    Trip = pd.read_sql_query('SELECT Name, "3B", Team FROM Batting_Stats ORDER BY "3B" DESC LIMIT 1',con)
    HR = pd.read_sql_query("SELECT Name, HR, Team FROM Batting_Stats ORDER BY HR DESC LIMIT 1",con)
    RBI = pd.read_sql_query("SELECT Name, RBI, Team FROM Batting_Stats ORDER BY RBI DESC LIMIT 1",con)
    pd.set_option('display.max_colwidth', 40)
    pd.options.display.float_format = '{:,.3f}'.format
    print("Average:\n",AVG.to_string(index=False),"\n")
    pd.reset_option('display.float_format')
    print("Hits:\n",H.to_string(index=False),"\n")
    print("Doubles:\n",Dbl.to_string(index=False),"\n")
    print("Triples:\n",Trip.to_string(index=False),"\n")
    print("Home Runs:\n",HR.to_string(index=False),"\n")
    print("Runs Batted In:\n",RBI.to_string(index=False),"\n")
    
def Bar_Graph(df):
    graph ={"Team":[],"HR":[]}
    while len(graph_List) > 0:
        Homeruns = df[df.Team == graph_List[-1]]
        z = Homeruns['HR'].sum()
        graph["Team"].append(graph_List[-1])
        graph["HR"].append(z)
        del graph_List[-1]
            
    frame = pd.DataFrame(graph, columns = ['Team', 'HR'])
    frame = frame.set_index("Team") 
    ax = frame.plot(kind='bar',width=.65, color='red')
    for p in ax.patches:
        ax.annotate(str(p.get_height()), (p.get_x() * 1.00, p.get_height() * 1.005))
    plt.title("Total Home Runs for Each Team")
    plt.show()
def Pitching_graph(data):
    x = data["H"]
    y = data["ER"]
    plt.scatter(x,y)
    
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    plt.plot(x,p(x),"r--")
    plt.title("Hits Allowed/Earned Runs Allowed")
    plt.xlabel("Hits Allowed")
    plt.ylabel("Earned Runs Allowed")
    plt.show()
    
def main():
    
    print("Lets take a look at some statistics from around the MLB.")
    print("The data will be stored in a database and we will display a few queries as examples for each table!")
    bat = input("Press ENTER to continue!")
    print("Fetching Data....\n")
    df = Batting()
    print("Now lets create a bar graph from that data that displays the total home runs for each team")
    bat = input("Press ENTER to continue!\n")
    Bar_Graph(df)
    print("Now lets take a look at some queries of the data base that display the homerun leaders and average leaders from around the MLB!\n")
    bat = input("Press ENTER to continue!\n")
    Homerun_query()
    Average_query()
    print("\nNow we can take a look at some of the statistics from pitchers from around the league!")
    pitch = input("Press ENTER to continue!")
    print("Fetching Data....\n")
    data = Pitching()
    print("Now we can create a scatter plot that shows for each pitcher what trend occurs when comparing hits allowed and earned runs allowed.")
    pitch = input("Press ENTER to continue!")
    Pitching_graph(data)
    print("Now lets take a look at some queries of the data base that display the strikeout and ERA leaders from around the MLB!\n")
    pitch = input("Press ENTER to continue!\n")
    Strikeout_query()
    ERA_query()
    print("\n You can take a look at the database and get plenty of more information about each player, it will be avalible in the same folder as this file")
    print("Have a nice day!")

if __name__ == "__main__":
    main()

