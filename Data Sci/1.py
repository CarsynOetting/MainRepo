import googleapiclient.discovery
import varibles
import pandas as pd
import json

with open('c:/Users/carso/Desktop/MainRepo/Data Sci/YT_URLS.txt','r') as IDS_LIST:
    for line in IDS_LIST:
        yt_id = line.split("=")[1]
        request = youtube.videos().list(
            part='snippet,contentDetails,statistics',
            id=yt_id # Replace with the video ID
            )
        print(yt_id)