import requests
from config import API_URL

def fetch_episodes(page, on_complete):
    episodes = []
    try:
        response = requests.get(API_URL, timeout=15)
        if response.status_code == 200:
            new_data = response.json()
            if isinstance(new_data, dict) and "data" in new_data:
                episodes = new_data["data"]
            elif isinstance(new_data, list):
                episodes = new_data

            if page.data is None:
                page.data = {}
            page.data["episodes_cache"] = episodes

    except Exception as err:
        print(f"Fetch error: {err}")
        if isinstance(page.data, dict) and "episodes_cache" in page.data:
            episodes = page.data["episodes_cache"]

    # ส่งผลลัพธ์คืน callback
    on_complete(episodes)