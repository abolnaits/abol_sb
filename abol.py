
import requests
import bs4

'''
Filter a set of data if the title has more than 5 words
'''
def abol_filter_more(item):
    words = item[1].split(' ')
    return len(words) > 5

'''
Filter a set of data if the title has less or  5 words
'''
def abol_filter_less(item):
    words = item[1].split(' ')
    return len(words) <= 5

'''
Function that use the points in the list 
as key in the sort() function
'''
def order_points(elem):
    return elem[2]

'''
Function that use the comments  in the list 
as key in the sort() function
'''
def order_comments(elem):
    return elem[3]

'''
Make a http request to a new url and return the a list with
the defined size
Return: list 
'''
def abol_search(url,size):
    try:
        # Get the request data as an object
        res = requests.get(url)
        soup = bs4.BeautifulSoup(res.text, 'lxml')
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
            item.append(tds1[x].text)
            item.append(tds1[x+1].text)
            x = x + 2
            # Score
            span = tds2[i].find('span', class_='score')
            # Commetns
            links = tds2[i].find_all('a')
            comment = links[3].text
            #Get the points as int
            list_span = span.text.split(' ')
            if len(list_span) == 2:
                item.append(int(list_span[0]))
            else:
                item.append(0)
            #Get the comments as int
            list_comm = comment.split('\xa0')
            if len(list_comm) == 2:
                item.append(int(list_comm[0]))
            else:
                item.append(0)
            
            # Add data to the main list
            raw_data.append(item)

        return raw_data

    except Exception as e:
        print(e)



'''
Main section
'''
if __name__ == "__main__":
    data = abol_search('https://news.ycombinator.com/',30)
    filter_data = filter(abol_filter_more,data)
    list_data = list(filter_data)
    #More than 5 words and order  by comments
    list_data.sort(reverse=True,key=order_comments)
    print('\nMore than 5 words and order  by comments\n')
    for i in list_data:
        print(i[0],i[1],i[2],'points',i[3],'comments')

    filter_data = filter(abol_filter_less,data)
    list_data = list(filter_data)
    #Less than 5 words and order  by points
    list_data.sort(reverse=True,key=order_points)
    print('\nLess than 5 words and order by points\n')
    for i in list_data:
        print(i[0],i[1],i[2],'points',i[3],'comments')