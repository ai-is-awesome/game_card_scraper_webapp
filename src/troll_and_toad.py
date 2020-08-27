from bs4 import BeautifulSoup

from src.requests_module import Request

from bs4 import BeautifulSoup as bs



def get_details(soup):
    cards = soup.find_all('div', class_ = 'card h-100 p-3')
    for card in cards:
        product_info = card.find_all('div', class_ = 'product-info')[0]
        product_info.find('div', class_ = 'prod-title').text.strip('\n')
        product_link = product_info.find('div', class_ = 'prod-title').a['href']
        




def query_formatter(query):
    query = query.replace(' ', '+')
    query = query.replace('&', '%26')
    return query





def get_search_url(query):
    origin = 'https://www.trollandtoad.com'
    search = 'https://www.trollandtoad.com/category.php?selected-cat=0&search-words={}'
    formatted_query = query_formatter(query)
    print(search.format(formatted_query))
    return search.format(formatted_query)



def get_soup(url):
    print("getting request")
    resp = Request.get(url)
    print("got the request!")
    soup = BeautifulSoup(resp.text, 'lxml')
    return soup





def scrape(soup):
    L = list()
    cards = soup.find_all('div', class_ = 'card h-100 p-3')
    for card in cards:
        D = {'product_title' : None, 'product_link' : None, 'product_category' : None, 'condition' : None, 'price' : None}
        product_info = card.find_all('div', class_ = 'product-info')[0]
        if product_info:
            D['product_title'] = product_info.find('div', class_ = 'prod-title').text.strip('\n')
            D['product_link'] = product_info.find('div', class_ = 'prod-title').a['href']
        
        D['product_category'] = card.find('div', class_ = 'prod-cat').text
        
        # More details
        buying_options = card.find('div', class_ = 'buying-options-container')
        details = buying_options.find('div', class_ = 'position-relative')
        for detail, i in zip(details.find_all('div', class_ = 'p-1'), range(len(details))):
            if i == 1:                
                D['condition'] = detail.a.text if detail.a else None

            if i == 3:
                D['price'] = detail.text if detail.text else None
        L.append(D)
                
    return L


def main(query):
    print("getting url")
    url = get_search_url(query)
    print("getting soup")
    soup = get_soup(url)
    print("running scraper")
    results = scrape(soup)
    return results




