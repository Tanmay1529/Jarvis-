import operator
import pyautogui
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import requests
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import time
import pyjokes
import speedtest
import psutil
import bs4
import instaloader
import twilio
from bs4 import BeautifulSoup
# from pypdf import PdfReader
from oauthlib.uri_validate import query


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0])

# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# Convert voice to text
def takecmd():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout = 3, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        # speak("Say that again Please...")
        return "none"
    query = query.lower()
    return query

# to Wish
def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour >= 0 and hour <= 12:
        speak(f"Good Morning Tanmay, its {tt}")
    elif hour > 12 and hour <= 16:
        speak(f"Good Afternoon Tanmay, its {tt}")
    elif hour > 16 and hour <= 21:
        speak(f"Good Evening Tanmay, its {tt}")
    else:
        speak(f"Good Night Tanmay, its {tt}")
    speak("I am Ramu Kaka. Please tell me how can I help you")

def news():
    main_url = 'https://newsapi.org/v2/everything?q=tesla&from=2025-02-04&sortBy=publishedAt&apiKey=c5cefa43ba174b28bc6fa96239db4fbf'
    main_page = requests.get(main_url).json()
    articles = main_page['articles']
    head = []
    day = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")

# def read_pdf():
#     book = open('Verity-by-Colleen-Hoover.pdf', 'rb')
#     pdf_reader = pypdf.PdfReader(book)
#     pages = pdf_reader.numPages
#     speak(f"Total number of pages in this book {pages}")
#     speak(f"Please Enter the page number I have to read: ")
#     pg = int(input("Please enter the page number: "))
#     page = pdf_reader.getPage(pg)
#     text = page.extractText()
#     speak(text)

def get_operator_fn(op):
    return {
        '+' : operator.add,
        '-' : operator.sub,
        '*' : operator.mul,
        '/' : operator.truediv,  # Fix operator for division
    }.get(op, None)  # Default to None if the operator is invalid

def eval_binary_expr(op1, oper, op2):
    op1, op2 = int(op1), int(op2)
    return get_operator_fn(oper)(op1, op2)

