import json
import requests

# Replace with your actual API key
api_key = "YOUR_API_KEY"
url = f"https://developer.nps.gov/api/v1/parks?api_key={api_key}&limit=500"

#Make the API request
response = requests.get(url)

# Save the response as a JSON file
with open('nps_parks.json', 'w') as f:
    json.dump(response.json(), f)

print(response.json())