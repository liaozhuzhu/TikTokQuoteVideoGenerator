from moviepy.editor import *
import json, requests, random, os
from random import randint
import pyperclip

def main():  
    
    #get quote
    quote = get_quote()
    text = TextClip(quote, fontsize=40, size=(560, 0), color="white", kerning=2, font="Verdana-Bold", method='caption', stroke_color="black", stroke_width=2) #set textclip to quote
     
    #get clip 
    randomClip = get_video()
    videoclip = VideoFileClip(f"videos/{randomClip}").subclip(0, 8) #set videoclip to random video
    
    #get audio
    randomAudio = get_audio()
    audioclip = AudioFileClip(f"music/{randomAudio}") #set audioclip to random music
    
    #get final
    get_final(videoclip, audioclip, text)
    
    #get caption
    pyperclip.copy('#fyp #motivation #quote #python #code #phonk') #set caption hashtags
    print("Caption copied to clipboard!") #verify caption has been copied
    
def get_quote():
    randomInt = randint(0, 49) #generate random int for quote
    response = requests.get("https://zenquotes.io/api/quotes/") #fetch quotes
    r = response.json() #parse quotes
    quote = r[randomInt]['q'] #set quote
    return quote #return quote

def get_video():
    randomClip = random.choice(os.listdir("videos")) #select random video from "./videos"
    while (randomClip == ".DS_Store"): #make sure file isn't .DS_Store (probably a better way to handle this)
        randomClip = random.choice(os.listdir("videos")) #set random video
    return randomClip #return video

def get_audio():
    randomAudio = random.choice(os.listdir("music")) #select random music from "./music"
    while (randomAudio == ".DS_Store"): #make sure file isn't .DS_Store (probably a better way to handle this)
        randomAudio = random.choice(os.listdir("music")) #set random video
    return randomAudio #return video

def get_final(videoclip, audioclip, text):
    finalclip = CompositeVideoClip([videoclip, text.set_pos("center")]).set_duration(8) #set final video duration to 8s
    finalclip = finalclip.set_audio(audioclip).set_duration(8) #set video audio and duration to 8s
    finalclip = finalclip.resize((1080, 1920)) #set video width, height
    finalclip.write_videofile("final.mp4", temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac") #compiles/writes file 'final.mp4'
    
    
if __name__ == "__main__":
	main()