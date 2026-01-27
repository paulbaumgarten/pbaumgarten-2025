import machine
import utime
import ujson
import requests
from cyd import *
from WIFI import WIFI
from tthelp import get_timetable_day

#########################################################
## Settings
#########################################################

NETWORKS = [("SCWiFi","wifi1234"),('BAUMG','91315689')]
API = "https://api.pbaumgarten.com/pets"

PET_NAME = "" # Your personalised name for your pet
PET_ID = "" # Your PET_ID from your teacher
API_KEY = "" # Your API_KEY from your teacher

#########################################################
## Functions
#########################################################

def show_welcome():
    # Welcome screen
    display.clear(Colors.black)
    display.draw_image('tamagotchi smile.raw',140,0,180,240) # x, y, w, h
    display.draw_text(0, 0, 'Welcome', font, Colors.cyan, Colors.black)
    display.draw_text(0, 25, PET_NAME, font, Colors.cyan, Colors.black)
    display.draw_text(0, 200, 'Starting...', font, Colors.grey, Colors.black)

def show_dashboard():
    display.clear(Colors.black)
    display.draw_text(0, 200, 'Fetching...', font, Colors.grey, Colors.black)
    # Request data
    response = requests.post(API+"/register", headers={"X-API-KEY": API_KEY, "Content-Type": "application/json"}, data=ujson.dumps({"pet_name":PET_NAME}))
    data = ujson.loads(response.text)
    response.close()
    # Draw response
    display.draw_image('tamagotchi smile.raw',140,0,180,240) # x, y, w, h
    display.draw_text(0,  0, f"Welcome, {data['pet_name']}", font, Colors.cyan, Colors.black)
    display.draw_text(0, 25, f"Owner:   {data['owner_name']}", font, Colors.cyan, Colors.black)
    display.draw_text(0, 50, f"Pet ID:  {data['pet_id']}", font, Colors.cyan, Colors.black)
    display.draw_text(0, 75, f"Points:  {data['points_balance']}", font, Colors.cyan, Colors.black)

def show_weather():
    display.clear(Colors.black)
    display.draw_text(0, 200, 'Fetching...', font, Colors.grey, Colors.black)
    # Request data
    response = requests.get(API+"/weather", headers={"X-API-KEY": API_KEY})
    print(response.text)
    weather = ujson.loads(response.text)
    response.close()
    # Draw response
    display.draw_text(0, 0, 'Weather forecast', font, Colors.white, Colors.black)
    today = weather[0]
    display.draw_text(0, 25, today['Day'], font, Colors.yellow, Colors.black)
    display.draw_text(0, 50, today['Info'], font, Colors.blue, Colors.black)
    display.draw_text(0, 75, f"Temperature: {today['Max']}", font, Colors.blue, Colors.black)
    display.draw_text(0, 100, f"Rain: {today['Rain']}", font, Colors.blue, Colors.black)
    tmrw = weather[1]
    display.draw_text(0, 125, tmrw['Day'], font, Colors.yellow, Colors.black)
    display.draw_text(0, 150, tmrw['Info'], font, Colors.blue, Colors.black)
    display.draw_text(0, 175, f"Temperature: {tmrw['Max']}", font, Colors.blue, Colors.black)
    display.draw_text(0, 200, f"Rain: {tmrw['Rain']}", font, Colors.blue, Colors.black)

def show_timetable():
    start_dates = {
        (2025,  8, 11): 0,
        (2025, 10, 13): 0,
        (2025, 11, 17): 0,
        (2026,  1,  5): 0,
        (2026,  2, 23): 0,
        (2026,  4, 13): 5
    }
    timetable = [
        ["12 CS", "10 CS", "11 CS", "13 CS", "9 DD 7"],
        ["13 CS HL", "13 CS HL", "7 DD 3", "", "9 DD 1"],
        ["", "9 DD 3" ,"12 CS", "9X2 WB", ""],
        ["11 CS", "", "10 CS", "", "12 CS"],
        ["12 CS", "10 CS", "13 CS", "", "8 DD 2"],
        ["11 CS", "", "13 CS HL", "9 DD 3", ""],
        ["12 CS", "12 CS", "", "10 CS", "11 CS"],
        ["", "7 DD 3", "", "9X2 WB", ""],
        ["13 CS", "9 DD 1", "", "11 CS", "10 CS"],
        ["12 CS", "9 DD 7", "8 DD 2", "", "13 CS"]
    ]
    # Calculate the current day number
    day_number = get_timetable_day(start_dates)
    display.clear(Colors.black)
    display.draw_text(0, 0, f'Your timetable', font, Colors.white, Colors.black)
    classes = ["Period 1","Period 2","Period 3","Period 4","Period 5"]
    for i in range(0, len(timetable[day_number])):
        display.draw_text(0, 25+i*25, classes[i], font, Colors.grey, Colors.black)
        display.draw_text(160, 25+i*25, timetable[day_number][i], font, Colors.pink, Colors.black)
    
