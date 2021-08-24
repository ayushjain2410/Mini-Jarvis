import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

# pyttsx3 module needed to make computer speak what we want computer to speak
# speech_Recognition module is needed for recognition of user's voice from microphone
# wikipedia module is used to search the data we would like to search
# web browser is inbuilt module used for opening platforms on google
# os is for directory module used to play music directory if we want to
# smtplib is used for sending email through gmail

engine = pyttsx3.init('sapi5')
# this is used for taking voices from microsoft
voices = engine.getProperty('voices')
# now voices is the list containing all the default voices it has
# voices[0] =david male voice voices[1]=zara =female voice
engine.setProperty('voice', voices[0].id)
# setting david voice for the program


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    # to make computer speak and remain speaking until fully spoken one time


def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("good morning ")
    elif 12 <= hour <= 18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("i am jarvis sir. please tell me how can i help you.")


def takecommand():
    # it takes microphone input from user and return string output
    r = sr.Recognizer()
    # recognizer will help us in recognizing the voice
    with sr.Microphone() as source:
        # will consider microphone as a source input of user's voice
        print("listening ...")
        r.pause_threshold = 1
        # prevent from stop listening if user stops in between while speaking for 1 sec
        audio = r.listen(source)
        # capturing our audio from microphone

        try:
            print("recognizing ...")
            query = r.recognize_google(audio, language='en-in')
            # converting audio into string format with laguage =english
            print(f"user said :{query}\n")
        except Exception as e:
            # print(e)
            print("say that again please... ")
            return "None"
        # if system cannot understand what we are saying it return none
    return query

def sendEmail(to,content):
    server= smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("youremailid","yourpassword")
    server.sendemail("youremailid",to,content)
    server.close()


if __name__ == '__main__':
    wishme()
    while True:

        query = takecommand().lower()
        # query will be the audio message of user in string format

        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("searching wikipedia ...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia ...")
            print(results)
            speak(results)


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


        elif "play music" in query:
            music_dir = "your music direcgory path"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            # will play 1st song


        elif "the time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strtime}")

        #opening different files
        elif "open code" in query :
            codepath="paste editor path"
            os.startfile(codepath)

        #sending email
        elif "email to yourname" in query:
            try:
                speak("what should i say")
                content = takecommand()
                to = "reciever mail id"
                sendEmail(to, content)
                speak("email has been sent")
            except Exception as e :
                print(e)
                speak("sorry i cannot send this email at the moment")




