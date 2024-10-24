# Tracking for that one project in Coursera

# I have no idea what this was for - I'm guessing the capstone. May delete later - 10/24/24


#--IMPORT SECTION--
import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import ssl

serviceurl = input("What is the URL you wish to pull from?")

#If we find a default website for testing later, we can use this (REPLACE TESTING.COM):
# if len(serviceurl) < 1:
#     serviceurl = "testing.com"

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE