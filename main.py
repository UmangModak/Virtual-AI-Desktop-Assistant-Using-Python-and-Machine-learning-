import webbrowser
import pyttsx3
import speech_recognition
import requests
from bs4 import BeautifulSoup
import datetime
import os
import pyautogui
import keyword
import random
from plyer import notification
from pygame import mixer
import speedtest

# password protected

for i in range(3):
    a = input("Enter password to open : ")
    pd_file = open("password.txt", "r")
    pd = pd_file.read()
    pd_file.close()
    if (a==pd):
        print("WELCOME SIR ! PLEASE SPEAK [WAKE UP] TO LOAD ME")
        break
    elif (i==2 and a!=pd):
        print("WARNING!! PLEASE WRITE CORRECT PASSWORD")
    elif (i==3 and a!=pd):
        exit()

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[0].id)
print(voices[0])
engine.setProperty("rate", 180)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

        try:
            print("Understanding....")
            query = r.recognize_google(audio, language="en-in")
            print(f"you said :{query}\n")
        except Exception as e:
            print("Say that again")
            return "none"

        return query


def alarm(query):
    timehere = open("alarm.txt", "w")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()

        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

        elif "talk" in query:
            from GreetMe import conversation
            conversation()
        elif "good" in query:
            from GreetMe import conversation1
            conversation1()
        elif "no" in query:
            from GreetMe import conversation2
            conversation2()

        ############### NEW FUNCTION ##############

        elif"change password" in query:
            speak(" what is the new password")
            new_pd = input(" Enter the new password:\n")
            new_pw = open("password.txt","w")
            new_pw.write(new_pd)
            new_pw.close()
            speak("Password Changed sir")
            speak("our new password is {new_pw}")
            exit()

        elif 'arranged my day' in query:
            task = []
            speak("Do you want to clear old tasks ( plz speak YES  or NO)")
            ans=str(input(""))
            if "yes" in ans:
                file = open("task.txt","w")
                file.write(f"")
                file.close()
                my_task = int(input("Enter the number of task :-  "))
                i = 0
                for i in range(my_task):
                    task.append(input("Enter the task :"))
                    file = open("task.txt","a")
                    file.write(f"{i}.{task[i]}\n")
                    file.close()

            elif "no" in ans:
                i = 0
                for i in range(my_task):
                    task.append(input("Enter the task :"))
                    file = open("task.txt", "a")
                    file.write(f"{i}.{task[i]}\n")
                    file.close()

        elif "show  my schedule" in query:
            file = open("task.txt","r")
            content = file.read()
            file.close()
            mixer.init()
            mixer.music.load('D:\\finalyearproject\\music.mp3')
            mixer.music.play()
            notification.notify(
                title = "My Schedule :-",
                message = content,
                timeout = 15

            )

        elif "open " in query:
            query = query.replace("open","")
            query = query.replace("jarvis","")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.sleep(2)
            pyautogui.press("Enter")
# internet speed
        elif "check my network speed" in query:
            wifi = speedtest.Speedtest()
            upload_speed = wifi.upload()/1048576
            download_speed = wifi.download()/1048576
            print("wifi upload speed is ",upload_speed)
            print("wifi download speed is ",download_speed)
            speak(f"wifi upload speed is{upload_speed}")
            speak(f"wifi download speed is {download_speed}")


        elif "recommend a movie" in query:
            import subprocess
            subprocess.run(["streamlit", "run", "movie.py"])



        elif "sports" in query:
            import urllib.request
            import requests
            from bs4 import BeautifulSoup
            from install import get_live_scores
            get_live_scores()


        elif "play rock scissors game" in query:
            from rockpapergame import rock_paper_scissors
            rock_paper_scissors()

        elif "play snake game" in query:
            speak("snake game start")
            from snakegame import game_loop
            game_loop()


