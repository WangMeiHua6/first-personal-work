import requests
import re
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}

comment = []
comments = []
data = '1613672133105'
cursor = '0'

for i in range(0, 1268):
    url = 'https://coral.qq.com/article/5963120294/comment/v2?callback=_article5963120294commentv2&orinum=10&oriorder=o&pageflag=1&cursor=' + cursor + '&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=1&_=' + data
    source = requests.get(url, headers=headers).content.decode()
    comment = re.findall('content":"(.*?),"', source, re.S)
    comments.append(comment)
    id = '"last":"(.*?)"'
    cursor = re.compile(id, re.S).findall(source)[0]
    data = str(int(data) + 1)

with open('comments.json', 'a', encoding='utf-8') as f:
    f.write(json.dumps(comments, indent=2, ensure_ascii=False))
    print(comments)