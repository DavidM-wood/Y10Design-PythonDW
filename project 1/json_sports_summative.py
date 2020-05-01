'''
myapi.py 
- simple program to demo using a web API with requests Python module
- secondary function to demo how to write out received data to an HTML file 
'''

import requests
import json

# Find APIs at - https://apilist.fun/
# some will require an API key, boo hiss!

# cool geo example
# https://geo-info.co/?ref=apilist.fun
# example - https://geo-info.co/43.65,-79.40

# cool funny example
# https://funtranslations.com/api/chef
# https://api.funtranslations.com/translate/chef.json?text=I%20like%20upper%20canada%20college

# For any indentation errors, make sure there are no tabs (\t) by doing 
# a full replace of \t with 4 actual spaces

def writeHTML(data):
    myfile = open("myapi.html","w")
    myfile.write("<h1>JSON file returned by API call</h1>")
    myfile.write("<p>Copy and paste to <a href='https://jsoneditoronline.org/'>JSON editor</a> for pretty format.</p>")
    myfile.write(data)
    myfile.close()


def searchhistory(data):
    l = []
    l = data.split('.')

    for i in l:
        if "invented" in i:
            print("Invented: ", i)
        else:
            pass

'''def basicdescription(data)

def full description(data)'''

def main():
    # use API to get place info
    # response = requests.get("https://geo-info.co/43.65,-79.40")
    response = requests.get("https://www.thesportsdb.com/api/v1/json/1/all_sports.php")

    # if API call is correct
    if (response.status_code == 200):
        data = response.content # response comes in as byte data type
        # data_as_str = data.decode()    # decode to str
        # writeHTML(data_as_str)  # call function to write string data to HTML file

        # load as a JSON to access specific data more easily
        d = {}

        d[1] = "Soccer"
        d[2] = "Baseball"
        d[3] = "Basketball"
        d[4] = "American Football"
        d[5] = "Ice Hockey"

        print ("Select one from the following sports")
        print("1. Soccer")
        print("2. Baseball")
        print("3. Basketball")
        print("4. Football")
        print("5. Hockey")

        inp = input()
        inp = int(inp)

        user_inp = d[inp]







        datajson = response.json()
        sports = datajson["sports"]
        for sport in sports:
            sportName = sport['strSport']
            if sportName == user_inp:
                searchhistory(sport['strSport'])
                print(sport['strSportDescription'])
            else:
                pass
            # print(sport['strSport'], sport['strSportDescription'])
        # print(data)
        # cities = datajson['nearbyCities']
        # for city in cities:
            # print(city)
        
    else:
        data = "Error has occured"
        writeHTML(data)

main()