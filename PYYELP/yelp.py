import requests
import config


url = "https://api.yelp.com/v3/businesses/search"

headers = {
    "Authorization" : "Bearer " + config.api_key
}

params = {
    "term": "Barber",
    "location": "NYC"
}
response = requests.get(url, headers=headers, params=params)
businesses = response.json()["businesses"]
names = [business["name"] for business in businesses if business["rating"] > 4.5] 
for name in names:
    print(name)
#PS C:\Users\kirki\CODING_PROJECTS\python_Practice\PYYELP> pipenv shell
#always save the file yelp.py when a new line of code or change in code is put in
#PS C:\Users\kirki\CODING_PROJECTS\python_Practice\PYYELP> pipenv run python yelp.py