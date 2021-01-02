import requests
import config
url = "https://api.yelp.com/v3/businesses/search"

headers = {
    "Authorization": "Bearer " + config.api_key
}
params = {
    "term": "Starbucks",
    "location": "NYC",
}
response = requests.get(url, headers=headers, params=params)
businesses = result = response.json()["businesses"]
# print(businesses)
alias = [business["alias"]
         for business in businesses if business["rating"] >= 2.0]
print(alias)
# for business in businesses:
#     print(business["name"])
