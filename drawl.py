import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin
import sys
num = 0
sys.setrecursionlimit(30000)  # 将默认的递归深度修改为30000
visited_pages = []
queuepage = []
def save_page_text(text, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)

def crawl_pages():
    try:
        global visited_pages,num,queuepage
        url = queuepage.pop(0)
        page_response = requests.get(url)
        if page_response.status_code == 200:
            page_soup = BeautifulSoup(page_response.content, 'html.parser')
            page_text = page_soup.get_text(separator='\n')
            page_id = len(visited_pages)
            filename = os.path.join('xmu_pages', f'{page_id}.txt')
            save_page_text(page_text, filename)
            print(f'Saved page {page_id}: {url}')
            visited_pages.append(url)            # 将当前页面添加到已访问列表中
            links = page_soup.find_all('a')      # 递归爬取页面中的链接
            num += 1
            for link in links:
                href = link.get('href')
                if href and not href.startswith('javascript:'):  # 排除以 "javascript:" 开头的链接
                    full_url = urljoin(url, href)
                    if(full_url[-1]=='/'):
                        full_url=full_url[0:-1]
                        full_url.replace('https','http')
                    if full_url not in visited_pages and full_url not in queuepage:
                        if 'xmu.edu.cn' in full_url and 'zip' not in full_url and'j. issn1000'not in full_url \
                        and '#0' not in full_url and 'mp4' not in full_url and'jpg' not in full_url  and 'ppt' not in full_url \
                        and 'aspx' not in full_url and 'english'not in full_url and 'oversea-auth' not in full_url and 'info' not in full_url \
                        and  'Download' not in full_url and 'pdf' not in full_url and 'doc' not in full_url and'#main-content'not in full_url \
                        and '@' not in full_url and 'xls'not in full_url and 'rar'not in full_url:
                            queuepage.append(full_url)
            while len(queuepage)>0 and len(visited_pages) < 8000:
                crawl_pages()
    except requests.exceptions.RequestException as e:
        print(f'Error occurred while requesting page: {url}\n{str(e)}')

url = 'http://www.xmu.edu.cn'
queuepage.append(url)
if not os.path.exists('xmu_pages'):
    os.makedirs('xmu_pages')
crawl_pages()
with open('lianjie.txt', 'w') as file:
    for string in visited_pages:
        file.write(string + '\n')
