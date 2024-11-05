import googleapiclient.discovery
import varibles
import pandas as pd
import json

# Replace with your actual API key
API_KEY = varibles.key
youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=API_KEY)


with open('c:/Users/carso/Desktop/MainRepo/Data Sci/YT_URLS.txt','r') as IDS_LIST:
    for line in IDS_LIST:
        yt_id = line.split("=")[1]
        request = youtube.videos().list(
            part='snippet,contentDetails,statistics',
            id=yt_id # Replace with the video ID
            )
        alpha = str(request)
        with open('./sample.txt', 'a') as fd:
            fd.write(alpha)
            fd.write("\n")