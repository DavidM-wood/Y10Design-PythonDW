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
    myfile.write("<p>Please feel free to visit <a href='https://www.thesportsdb.com/api.php?ref=apilist.fun'>Sports DB</a> for further info.</p>")
    myfile.write(data)
    myfile.close()


def SearchBasketballHistory(data):
    l = []
    wlist = []
    l = data.split('.')
    

    for i in l:
        if "invented" in i:
            wlist = i.split(' ')
            for w in wlist:
                if w.isdigit():
                    print("Invented in:",w)
                else:
                    pass
            #print("Invented: ", i)
        else:
            pass

def SearchBaseballHistory(data):
    l = []
    l = data.split('\n')

    for i in l:
        if "evolved" in i:
            print("History:", i)
        else:
            pass

def SearchDescription(data):
    l = []
    l = data.split('\n')

    for i in l:
        if"score" in i:
            print("Description:", i)
        else:
            pass

def FullText(data):
    print(data)


'''def basicdescription(data)

def full description(data)'''

def main():
    # use API to get place info
    # response = requests.get("https://geo-info.co/43.65,-79.40")
    response = requests.get("https://www.thesportsdb.com/api/v1/json/1/all_sports.php")

    # if API call is correct
    if (response.status_code == 200):
        data = response.content # response comes in as byte data type
        writeHTML(data.decode())  # call function to write string data to HTML file

        # load as a JSON to access specific data more easily
        d = {}

        
        d[1] = "Baseball"
        d[2] = "Basketball"
        d[3] = "American Football"
        d[4] = "Ice Hockey"

        print ("Select one from the following sports")
    
        print("1. Baseball")
        print("2. Basketball")
        print("3. Football")
        print("4. Hockey")

        inp = input()
        inp = int(inp)

        user_inp = d[inp]


        d2 = {}

        d2[1] = "History"
        d2[2] = "Description"
        d2[3] = "Full Text"


        print("Please select which information you would like to see.")
        print("1 History of", d[inp])
        print("2 Description of", d[inp])
        print("3 Full Text")

        inp2 = input()
        inp2 = int(inp2)

        user_inp2 = d2[inp2]





        datajson = response.json()
        sports = datajson["sports"]
        for sport in sports:
            sportName = sport['strSport']
            if sportName == user_inp:
                search = user_inp2
                if search == "History" and sportName == "Basketball":
                   SearchBasketballHistory(sport['strSportDescription'])
                elif search == "History" and sportName =="Baseball":
                    SearchBaseballHistory(sport['strSportDescription'])

                elif search == "Description":
                    SearchDescription(sport["strSportDescription"])
                elif search == "Full Text":
                    FullText(sport["strSportDescription"])
                
                else:
                    print("Invalid Request")
                #print(sport['strSportDescription'])
            else:
                pass
           
        
    else:
        data = "Error has occured"
        writeHTML(data)

main()
