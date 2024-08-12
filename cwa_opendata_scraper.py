import requests
import json
import os
import pprint

def get_cuties_weather():
    header={
        'Accept':'application/json'
    }
    parameters={
        'Authorization':os.getenv("CWA_API_KEY",None),
        'locationName':['臺中市']
    }

    url= r"https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001"

    response = requests.get(url, headers=header, params=parameters)
    print(response)

    if response.status_code == 200:
        weathr_data=response.json()
    else:
        print("Requests Fail")

    weather_element_name = {
        'Wx':"天氣現象",
        'Pop':"降雨機率",
        'CI':"舒適度",
        'MinT':'時段最低溫度',
        'MaxT':'時段最高溫'
    }
    #pprint(weathr_data['records']['location'])
    cities_weather = dict()
    for location in weathr_data['records']['location']:
        
        print(location['locationName'])
        city_name = location['locationName']
        city_weather =get_city_weather(location)
        city_weather = dict()
        

def get_city_weather(location):
    city_weather = dict()
    for element in location['weatherElement']:
        print(element['elementName'],end=':')
        print(element["time"][0]['parameter']['parameterName'])
        element_name=element['elementName']
        element_value=element["time"][0]['parameter']['parameterName']

        if element_name in ['MinT', 'MaxT']:
            element_unit = "C"
        elif element_name in ['PoP']:
            element_unit = '%'
        else:
            element_unit = ""
        element_name=weather_element_name[element_name]
        city_weather[element_name] = element_value + element_unit


    return city_weather
if __name__ == '__main__':
    cwa_api_key