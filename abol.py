
import requests
import bs4


def abol_filter(item):
    words = item[1].split(' ')
    if len(words) > 5
    print(len(words))


def abol_search(url,size):
    try:
        # Get the request data as an object
        res = requests.get(url)
        # print(res.text)
        soup = bs4.BeautifulSoup(res.text, 'lxml')
        # print(type(soup))
        # Parent table
        table = soup.find('table', class_='itemlist')
        # Children tr
        tds1 = table.find_all('td', class_='title')
        tds2 = table.find_all('td', class_='subtext')
        #print(len(tds2))
        # Data
        raw_data = []
        x = 0
        for i in range(0, size):
            item = []
            # print(tds1[x].text)
            # print(tds1[x+1].text)
            item.append(tds1[x].text)
            item.append(tds1[x+1].text)
            x = x + 2
            # Score
            span = tds2[i].find('span', class_='score')
            # Commetns
            links = tds2[i].find_all('a')
            comment = links[3].text
            item.append(span.text)
            item.append(comment)
            # Add data
            raw_data.append(item)

        #print(raw_data)
        return raw_data

    except Exception as e:
        print(e)



if __name__ == "__main__":
    data = abol_search('https://news.ycombinator.com/',30)
    filter_data = map(abol_filter,data)
    print(list(filter_data))