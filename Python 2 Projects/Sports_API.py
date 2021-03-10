import requests, json 
from csv import DictReader

url = "https://mlb-data.p.rapidapi.com/json/named.player_teams.bam"

querystring = {"player_id":"'493316'","season":"'2019'"}

headers = {
    'x-rapidapi-key': "3373986159mshacd89d2d6a3b458p1f883djsn0cf637deb7fd",
    'x-rapidapi-host': "mlb-data.p.rapidapi.com"
    }

def player_by_id():
    
    player_id = input("Enter player ID to lookup a specific player.\n")
    player_search = f"/json/named.player_info.bam?sport_code='mlb'&player_id={player_id}"
    full_url = url + player_search
    return(full_url)


def player_by_Name():
    name_part = input("Input player's last or first and last name for the player you wish to lookup.\n")
    name_part = name_part.lower()
    if len(name_part.split()) == 1:
        name_part = name_part + "%25"
        name_part = f"'{name_part}'"
    else:
        name_part = f"'{name_part}'"
    active_sw = input("Is the player you are looking for an active MLB player? (Y or N)\n")
    active_sw = active_sw.upper()
    active_sw = f"'{active_sw}'"
    player_search = f"/json/named.search_player_all.bam?sport_code='mlb'&active_sw={active_sw}&name_part={name_part}"
    full_url = url + player_search
    print(full_url)
    return full_url

def main():
    x = int(input("Would you like to lookup MLB players by ID number or name? (1 for ID or 2 for name)\n"))
    if x == 1:
        resp = requests.get(player_by_id(), headers = headers)
        print("Made request, response status: ", resp.status_code)
        if (int(resp.status_code)) == 200:
            payload = json.loads(resp.text)
            print(payload) 
    if x == 2:
        resp = requests.get(player_by_Name(), headers = headers)
        print("Made request, response status: ", resp.status_code)
        if (int(resp.status_code)) == 200:
            payload = json.loads(resp.text)
            print(payload)         

main()