import requests
from constants import BACKEND_HOST


def fetch_top_wines(limit=10):
    url = BACKEND_HOST + "top-wines?limit=" + str(limit)

    try:
        response = requests.get(url)
        response.raise_for_status()
        print(response.json())
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching wines from backend: {e}")
        return 'Wines not available'


def fetch_most_recent_wines(limit=10):
    url = BACKEND_HOST + "most-recent-wines?limit=" + str(limit)

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching wines from backend: {e}")
        return 'Wines not available'


def fetch_least_recent_wines(limit=10):
    url = BACKEND_HOST + "least-recent-wines?limit=" + str(limit)

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching wines from backend: {e}")
        return 'Wines not available'