def listen_and_calculate():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Say what you want to calculate, example: 3 plus 3 is 6")
        print("listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    my_string = r.recognize_google(audio)
    print(my_string)

    my_string = my_string.replace("plus", "+").replace("minus", "-").replace("times", "*").replace("divided by", "/")

    # Split the input into operands and operator
    parts = my_string.split()

    if len(parts) == 3:
        op1, oper, op2 = parts
        result = eval_binary_expr(op1, oper, op2)
        speak(f"Result is: {result}")
    else:
        speak("I couldn't understand the equation. Please try again.")

# def get_weather(city):
#     # Create URL for the search
#     url = f"https://www.google.com/search?q=weather+{city}"
#
#     # Adding headers to simulate a request from a browser
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
#     }
#
#     # Making the request to Google
#     html = requests.get(url, headers=headers).content
#
#     # Parsing the HTML content
#     soup = BeautifulSoup(html, 'html.parser')
#
#     # Extracting the temperature with error handling
#     temp_tag = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'})
#     temp = temp_tag.text if temp_tag else "Not found"
#
#     # Extracting the time and sky description with error handling
#     str_tag = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'})
#     if str_tag:
#         str_ = str_tag.text
#         data = str_.split('\n')
#         time = data[0]
#         sky = data[1] if len(data) > 1 else "Not available"
#     else:
#         time = "Not found"
#         sky = "Not found"
#
#     # Extracting other weather information (like wind speed) with error handling
#     listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
#     if len(listdiv) > 5:
#         strd = listdiv[5].text
#         pos = strd.find('Wind')
#         other_data = strd[pos:] if pos != -1 else "Other data not available"
#     else:
#         other_data = "Other data not available"
#
#     # Returning the weather data
#     return temp, time, sky, other_data

# Example of calling the function for Pune
# city = "pune"
# temp, time, sky, other_data = get_weather(city)

# Printing the extracted weather data
# print(f"Temperature in {city}: {temp}")
# print(f"Time: {time}")
# print(f"Sky Description: {sky}")
# print(f"Other Weather Data: {other_data}")

import speedtest

# def check_internet_speed():
#     st = speedtest.Speedtest()
#
#     # Get best server based on ping
#     st.get_best_server()
#
#     # Measure download and upload speeds
#     download_speed = st.download() / 1_000_000  # Convert from bits to Megabits
#     upload_speed = st.upload() / 1_000_000  # Convert from bits to Megabits
#
#     # Measure ping
#     ping = st.results.ping
#
#     # Speak the results
#     speak(f"Sir, we have {download_speed:.2f} Megabits per second downloading speed and {upload_speed:.2f} Megabits per second uploading speed. The ping is {ping} ms.")


def TaskExecution():
    wish()

    while True:
        query = takecmd().lower()

        # logic building for tasks

        if "open notepad" in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)

        elif "open pycharm" in query:
            ppath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2023.1.3\\bin\\pycharm.exe"
            os.startfile(ppath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            if not cap.isOpened():
                print("Error: Could not open camera.")

            while True:
                ret, img = cap.read()

                # Check if frame is successfully captured
                if not ret:
                    print("Error: Failed to capture image.")
                    break

                # Display the captured frame
                cv2.imshow('webcam', img)

                # Exit the loop if the user presses the 'Esc' key (ASCII value 27)
                k = cv2.waitKey(50)
                if k == 27:  # 27 is the ASCII value for 'Esc' key
                    break

                # Release the camera and close the window
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir = "E:\\Music"
            songs = os.listdir(music_dir)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, songs[0]))

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP Address is {ip}")

        elif "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(result)
            print(result)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open brave" in query:
            webbrowser.open("www.brave.com")

        elif "open linkedin" in query:
            webbrowser.open("www.linkedin.com")

        elif "open google" in query:
            speak("Sir, What should I search on Google?")
            query = takecmd().lower()
            webbrowser.open(f"{query}")

        elif "send whatsapp message" in query:
            kit.sendwhatmsg("+917558223190", "This is testing protocol", 17, 52)

        elif "play song on youtube" in query:
            kit.playonyt("Perfect")

        elif "you can sleep" in query:
            speak("Thanks for using me sir, have a nice day!")
            sys.exit()

        # to close application
        elif "close notepad" in query:
            speak("Okay Sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")

        # to set alarm
        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            if nn == 2:
                music_dir = 'E:\\music'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))

        # to find a joke
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "shut dowm the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "sleep the system" in query:
            os.system("rundll32.exe powerprof.dll,SetSuspendState 0,1,0")

        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "tell me news" in query:
            speak("please wait sir, fetching the latest news")
            news()

        # to find my location using IP Address

        elif "Where I am" in query or "Where we are" in query:
            speak("wait sir let me check")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()

                city = geo_data['city']
                # state = geo_data['state']
                country = geo_data['country']
                speak(f"Sir we are in {city} city of {country} country")

            except Exception as e:
                speak("sorry sir, Due to network issue i am not able to find where we are")
                pass

        elif "take screenshot" in query or "take a screenshot" in query:
            speak("Sir, please tell me the name for this screenshot file")
            name = takecmd().lower()
            speak("please sir hold the screen for few seconds, i am taking screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("I am done sir, the screenshot is saved in our main folder. Now i am ready for next command")

        # elif "read pdf" in query:
        #     read_pdf()

        elif "hide all files" in query or "hide this folder" in query or "visible for everyone" in query:
            speak(f"Want to hide this folder or make it visible for everyone")
            condition = takecmd().lower()
            if "hide" in condition:
                os.system("attrib +h /s /d")
                speak("Sir, all files in this folder are now hidden")

            elif "visible" in condition:
                os.system("attrib -h /s /d")
                speak("Sir, all files are visible to everyone")

            elif "leave it" in condition or "leave for now" in condition:
                speak("Ok sir!")

        # elif "do some calculation" in query or "can you calculate" in query:
        #     r = sr.Recognizer()
        #     with sr.Microphone() as source:
        #         speak("Say what you want to calculate, example 3  plus 3 is 6")
        #         print("listening...")
        #         r.adjust_for_ambient_noise(source)
        #         audio = r.listen(source)
        #     my_string=r.recognize_google(audio)
        #     print(my_string)
        #     def get_operator_fn(op):
        #         return {
        #             '+' : operator.add,
        #             '-' : operator.sub,
        #             '*' : operator.mul,
        #             '-' : operator.__truediv__,
        #         }[op]
        #     def eval_binary_expr(op1, oper, op2):
        #         op1, op2 = int(op1), int(op2)
        #         return get_operator_fn(oper)(op1, op2)
        #     speak("result is")
        #     speak(eval_binary_expr(*(my_string.split())))

        elif "do some calculation" in query or "can you calculate" in query:
            listen_and_calculate()

        elif "hello" in query or "hey" in query:
            speak("Hello Sir, May I help you with something")

        elif "how are you" in query:
            speak("I am fine sir, How are you?")

        elif "I am good" in query or "fine" in query:
            speak("That's great to hear from you Sir")

        elif "thank you" in query or "thanks" in query:
            speak("It's my pleasure sir")

        elif "you can sleep" in query or "sleep now" in query:
            speak("Okay Sir, I am going to sleep. You can call me anytime")
            break

        # elif "temperature" in query:
        #     get_weather()

        elif "how much power left" in query or "battery" in query:
            import psutil
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"sir you system have {percentage} percent battery")
            if percentage >= 80:
                speak("We have enough power to continue our work")
            elif percentage >=50 and percentage < 80:
                speak("I guess we should connect the charger")
            elif percentage >= 30 and percentage < 50:
                speak("We dont have enough power to work, please connect the charger")
            elif percentage <= 20:
                speak("We are running out of power. Please connect the charger as system is going to shutdown")

        # elif "internet speed" in query:
        #     try:
        #         os.system('cmd /k "speedtest"')
        #     except:
        #         speak("there is no internet connection")

        # elif "send message" in query:
        #     speak("What message to send?")
        #     msg = takecmd()
        #
        #     from twilio.rest import Client
        #
        #     account_sid = 'AC5b5db1266cec4c882b016ba0218bced9'
        #     auth_token = '20139823a4d1dd488f4bf162731cfcf9'
        #
        #     client = Client(account_sid, auth_token)
        #
        #     message = client.messages \
        #         .create(
        #             body = msg,
        #             from_ = '+19069702328',
        #             to = '+917558223190'
        #         )
        #     print(message.sid)
        #     speak("Sir, message has been sent")

        elif "volume up" in query:
            pyautogui.press("volumeup")

        elif "volume down" in query:
            pyautogui.press("volumedown")

        elif "mute" in query:
            pyautogui.press("volumemute")

        elif "alarm" in query:
            speak("Sir, please tell me the time to set alarm.")
            tt = takecmd()  # set alarm to 5:30 pm - example
            tt = tt.replace("set alarm to", "")
            tt = tt.replace(".", "")
            tt = tt.upper()
            import MyAlarm
            MyAlarm.alarm(tt)



if __name__ == "__main__":
    while True:
        permission = takecmd()
        if "wake up" in permission:
            TaskExecution()
        elif "goodbye" in permission:
            sys.exit()
            speak("Thanks for using me Sir, Have a good day!")




