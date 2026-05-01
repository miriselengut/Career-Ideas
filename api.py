import requests
import json
import sqlite3 as st

def quit_rate_api():
    try:
        headers = {'Content-type': 'application/json'}
        data = json.dumps({"seriesid": ['JTS000000000000000JOR'],"startyear":"2020", "endyear":"2026"})
        p = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/', data=data, headers=headers)
        json_data = json.loads(p.text)
    except requests.exceptions.RequestException:
        return "No valid connection"
    if "message" in json_data and json_data["message"]:
        #if called too many time, can't reach api, return table to build on code until limit resets
        st.Error("API limit reach for the day. Try again later")
        return [{'year': '2025', 'period': 'M12', 'periodName': 'December', 'value': '4.0'},
                {'year': '2025', 'period': 'M11', 'periodName': 'November', 'value': '4.1'}, 
                {'year': '2025', 'period': 'M10', 'periodName': 'October', 'value': '4.3'}, 
                {'year': '2025', 'period': 'M09', 'periodName': 'September', 'value': '4.3'}, 
                {'year': '2025', 'period': 'M08', 'periodName': 'August', 'value': '4.2'}, 
                {'year': '2025', 'period': 'M07', 'periodName': 'July', 'value': '4.3'}, 
                {'year': '2025', 'period': 'M06', 'periodName': 'June', 'value': '4.3'}, 
                {'year': '2025', 'period': 'M05', 'periodName': 'May', 'value': '4.4'}
                ]
    data_table = []
    try:
        for series in json_data['Results']['series']:
            for item in series['data']:
                info = {
                    "year": item['year'], 
                    "period": item['periodName'], 
                    "value": item['value']
                }
                data_table.append(info)
        return data_table
    except (KeyError, TypeError):
        return "Missing or incorrect results in response"