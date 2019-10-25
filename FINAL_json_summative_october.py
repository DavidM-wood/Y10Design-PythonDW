'''
myapi.py 
- simple program to demo using a web API with requests Python module
- secondary function to demo how to write out received data to an HTML file 
'''

import requests
import json





def writeHTML(data):

    myfile = open("SportAPI.html","w") # use "a" to "append"
    
    ############### CSS
    
    myfile.write("""
    <html>

      <head>
        <title> MY PAGE </title>
      </head>

      <body>
        <font size="3" color="red">This page belongs to David Wood!</font>
        <h1>Welcome to My List of Sports Page</h1>

        <p>Go to <a href='https://www.thesportsdb.com/api.php?ref=apilist.fun'>The Sports DB</a> for API Info.</p>

       
        <p> This page shows the basic history, the sport description, and the full text about the sport for baseball, basketball, football and hockey</p>
        <h1 style="background-color:DodgerBlue;">Here is the information you requested</h1>

        <p> Info: """+ data+"""</p>

       
      </body>

    </html>""")

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
                    # added HTML call
                    writeHTML(w)
                else:
                    pass
        else:
            pass

#SearchBFHHistory searches the paragraph in Baseball, Football, and Hockey about the history of the game. 
def SearchBFHHistory(data):
    l = []
    l = data.split('\n')

    for i in l:
        if "evolved" in i:
            print("History:", i)
            writeHTML(i)
        else:
            pass

def SearchDescription(data):
    l = []
    l = data.split('\n')

    for i in l:
        if"score" in i:
            print("Description:", i)
            writeHTML(i)
        else:
            pass



def FullText(data):
    writeHTML(data)
    print(data)

d = {}

d[1] = "Baseball"
d[2] = "Basketball"
d[3] = "American Football"
d[4] = "Ice Hockey"
inp = None

def makeSelection():
    global d, inp

    print ("Select one from the following sports")

    print("1. Baseball")
    print("2. Basketball")
    print("3. Football")
    print("4. Hockey")

    inp = input()

    try:
        inp = int(inp)
        if inp not in [1, 2, 3, 4]:
            print("Invalid input!")
            return makeSelection()
        return inp
    except:
        print("Invalid input!")
        return makeSelection()

d2 = {}
d2[1] = "History"
d2[2] = "Description"
d2[3] = "Full Text"

def makeSelection2():
    global d2, d, inp

    print("Please select which information you would like to see.")
    print("1 History of", d[inp])
    print("2 Description of", d[inp])
    print("3 Full Text")

    inp2 = input()

    try:
        inp2 = int(inp2)
        if inp2 not in [1, 2, 3]:
            print("Invalid input!")
            return makeSelection2()
        return inp2
    except:
        print("Invalid input!")
        return makeSelection2()

def body():
    global d, inp, d2
    # use API to get place info
    # response = requests.get("https://geo-info.co/43.65,-79.40")
    response = requests.get("https://www.thesportsdb.com/api/v1/json/1/all_sports.php")

    # if API call is correct
    if (response.status_code == 200):
        data = response.content # response comes in as byte data type
        #writeHTML(data.decode())  # call function to write string data to HTML file

        print("Loading...")


        inp = makeSelection()
        print(inp)
        user_inp = d[inp]



       
        inp2 = makeSelection2()
        print(inp2)
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
                    SearchBFHHistory(sport['strSportDescription'])
                elif search == "History" and sportName == "American Football":
                    SearchBFHHistory(sport['strSportDescription'])
                elif search == "History" and sportName == "Ice Hockey":
                    SearchBFHHistory(sport['strSportDescription'])

                elif search == "Description":
                    SearchDescription(sport["strSportDescription"])
                elif search == "Full Text":
                    FullText(sport["strSportDescription"])
                
                else:
                    print("Invalid Request")
            else:
                pass
           
        
    else:
        data = "Error has occured"

body()
