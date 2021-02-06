import requests

url = "https://alexnormand-dino-ipsum.p.rapidapi.com/"

querystring = {"format":"html","words":"30","paragraphs":"30"}

headers = {
    'x-rapidapi-key': "ee49d8625dmsh18d0f4dce6867afp16814ejsne918a8e68f98",
    'x-rapidapi-host': "alexnormand-dino-ipsum.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
