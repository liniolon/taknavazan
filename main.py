from lxml import html
import requests


COUNTER = 53
END = 53

my_session = requests.session()
for_cookies = my_session.get("https://taknavazi.com")
cookies = for_cookies.cookies
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'}

while COUNTER <= END:
    print(f"########   PAGE  {COUNTER}  ######")
    URL = 'https://taknavazi.com/tag/%D8%AF%D8%A7%D9%86%D9%84%D9%88%D8%AF-%D8%A2%D8%B1%D8%B4%DB%8C%D9%88-%DA%A9%D8%A7%D9%85%D9%84-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87-%D8%AA%DA%A9%D9%86%D9%88%D8%A7%D8%B2%D8%A7%D9%86/page/{}/'.format(COUNTER)
    page = requests.get(URL, headers=headers, cookies=cookies)
    
    doc = html.fromstring(page.text)
    
    get_links = doc.xpath(
        '//*/h2[@class="post-box-title"]/a/@href')
    
    for l in get_links:
        page = requests.get(l, headers=headers, cookies=cookies)

        doc = html.fromstring(page.text)

        get_links = doc.xpath(
            '//*/div[@class="entry"]/h5/a/@href')

        
        if len(get_links) > 0:
            f = open('link.txt', 'a')
            f.write(get_links[0] + "\n")
            f.close()

            print("Add new link >>> ", get_links[0])

    COUNTER += 1
