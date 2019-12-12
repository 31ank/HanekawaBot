import requests

def wikipedia(keyword):
    r = requests.get("https://en.wikipedia.org/w/api.php?action=opensearch&search=" + keyword)
    if(r.status_code != 200):
        return ""
    result = r.json()
    if result[2][0] != "":
        return str(result[2][0])
    else:
        return ""