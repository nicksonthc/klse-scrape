import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent() # fake user agent to simulate access from browser , else will get 403 error forbiden.

def scrapePage()-> BeautifulSoup :

    headers = {'Content-Type': 'application/json; charset=utf-8' ,  'User-Agent': ua.chrome}

    priceTargetUrl = 'https://klse.i3investor.com/jsp/stocks.jsp' # get url
    page = requests.get(priceTargetUrl , headers = headers) # connect to page
    html = page.content # get html content
    soup = BeautifulSoup(html, parser="html.parser") #beautify the html page

    return soup

def companyList(soup : BeautifulSoup)-> list :
    test4 = soup.find_all(id ="tablebody")
    companies_url = []

    for company in test4[0].contents :
        if company != ' ' :
            url = company.contents[1].contents[0].attrs['href']
            companies_url.append(url)

    print(companies_url)
    return companies_url 
    
    # resultsTest = soup.find(id='header')
    # results = soup.find('div', attrs={"id": "stockListingTable_wrapper"})
    # test3 = soup.find_all(id="main-content-cell")
    # print(results.prettify())



# Driver code
soup =  scrapePage()

companylist = companyList(soup)



