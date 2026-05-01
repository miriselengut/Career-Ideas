import requests
import json


def quit_rate_api():
    headers = {'Content-type': 'application/json'}
    data = json.dumps({"seriesid": ['JTS000000000000000JOR','JTS000000000000000QUR'],"startyear":"2022", "endyear":"2025"})
    p = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/', data=data, headers=headers)
    json_data = json.loads(p.text)
    if "Results" not in json_data:
        print("API error:", json_data)
        return []
    data_table = []
    for series in json_data['Results']['series']:
        for item in series['data']:
            info = {
                #"seriesId": series['seriesID'],
                "year": item['year'],
                "period": item['period'],
                "value": item['value']
            }
            data_table.append(info)
    print(data_table)

quit_rate_api()