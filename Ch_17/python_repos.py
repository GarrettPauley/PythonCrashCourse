import requests
from plotly.graph_objs import Bar 
from plotly import offline

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers) 
print(f"Status code: {r.status_code}")
#store API response in a variable 
response_dict = r.json()
print(f"Total repo's: {response_dict['total_count']}")
#process the results 
repo_dicts = response_dict['items'] 
repo_links, stars, labels = [], [], []
print(f"Repositories returned: {len(repo_dicts)}")


for repos in repo_dicts: 
    repo_names= repos['name']
    repo_url = repos['html_url']
    repo_link = f"<a href='{repo_url}'> {repo_names}</a>"
    repo_links.append(repo_link)
    stars.append(repos['stargazers_count'])

    owner = repos['owner']['login']
    description = repos['description']
    label = f"{owner} <br /> {description}"
    labels.append(label)
    

#Visualize the data 

data = [{
    'type': 'bar', 
    'x': repo_links,
    'y': stars,
    'hovertext': labels, 
    'marker': { 
        'color': 'rgb(60,100,150)', 
        'line': {'width': 1.5, 'color': 'rgb(25,25,25)'}

    }, 
    'opacity': 0.6, 
}]

my_layout = {
    'title': "The Most Popular Python Projects on Github",
    'xaxis': {
        'title': 'Repository', 
        'titlefont': {'size': 24}, 
        'tickfont': {'size': 14},
    
    } ,
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
        } ,
    

}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename = 'python_repos.html') 
