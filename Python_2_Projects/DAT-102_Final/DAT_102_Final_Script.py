import pandas as pd
import numpy as np
import requests
import time
import sqlite3
import xlsxwriter
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from bs4 import BeautifulSoup

column_names = ["Years"]
Years_csv = pd.read_csv("years.csv", names=column_names)
Years = Years_csv.Years.to_list()
Years2= Years.copy()
del Years2[0]
# Goal is to scrape all teams in the MLB for pitching and batting statitics and find the leader in the categories of average and strikeouts(K's)
def Payroll(): # Creates database table for every hitter in the major league with up to date statistics for 2021 from espn.com
    start_time = time.time()
    while len(Years) > 0:
        #scrape data and create readable data
        url = f'http://www.thebaseballcube.com/topics/payrolls/byYear.asp?Y={Years[-1]}'
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        # Creates elements from html that will be the base for the Data Frame
        table = soup.find('div', attrs = {'class':'section_dataGrid'})
        #Creates Pandas dataframes
        try:
            df = pd.read_html(str(table))[0]
        except:
            print('Completed')
            break
        index = df.index
        df = df.drop(df.index[len(index) - 1])        
        df = df.dropna(axis = 1, how = 'any')
        df.columns = df.iloc[0]
        df = df.drop([0])
        df = df.reset_index(drop = True)
        print(df)
        con = sqlite3.connect("Payroll.sqlite") # change to 'sqlite:///your_filename.db'
        cur = con.cursor()    
        df.to_sql(f"{Years[-1]}", con, if_exists='replace', index=False)         
        con.commit()
        con.close()              
        # Combines tables to create readable data
        del Years[-1]
        
        if len(Years) < 1:
            break
    #ends timer for inquary
    clock = "{:.3f}".format(time.time() - start_time)
    print("Inquiry took:", clock ,"seconds.\n")
    
    
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
def Payroll_graph(data):
    data.plot(x='WPct', y="Team Payroll")
    #z = np.polyfit(x, y, 1)
    #p = np.poly1d(z)
    #plt.plot(x,p(x),"r--")
    plt.show()
def Years_List():
        Years_dict = {f'{Years2[1]}':[],f'{Years2[2]}':[],f'{Years2[3]}':[],f'{Years2[4]}':[],
                      f'{Years2[5]}':[],f'{Years2[6]}':[],f'{Years2[7]}':[],f'{Years2[8]}':[],f'{Years2[9]}':[],
                      f'{Years2[10]}':[]}
                     
        print(Years_dict)
        return Years_dict
def statistics():
    con = sqlite3.connect("Payroll.sqlite")
    c = ['Years']
    year = pd.DataFrame(Years2 ,columns=c)
    year = year.sort_values(by='Years',ascending=True)
    year = year.reset_index(drop=True)
    comp = pd.DataFrame()
    while len(Years2) >0:
        sql = 'SELECT "Team Payroll", WPct FROM ? WHERE "Team Name" == "Pittsburgh Pirates"'
        y = pd.read_sql_query('SELECT "Team Payroll", WPct FROM "%s" WHERE "Team Name" == "Pittsburgh Pirates"' % str(Years2[-1]), con)
        comp = comp.append(y)
        del Years2[-1]
    comp = comp.reset_index(drop=True)
    result = year.join(comp)
    result.to_csv('Pirates_Data.csv')
    return result
    
def main():
    data = statistics()
    Payroll_graph(data)


if __name__ == "__main__":
    main()

