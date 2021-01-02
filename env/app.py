import requests
response = requests.get("https://api.yelp.com/v3/businesses/search")
print(response)
