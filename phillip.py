import os
import discord
import requests

search = "q=how+to+jump"
amount = "&num=3"
url = "https://google-search3.p.rapidapi.com/api/v1/search/"

headers = {
    'x-rapidapi-host': "google-search3.p.rapidapi.com",
    'x-rapidapi-key': "cefb669da5msha21fc129025df58p116d34jsn075161051c3a"
    }

response = requests.request("GET", url, headers=headers)


