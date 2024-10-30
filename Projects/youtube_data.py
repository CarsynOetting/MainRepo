import googleapiclient.discovery
import varibles
import pandas as pd
import json

# Replace with your actual API key
API_KEY = varibles.key
youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=API_KEY)

# yt_url = input("What URL do you want to use?")
# yt_id = yt_url.split('=')[1]

with open('c:/Users/carso/Desktop/MainRepo/Data Sci/YT_URLS.txt','r') as IDS_LIST:
    for line in IDS_LIST:
      yt_id = line.split('=')[1]
      request = youtube.videos().list(
      part='snippet,contentDetails,statistics',
      id=yt_id # Replace with the video ID
      )
      response = request.execute()

      with open('./raw_YT_data.json', 'a') as fd:
         json.dump(response, fd)
         fd.write("\n")
