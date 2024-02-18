import time
import random
import json
"""
MODULE fOR MAIN GAME FUNCTIONS    
"""

companies = {
            "henriks":{
                "stock_value":76,
                "value_change_rate":7,
                "description": "A department store than has been on the Highstreet for over 200 years and has 150 stores across the UK. ",
                "values_list":[76],
                "stock-owned": 0
             },
             "infinity":{
                "stock_value":16,
                "value_change_rate":1,
                "description" : "A tech company that makes electronic cars, solar panels and batteries for a more sustainable future away from fossil fuels", 
                "values_list": [16],
                "stock-owned": 0
             },
             "palmer":{
                "stock_value":141.46,
                "value_change_rate":14,
                "description" : "multinational technology company focusing on artificial intelligence, online advertising, search engine technology, cloud computing, computer software,  consumer electronics",
                "values_list":[141],
                "stock-owned": 0
             },
             "jojo":{
                "stock_value":45,
                "value_change_rate":4,
                "description" : "upscale athletic ware than does most of their business online", 
                "values_list":[45],
                "stock-owned": 0
             }
            }
date_list=[]
pause_flag=False

current_week = 0
current_month = 13
year = 2016
megaMonth = 2 #1 and 12 - Month that the Mega event happens
megaWeek = 0 # 1 and 4 - Week that the Mega event happpens
mediumWeek = 1 #1 and 4 - Week that the Medium event happens

immediate = 0


def jsonToDictionary(fileName):
    """Turns JSON dictionary to a normal dictionary"""
    with open(fileName, 'r', encoding="utf-8") as json_file:
        events = json.load(json_file)
    return events

def chooseMediumevent(filename):
    choice = random.randint(0,2)  # Where 2 is number of possible events - 1
    # medium section from json file for current company (given by filename)
    with open(filename,"r",encoding ="utf-8") as f : # opens the json file
            json_data = json.load(f)
            file = json_data["medium"]
    description = file[choice]["description"]
    immediate = file[choice]["immediateEffect"]

    return description, immediate

def chooseMegaEvent(filename): 
    """"get the mega event for the year"""
    # global year
    # description = ""
    # immediate = 0
    # overtime = 0 
    # with open(filename,"r",encoding ="utf-8") as f : # opens the json file
    #     json_data = json.load(f)
    #     mega_info = json_data["mega"]
    # for i in range(len(mega_info)-1):
    #     if (mega_info[i]["year"] == year):
    #         print(mega_info[i])
    #         description = mega_info[i]["description"]
    #         immediate = mega_info[i]["immediateEffect"]
    #         overtime = mega_info[i]["overTimeEffect"]

    description = "An industry wide change occured"
    immediate = -20
    overtime = 5
    return description, immediate, overtime


def date():
    return_val = str(current_week) + " " + str(current_month)  + " " + str(year)
    return return_val

def getMonth():
    """ decide what month the mega event is happening  """
    global megaMonth
    month = random.randint(1,12)
    megaMonth = month

def getWeek():
    """"If mega in current month, chosethe week it occurs
    Then chose one week for the medium event to occur"""
    global current_month
    global megaWeek, megaMonth, mediumWeek
    if megaMonth == current_month:
        megaWeek = random.randint(1,4)
    mediumWeek = random.randint(1,4)
    while megaWeek == mediumWeek:
        mediumWeek = random.randint(1,4)

def weekLoop(company_json):
    """"Generate normal event
    execute larger event if scheduled"""
    global current_week
    global megaWeek, mediumWeek
    global immediate

    normalEvent = random.randint(-5,5)
    # insert ripple modifier
    description = "Nothing happened this week"
    if (current_week == megaWeek and current_month == megaMonth):
        description, immediate, overtime = chooseMegaEvent(company_json)
        print(date() + " - Mega event happened")
    elif (current_week == mediumWeek):
        description, immediate = chooseMediumevent(company_json)
        print(date() + " - Medium event happened")
    else:
        print(date())

    return description
    # Overtime added to value_change_rate in company's dictionary

def timeIncriment():
    """Increases time properly becuse im cool"""
    global current_week, current_month, year
    global megaWeek, megaMonth, mediumWeek
    current_week += 1
    if (current_week > 4):
        current_week %= 4
        current_month += 1
        getWeek()
        print("megaWeek = " + str(megaWeek))
        print("mediumWeek = " + str(mediumWeek))
    if current_month > 12:
        current_month %= 12
        year += 1
        # Can also add a thing to stop everything when year == 2024
        getMonth()
        print("megaMonth = " + str(megaMonth))

def stock_change():
    """Updates stock value and appends new value
    to list for graph generation."""
    global companies, immediate
    company_list = ["henriks", "infinity", "palmer", "jojo"]
    for i in range(len(company_list)-1):
            stock_value = companies[company_list[i]]["stock_value"]

            # value_change_rate is now the ripple effect
            value_change_rate = companies[company_list[i]]["value_change_rate"]
            normal_change = random.randint(-5,5)

            stock_value = stock_value + immediate + value_change_rate + normal_change
            
            # immediate is done only once, so down to 0 once used
            immediate = 0

            # Lowers value_change_rate until it's 0
            # At this point the ripple is gone!
            if(value_change_rate > 0):
                value_change_rate -= 1
            elif(value_change_rate < 0):
                value_change_rate += 1

            companies[company_list[i]]["values_list"].append(stock_value)
            companies[company_list[i]]["stock_value"] = stock_value
            companies[company_list[i]]["value_change_rate"] = value_change_rate
    date_list.append(date())

if __name__ == "__main__":
    # events_1 = jsonToDictionary("henrik's_department_store.json")
    # events_2 = jsonToDictionary("infinity_corp.json")
    # events_3 = jsonToDictionary("palmer_tech.json")
    # events_4 = jsonToDictionary("jojo_corp.json")


    for i in range(50):
        timeIncriment()
        weekLoop("test.json")
        stock_change()
    company = 'henriks'
    print(companies[company]["values_list"])