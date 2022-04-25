import pandas as pd
import pyttsx3
import random

def tell_stories():
    df = pd.read_csv(r"/Users/sachindiilhan/Desktop/Voice_bot/Stories/children_books.csv")
    rand_num = random.randint(1,3268)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    mytext = df['Desc'][rand_num] 
    #mytext = 'Hi manavi puka palanawa '
    newVoiceRate = 100
    engine.setProperty('rate',newVoiceRate)
    engine.say(mytext)
    engine.runAndWait()