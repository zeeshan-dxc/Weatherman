"""
import http.client

conn = http.client.HTTPSConnection("")

api_key = '23b9b2cda2de73f546fb9ac14d881d73'
api_address = "api.openweathermap.org/data/2.5/weather?q=London"

last_part_of_request = "appid={your api key}"
headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "f8fe826b3emshc8d3a2bad2afae0p19c39djsn53e0961bb1d4"
}

conn.request("GET", "/weather?callback=test&id=2172797&units=%2522metric%2522%20or%20%2522imperial%2522&mode=xml%252C%20html&q=London%252Cuk", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
"""

import requests
import simplejson as json


def main():
    """
    value = input(
        "Which planet do you want to know about? Type a number between 1 and 10 - or however many planets there are...!\n")
    """

    response = requests.get(
        "http://api.openweathermap.org/data/2.5/forecast?q=London&appid=23b9b2cda2de73f546fb9ac14d881d73")

    print(response.status_code)

    print(response.json())

    """
    jayson = response.json()

    string = response.text

    #planets = json.loads(string)

    for key in jayson:
        if (key == 'results'):
            #print("JSN.RESULTS IS TYPE: " + str(type(jayson[key])))
            for i in range(len(jayson[key])):
                print("PLANET: " + str(i) + ": " + str(jayson[key][i]['name']))
                i += 1

            #print(key, '--->', jayson[key])

    # for planet in planets:
    #   print("The planet is called: " + planet.results['name'])
"""


if __name__ == '__main__':
    main()
