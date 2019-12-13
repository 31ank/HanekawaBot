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

def redditreq(subreddit, mode = "rising"):
    r = requests.get("https://www.reddit.com/r/" + subreddit + "/" + mode + ".json?limit=1", headers={'User-agent': 'HanekawaBot'})
    result = r.json()
    answer = []
    answer.append(result['data']['children'][0]['data']['title'])
    answer.append(result['data']['children'][0]['data']['url'])
    return answer