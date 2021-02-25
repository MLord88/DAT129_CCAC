import json

#Create a data structure in Python which we'll encode/serialize into JSON specs
#friendly text
Baseball_Teams = {}
Baseball_Teams['Yankees'] = 'New York Yankees, 26 time Champions'
Baseball_Teams['Pirates'] = 'Pittsburgh Pirates, how can they be this bad'
Baseball_Teams['Nationals'] = 'Washington Nationals, Better without Bryce'
Baseball_Teams['Rays'] = 'Tampa Bay Rays, Should have kept the Devil in the name'
Baseball_Teams['Do the Astros deserve their worldseries?'] = False
Baseball_Teams["Pirates Payroll in 2020"] = f'${25337837:,}'
Baseball_Teams["Yankees Payroll in 2020"] =  f'${111939081:,}'

print(json.dumps(Baseball_Teams))

with open('baseball_teams.json', 'w')  as baseball_file:
    baseball_file.write(json.dumps(Baseball_Teams))