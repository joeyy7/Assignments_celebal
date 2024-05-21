# WAP to create a web crawler.
import re
import requests # need to import this module, used to fetch content from webpage
from collections import Counter


url = 'http://www.poornima.org/'  

#extract HTML content
response = requests.get(url)
html_content = response.text

# extract <a> tag hyperlinks
hyperlinks = re.findall(r'<a[^>]+href="([^"]+)"', html_content)

valid_links = [
    link for link in hyperlinks 
    if re.match(r'^(https?://|/)', link) and not re.match(r'^(tel:|javascript:|/)$', link)
]

# frequency of all links
link_counts = Counter(valid_links)

sorted_links = link_counts.most_common()

for link, count in sorted_links:
    print(f'{link}: {count}')
