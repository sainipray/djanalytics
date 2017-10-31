import bs4
import requests


def get_object(url):
    res = requests.get(url)
    res.raise_for_status()
    return bs4.BeautifulSoup(res.text, 'html.parser')


def get_latest_questions():
    soup = get_object('http://stackoverflow.com')
    latest_questions = soup.select('.question-summary > div.summary > h3 > a')
    users = soup.select('.question-summary > div.summary > div.started > a:nth-of-type(2)')
    status = soup.select('.question-summary > div.summary > div.started > a.started-link')
    latest_questions = map(lambda x: x.text.strip(), latest_questions)
    users = map(lambda x: x.text.strip(), users)
    status = map(lambda x: x.text.strip(), status)
    return {'data': zip(latest_questions, users, status), 'keys': ('Latest Question', 'Users', 'Status')}


def get_popular_tags():
    soup = get_object('https://stackoverflow.com/tags')
    tags = soup.select('#tags-browser .post-tag')
    counts = soup.select('#tags-browser span.item-multiplier-count')
    tags = map(lambda x: x.text.strip(), tags)
    counts = map(lambda x: x.text.strip(), counts)
    return {'data': zip(tags, counts), 'keys': ('Tag Name', 'Count')}


def get_top_users():
    soup = get_object('https://stackoverflow.com/users?tab=Reputation&filter=all')
    users = soup.select('#user-browser .user-details > a')
    reputation = soup.select('#user-browser .user-details .reputation-score')
    users = map(lambda x: x.text.strip(), users)
    reputation = map(lambda x: x.text.strip(), reputation)
    return {'data': zip(users, reputation), 'keys': ('User', 'Reputation')}


def get_top_users_of_tag(tagname):
    soup = get_object('https://stackoverflow.com/tags/' + tagname + '/topusers')
    users = soup.select('#questions div.fl')[1].select('.user-details a')
    point = soup.select('#questions div.fl')[1].select('tr')
    users = map(lambda x: x.text.strip(), users)
    point = map(lambda x: x.text.strip().split('\n')[0], point)
    return {'data': zip(users, point), 'keys': ('User', 'Points')}
