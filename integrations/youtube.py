import requests

# search for videos
def search(query):
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": query,
        "key": "" # put your API key here
    }
    response = requests.get(url, params=params)
    return response.json()

    video_id = search_results["items"][0]["id"]["videoId"]






