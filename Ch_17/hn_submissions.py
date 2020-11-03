import json 
from operator import itemgetter
import requests 

#Make an API call and store the response. 
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url) 
print(f"status Code: {r.status_code}")

#process each submission 
submission_ids = r.json()
submission_dicts = [] 
for submission_id in submission_dicts[:30]: 
    #Make a separate API call for each submission. 
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    #Build a dictionary with each article 
    submisson_dict = {
        'title': response_dict['title'], 
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}", 
        'comments': response_dict['descendants'], 
    }
    submission_dicts.append(submisson_dict)

    submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

for dicts in submission_dicts: 
    print(f"\ntitle: {submisson_dict['title']}")
    print(f"Discussion Link: {submisson_dict['hn_link']}")
    print(f"Comments: {submisson_dict['comments']}")
