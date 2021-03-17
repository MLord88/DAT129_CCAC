from csv import DictReader
# Parsing the Toxic Inventory from WPRDC
# https://data.wprdc.org/dataset/toxic-release-inventory/resource/b2d6f249-4e3b-4c38-b4bc-5dafd3cb55e7

triunderground = {'incident_count':0,'facility':{},'company':{},'year':{}}

with open('tri_underground.csv') as trifile:
    #pass our file object to the DictReader constructor, creating an interable Reader object
    dreader = DictReader(trifile)
    #print(dreader.fieldnames)
    for record in dreader:
        triunderground['incident_count'] = triunderground['incident_count'] + 1
        if record ['FACILITY_NAME'] not in triunderground['facility']:
            #print('Located new Facility: ', record['FACILITY_NAME'])
            triunderground['facility'][record['FACILITY_NAME']] = 1
        else:
            triunderground['facility'][record['FACILITY_NAME']]+= 1
        if record ['PARENT_CO_NAME'] not in triunderground['company']:
            #print('Located new Parent Company: ', record['PARENT_CO_NAME'])
            triunderground['company'][record['PARENT_CO_NAME']] = 1
        else:
            triunderground['company'][record['PARENT_CO_NAME']]+= 1
        if record['REPORTING_YEAR'] not in triunderground['year']:
            #print('Located new event: ', record['REPORTING_YEAR'])
            triunderground['year'][record['REPORTING_YEAR']] = 1
        else:
            triunderground['year'][record['REPORTING_YEAR']] += 1
maximum_f = max(triunderground['facility'], key = triunderground['facility'].get)
minimum_f = min(triunderground['facility'], key = triunderground['facility'].get)
maximum_c = max(triunderground['company'], key = triunderground['company'].get)
minimum_c = min(triunderground['company'], key = triunderground['company'].get)
US_company = triunderground['incident_count'] - (triunderground['company'][maximum_c])
percent = (US_company) / (triunderground['incident_count']) *100

print('Data pulled from the TRI Underground file provided from the WPRDC')
print('-------------------------------------------------------------------\n')
print('Most incidents per facility: ' ,maximum_f, 'with', triunderground['facility'][maximum_f],'incident(s)')
print('Least incidents per facility: ',minimum_f, 'with', triunderground['facility'][minimum_f],'incident(s)')
print()
print('Most incidents per company: ' ,maximum_c, 'with', triunderground['company'][maximum_c],'incident(s)')
print('Least incidents per company: ',minimum_c, 'with', triunderground['company'][minimum_c],'incident(s)')
print('----------------------------------------------------------------')
print('Percent of incidents with a US based company: ',round(percent, 5),'%')
print('----------------------------------------------------------------')
print('List of incidents per company:\n----------------------------------------------------------------')
for y in sorted(triunderground['company']):
    print(y, ':', triunderground['company'][y],end='\n')
