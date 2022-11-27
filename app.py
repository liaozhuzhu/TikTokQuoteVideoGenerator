from moviepy.editor import *
import json, requests, random, os
from random import randint
import pyperclip

#/Users/liaozhu/cs-projects/quotebot/virt/bin/python3

def main():  
    quote = get_quote()
    text = TextClip(quote, fontsize=40, size=(560, 0), color="white", kerning=2, font="Verdana-Bold", method='caption', stroke_color="black", stroke_width=2)
    
    # set clip 
    randomClip = get_video()
    videoclip = VideoFileClip(f"videos/{randomClip}").subclip(0, 8)
    
    # set audio
    randomAudio = get_audio()
    audioclip = AudioFileClip(f"music/{randomAudio}")
    
    # set final
    finalclip = CompositeVideoClip([videoclip, text.set_pos("center")]).set_duration(8)
    finalclip = finalclip.set_audio(audioclip).set_duration(8)
    finalclip = finalclip.resize((1080, 1920))
    finalclip.write_videofile("final.mp4", temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")
    pyperclip.copy('#fyp #motivation #quote #python #code #phonk')
    print("Caption copied to clipboard!")
    
def get_quote():
    randomInt = randint(0, 49) #generate random int for quote
    response = requests.get("https://zenquotes.io/api/quotes/") #fetch quotes
    r = response.json() #parse quotes
    quote = r[randomInt]['q'] #set quote
    return quote #return quote

def get_video():
    randomClip = random.choice(os.listdir("videos"))
    while (randomClip == ".DS_Store"):
        randomClip = random.choice(os.listdir("videos"))
    return randomClip

def get_audio():
    randomAudio = random.choice(os.listdir("music"))
    while (randomAudio == ".DS_Store"):
        randomAudio = random.choice(os.listdir("music"))
    return randomAudio
    
if __name__ == "__main__":
	main()