#change karna hai isko
        elif "play cricket game " in query:
            speak("cricket game starting....")
            from chessgame import cricket_game
            cricket_game()


        elif "scan port" in query:
            from chessgame import scan_ports

            host_input = input("Enter the website domain or IP address: ")
            speak(host_input)
            start_port = int(input("Enter the start port: "))

            end_port = int(input("Enter the end port: "))

            result = scan_ports(host_input, start_port, end_port)

            print("Port scanning report:")
            for entry in result:
                print(entry)



        #focus mode
        elif "set focus mode" in query:
           from focusmode import block_unblock_website

           website_to_block = input("Enter the website domain to block (e.g., example.com): ")
           start_time_str = input("Enter the start time to block (HH:MM, 24-hour format): ")
           end_time_str = input("Enter the end time to unblock (HH:MM, 24-hour format): ")

           block_unblock_website(website_to_block, start_time_str, end_time_str)
           exit()



























        ################ NEW FUNCTION AREA ABOVE ######


        elif "open " in query:
            from appdata import openappweb

            openappweb(query)


        elif "close " in query:
            from appdata import closingapp

            closingapp(query)


        # youtube control
        elif "pause video" in query:
            pyautogui.press("k")
            speak("video pausing sir ")
        elif "play video" in query:
            pyautogui.press("k")
            speak("video playing sir")

        elif "mute video" in query:
            pyautogui.press("m")
            speak("video mute sir")

        elif "unmute video" in query:
            pyautogui.press("n")
            speak("video unmute sir")

        elif "volume up" in query:
            from keyboard import volumeup

            speak("turning colume up sir")
            volumeup()

        elif "volume down" in query:
            from keyboard import volumedown

            speak("turning colume up sir")
            volumedown()

        # youtube control done

        # songs playing

        elif "play songs" in query:
            speak("playing songs sir ...")
            a = (1, 2, 3, 4)
            b = random.choice(a)

            if b == 1:
                webbrowser.open(
                    "https://www.youtube.com/watch?v=oRZ0cfZ9SeU&list=RDGMEM916WJxafRUGgOvd6dVJkeQ&start_radio=1&rv=YfQ-3d5cFeo")
            elif b == 2:
                webbrowser.open("https://www.youtube.com/watch?v=90r1L3wtIiU")
            elif b == 3:
                webbrowser.open("https://www.youtube.com/watch?v=ZpA12AIvOGE")
            elif b == 4:
                webbrowser.open("https://www.youtube.com/watch?v=r0c1f6XxRQg")

        # News Read
        elif "news" in query:
            from News import newsforme

            newsforme()
        # calculator
        elif "calculate" in query:
            from calculation import Calculators
            from calculation import calci

            query = query.replace("calculate", "")
            query = query.replace("jarvis", "")
            calci(query)


        # sending whatsapp messeage
        elif "whatsapp" in query:
            from Whatsapp import sendmsg

            sendmsg()

        # shutdown system
        elif "shutdown system" in query:
            speak(" are you really want to shutdown ?")
            shutdown = input("Do you want to shutdown ? (yes/no")
            if shutdown == "yes":
                os.system("shutdown /s /t 1")

            elif shutdown == "no":
                break

        elif "set an alarm" in query:
            print("input time : 10 and 10 and 10")
            speak("set the time")
            a = input("please set time :  ")
            alarm(a)
            speak("done sir")









        elif "google" in query:
            from searchin import googlesearch

            googlesearch(query)


        elif "youtube" in query:
            from searchin import youtubesearch

            youtubesearch(query)

        elif "wikipedia" in query:
            from searchin import wikipediasearch

            wikipediasearch(query)

        elif " weather" in query:
            from searchin import weathersearch

            weathersearch(query)

        elif "the time" in query:
            from searchin import timesearch

            timesearch(query)

        elif "reminder for you " in query:
            remindermsg = query.replace("reminder", "")
            remindermsg = query.replace("jarvis", "")
            speak("the reminder for me " + remindermsg)
            remind = open("Reminder.txt", "w")
            remind.write(remindermsg)
            remind.close()

        elif " what is the reminder" in query:
            reminder = open("Reminder.txt", "r")
            speak("the reminder for you is" + reminder.read())




        elif "finally sleep" in query:
            speak("going t sleep , sir")
            exit()