def show_meal():
    display.clear(Colors.black)
    display.draw_text(0, 0, 'Eating...', font, Colors.grey, Colors.black)
    # Request data
    response = requests.post(API+"/meal", headers={"X-API-KEY": API_KEY})
    print(response.text)
    data = ujson.loads(response.text)
    response.close()
    # Draw response
    if data['status'] == 'success':
        display.draw_image('tamagotchi exclaim.raw',140,0,180,240) # x, y, w, h
        display.draw_text(0, 0, 'Delicious!!', font, Colors.green, Colors.black)
        display.draw_text(0, 50, f'Balance: {data["points_balance"]}', font, Colors.grey, Colors.black)
    else:
        display.draw_image('tamagotchi frown.raw',140,0,180,240) # x, y, w, h
        display.draw_text(0,  0, 'No food for you :<', font, Colors.red, Colors.black)
        display.draw_text(0, 50, '(pets only need', font, Colors.grey, Colors.black)
        display.draw_text(0, 75, ' a meal once', font, Colors.grey, Colors.black)
        display.draw_text(0,100, ' every 12 hours)', font, Colors.grey, Colors.black)

def show_hello():
    display.clear(Colors.black)
    display.draw_text(0, 0, 'Friendly wave...', font, Colors.grey, Colors.black)

    # Initiate 1st request
    response = requests.post(API+"/hello", headers={"X-API-KEY": API_KEY})
    print(response.text)
    data = ujson.loads(response.text)
    response.close()
    
    if data['status'] == 'acknowledged':
        # Wait 5 seconds to see if someone waves back....
        utime.sleep(5) 

        # Initiate 2nd request
        response = requests.get(API+"/hello-check", headers={"X-API-KEY": API_KEY})
        print(response.text)
        data = ujson.loads(response.text)
        response.close()
    
    # Process outcome
    if data['status'] == 'success':
        display.draw_image('tamagotchi exclaim.raw',140,0,180,240) # x, y, w, h
        display.draw_text(0, 0, 'Yay !!!               ', font, Colors.green, Colors.black)
        display.draw_text(0, 50, f'{data["responder"]} ', font, Colors.green, Colors.black)
        display.draw_text(0, 75, f'waved back!!        ', font, Colors.green, Colors.black)
    elif data['status'] == "no responses":
        display.draw_image('tamagotchi frown.raw',140,0,180,240) # x, y, w, h
        display.draw_text(0, 0,  'Boo hoo....  ', font, Colors.red, Colors.black)
        display.draw_text(0, 50, 'Noone wanted ', font, Colors.red, Colors.black)
        display.draw_text(0, 75, 'to wave.     ', font, Colors.red, Colors.black)

