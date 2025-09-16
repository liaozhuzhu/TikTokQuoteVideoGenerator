# TikTok Quote Bot Generator

Entire process (besides upload) is done automatically.

## Motivation 

I see thousands of videos across TikTok that simply have 3 things: music, a video background, and an inspiring quote. After watching [Coding With Lewis](https://www.youtube.com/watch?v=3gjcY_00U1w),
I was inspired to try making one of these bots on my own.

## Disclaimers

This bot does not upload to TikTok automatically in order to stay in line with community guidelines (and I found it very difficult to implement the process with Selenium)

## Running on your own

1. Clone this repository
2. Run `pip install -r requirements.txt`
3. Follow [this link](https://www.imagemagick.org/script/download.php)
4. Download music & videos and store them in directories named: "music" & "videos" **These names are strict**
5. Fetch quotes (default) or create your own texts
6. Run `python3 app.py`
7. Wait for "final.mp4" file to be created
8. Play "final.mp4" in QuickTime or VLC Media Player

## How it works

1. A quote from [ZenQuotes](https://zenquotes.io/api) is randomly selected from their api
2. A video & song is randomly selected from my vast list of downloaded files
3. These 3 things are compiled together into a single mp4 file (named "final.mp4") using Moviepy
4. The caption is then copied to your clipboard using pyperclip for ease of upload
5. That's literally it
6. **01/12/2023 Update**: The bot now generates 5 videos ("final0.mp4" - "final4.mp4") so the user can choose between multiple videos to upload. Thank you [@jerseymason](https://github.com/jerseymason) for issuing the idea.

## Statistics (11/27/2022)

- There are 776880 possible combinations of videos that can be made (note there are only 240 possible video/music combinations)
- Averages 74.14 views per video
