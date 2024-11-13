import pandas as pd
import json

# yt_list = []
# with open("c:/Users/carso/Desktop/MainRepo/Projects/raw_YT_data.json", 'r') as file:
#     for line in file:
#         yt_list.append(json.loads(line))
#         for item in yt_list:
#             a = item["items"]["snippet"]["title"]
#         print (a)
YT_data = []
yt_list = []
with open("c:/Users/carso/Desktop/MainRepo/Projects/raw_YT_data.json") as f:
    for object in f:
        videodata = json.loads(object)
        yt_list.append(videodata)

for line in yt_list:
    for item in line["items"]:
        title = item["snippet"]["title"]
        vidId = item["id"]
        date = item["snippet"]["publishedAt"]
        chanTitle = item["snippet"]["channelTitle"]
        chanId = item["snippet"]["channelId"]
        views = item["statistics"]["viewCount"]
        comments = item["statistics"]["commentCount"]
        vid_str = (title,date,chanTitle,chanId,views,comments)
        YT_data.append(vid_str)

print(YT_data)
# df = pd.DataFrame(YT_data, columns=["Title","Publication Date","Channel Name","Channel ID","Views","Comments"])

# df.head()
