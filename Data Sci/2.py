def YT_id_extract(URL):
        file = open(URL,"r")
        for line in file:
            yt_id = line.split('=')[1]
            with open("YT_VID_IDS.txt","a") as file:
                  file.write(yt_id)

location = input("What file do you want to use? ")
if len(location) < 1:
      location = 'c:/Users/carso/Desktop/MainRepo/Data Sci/YT_URLS.txt'

YT_id_extract(location)
