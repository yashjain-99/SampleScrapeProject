# beautiful-soup code to extract data from a website
import requests
from bs4 import BeautifulSoup
import re
import json
from tqdm import tqdm
final = []
err = []
selected_topics = ['computer-vision', 'etl', 'nlp', 'data-science', 'sql']
for topic in tqdm(selected_topics):
    source = requests.get(f'https://medium.com/tag/{topic}/top/all-time').text
    soup = BeautifulSoup(source, 'lxml')
    c = 0
    for article in soup.find_all('article'):
        temp = {}
        if c < 9:
            try:
                headline = article.find(
                    'a', attrs={"aria-label": "Post Preview Title"}).div.h2.text
                link = article.find(
                    'a', attrs={"aria-label": "Post Preview Title"})['href']
                link = link.split('/')[2]
                link = link.split('?')[0]
                link = 'https://towardsdatascience.com/'+str(link)
                author_name = article.find(
                    'a', class_='ae af ag ah ai aj ak al am an ao ap aq ar as').text

                pattern = re.compile(
                    r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|January|February|March|April|May|June|July|August|September|October|November|December)\s[0-3]?[0-9],\s\d{4}')
                matches = pattern.search(article.text)
                post_date = matches.group(0)

                read_time = article.find(
                    'a', attrs={"aria-label": "Post Preview Reading Time"}).text

                soup_temp = BeautifulSoup(requests.get(link).text, 'lxml')
                author_follower = soup_temp.find_all(
                    'span', class_=['pw-follower-count', 'bd', 'b', 'fh', 'fi', 'dw'])[-1].text

                tags = []
                for b in soup_temp.find_all('div', attrs={"class": ['nl', 'di', 'dt', 'nm', 'nn', 'no', 'bd', 'b ', 'be', 'z ', 'bi', 'np']}):
                    if len(b.get('class')) == 12:
                        tags.append(b.text)

                foot = soup_temp.find('footer')
                ps = foot.find_all('p')
                comments = ps[2].text

                temp['topic_name'] = topic
                temp['topic_best_all_time_url'] = f'https://medium.com/tag/{topic}/top/all-time'
                temp['post_title'] = headline
                temp['post_link'] = link
                temp['author_name'] = author_name
                temp['post_date'] = post_date
                temp['read_time'] = read_time
                temp['author_follower_count'] = author_follower
                temp['post_tags'] = list(set(tags))
                temp['post_clap_count'] = 'NA'
                temp['post_comment_count'] = comments
                final.append(temp)
                c += 1
            except Exception as e:
                print(e)
                pass
        else:
            break
with open('data.json', 'w') as outfile:
    json.dump(final, outfile,  indent=4, separators=(',', ': '))
