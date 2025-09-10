import requests
from config import HF_API_KEY, API_URL

api_url = f"{API_URL}"


headers = {
    "Authorization": f"Bearer {HF_API_KEY}"
}


text = "I love this movie! It was fantastic"

response = requests.post(api_url, headers = headers, json={"inputs": text})

if response.status_code == 200:
    result = response.json()
    print("Detected emotions:")
    for emotion in result[0]:
        label = emotion["label"]
        score = emotion["score"]
        print(f"{label}: {score:.4f}")
else:
    print(f"Error: {response.status_code}\nMessage: {response.text}")
