
import requests
import config

url = "https://api.yelp.com/v3/businesses/search"

headers = {
    "Authorization": "Bearer " + config.api_key
}
params = {
    "term": "Nail salon",
    "location": "Chicago"
}
response = requests.get(url, headers=headers, params=params)
# to store results in dictionary:
businesses = response.json()["businesses"]

# for business in businesses:
#     print(business["name"])

# to pick by rating:
names = [business["name"]
         for business in businesses if business["rating"] > 4.5]
print(names)
