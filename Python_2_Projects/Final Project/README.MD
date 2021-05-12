# Statistics from Major League Baseball Players

## Abstract
When i started this project i set out to create a database with up to date player statistics from every team in the MLB.

## Purpose
The purpose of this python script is to give the user access to a database of MLB player data. Along with this it gives some sample query and output types that anothe user could use when using this script if they desired. I could have done a million things with the data collected and this code could easily be adapted to do those things if the user desiered. 

## Background/sources
A little bit of background on why i chose this topic and why i chose create this particular script:
* Baseball has been a part of my life since i was a little kid. Basically as long as i can remember. 
* Part of the fun of the game is being curious about specific players and their statistics.
* Always wanted to have access to a custom tool to anylize sports statistics.
### Sources
* Data was scraped from the web mostly from [ESPN](https://www.espn.com/mlb/team/stats).
* Also a custom CSV that imports team names

## Results
### DataBase
#### Batting Statistics for every player that has recored and at bat:
![Batting_Table](https://user-images.githubusercontent.com/78560792/118042391-02231880-b342-11eb-9f52-46a103c804f5.PNG)
#### Pitching Statistics for every player that has thrown a pitch this season:
![Pitching_Table](https://user-images.githubusercontent.com/78560792/118042632-529a7600-b342-11eb-817a-84e765fbc363.PNG)
### Python Script Results
#### Home Run and Batting Average Top 5:
![Batting_query_output](https://user-images.githubusercontent.com/78560792/118042962-be7cde80-b342-11eb-863a-d6d4ec436f09.PNG)
#### Graph showing total homeruns for each team in MLB:
![Homerun_graph](https://user-images.githubusercontent.com/78560792/118043127-f6842180-b342-11eb-82c9-82668726aace.PNG)
#### Strikeout and ERA(Earned Run Average) Leaders:
![Pitching_query_output](https://user-images.githubusercontent.com/78560792/118043136-fab03f00-b342-11eb-9a90-4b4b6ccee66a.PNG)
#### Scatter plot comparing hits alllowed by each pitcher this season to the amount of earned runs allowed by each pitcher:
![Pitching_Scatter](https://user-images.githubusercontent.com/78560792/118043387-4b279c80-b343-11eb-8b31-a47384135674.PNG)
## Conclusions:
I have come to the realization while completing this project that there would be much more to expand on in this script. Pulling in different sources of data and creating an extensive database would make the options for data crunching to be almost endless. Although there are resources out there on the web that can do the things that this script can do do it is always fun to create your own so that you can learn from it. 
## Limitations:
* Time constraints(would love to have had more time avalible to make this even more robust)
* Stuggled to come up with deep data comprehensions due to focusing more on the coding aspect of the project
## Future research:
I would like to in the future research more into databases so that i can make something similar to this with a better database structure. I feel like the way i did things although seemed easy resulted in a less then optimal database structure.