def show_prs():
    display.clear(Colors.black)
    display.draw_text(0, 0, 'Paper rock scissors!', font, Colors.white, Colors.black)

    # Initiate 1st request
    response = requests.post(API+"/prs", headers={"X-API-KEY": API_KEY})
    print(response.text)
    data = ujson.loads(response.text)
    response.close()
    
    if data['status'] == "waiting for opponent":

        # Wait 5 seconds to see if someone plays back....
        utime.sleep(5) 

        # Initiate 2nd request
        response = requests.get(API+"/prs-check", headers={"X-API-KEY": API_KEY})
        print(response.text)
        data = ujson.loads(response.text)
        response.close()
    
    # Process outcome
    if data['status'] == 'match':
        if data['result'] == 'win':
            display.draw_image('tamagotchi exclaim.raw',140,0,180,240) # x, y, w, h
            display.draw_text(0, 0, 'YOU WIN !!', font, Colors.green, Colors.black)
            display.draw_text(0, 50, f"You chose {data['your_choice']}", font, Colors.white, Colors.black)
            display.draw_text(0, 75, f"against {data['opponent']}", font, Colors.white, Colors.black)
            display.draw_text(0,100, f"who chose {data['their_choice']}", font, Colors.white, Colors.black)
        elif data['result'] == 'lose':
            display.draw_image('tamagotchi frown.raw',140,0,180,240) # x, y, w, h
            display.draw_text(0, 0, 'YOU LOSE !!', font, Colors.red, Colors.black)
            display.draw_text(0, 50, f"You chose {data['your_choice']}", font, Colors.white, Colors.black)
            display.draw_text(0, 75, f"against {data['opponent']}", font, Colors.white, Colors.black)
            display.draw_text(0,100, f"who chose {data['their_choice']}", font, Colors.white, Colors.black)
        else: # tie
            display.draw_image('tamagotchi meh.raw',140,0,180,240) # x, y, w, h
            display.draw_text(0, 0, 'A TIE !!!', font, Colors.yellow, Colors.black)
            display.draw_text(0, 50, f"You chose {data['your_choice']}", font, Colors.white, Colors.black)
            display.draw_text(0, 75, f"against {data['opponent']}", font, Colors.white, Colors.black)
            display.draw_text(0,100, f"who chose {data['their_choice']}", font, Colors.white, Colors.black)
    else:
        display.draw_image('tamagotchi frown.raw',140,0,180,240) # x, y, w, h
        display.draw_text(0, 0, 'Boo hoo....', font, Colors.red, Colors.black)
        display.draw_text(0, 50, 'Noone played :<', font, Colors.red, Colors.black)

def show_buttons(left,right):
    display.fill_rectangle(0, 200, 319, 39, Colors.grey)
    display.draw_text(0, 200, f' {left.upper()} ', font, Colors.white, Colors.blue)
    display.draw_text(160, 200, f' {right.upper()} ', font, Colors.white, Colors.blue)

def show_error(message):
    display.clear(Colors.red)
    display.draw_text(0, 0, 'Error!', font, Colors.yellow, Colors.red)
    display.draw_text(0, 25, "Sorry, I'm stuck", font, Colors.yellow, Colors.red)
    display.draw_text(0, 100, message, font, Colors.white, Colors.red)
    print("[ERROR] Stuck. Can not continue: ",message)
    import sys
    sys.exit()

def hibernate():
    backlight.off()
    while not screen.pressed:
        utime.sleep(5)
        led.green()
        utime.sleep(0.2)
        led.off()
    screen.getpress()
    backlight.on()
    

#########################################################
## Main code starts here
#########################################################

show_welcome()
wifi = WIFI(NETWORKS)
ip = wifi.connect()
if not ip:
    show_error("No Internet!")

show_dashboard()
current = "Dashboard"
show_buttons(current,"Next")
last_activity = utime.time()
while True:    
    if screen.pressed:
        last_activity = utime.time()
        x,y = screen.getpress()
        print(f"Press detected. current={current} x={x} y={y}")
        if x > 160: # right click
            if current=="Dashboard":
                current="Weather"
            elif current=="Weather":
                current="Timetable"
            elif current=="Timetable":
                current="Meal"
            elif current=="Meal":
                current="Hello"
            elif current=="Hello":
                current="Paper rock scissors"
            else:
                current="Dashboard"
            show_buttons(current,"Next")
        else: # left click
            if current=="Dashboard":
                show_dashboard()
                show_buttons(current,"Next")
            elif current=="Weather":
                show_weather()
                show_buttons(current,"Next")
            elif current=="Timetable":
                show_timetable()
                show_buttons(current,"Next")
            elif current=="Meal":
                show_meal()
                show_buttons(current,"Next")
            elif current=="Hello":
                show_hello()
                show_buttons(current,"Next")
            elif current=="Paper rock scissors":
                show_prs()
                show_buttons(current,"Next")
    if utime.time()-last_activity > 120: # 2 minutes inactivity:
        hibernate()
        last_activity = utime.time()
    utime.sleep(0.01)




