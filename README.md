[![pipeline status](https://gitlab.com/nicksonthc/klse-scrape/badges/master/pipeline.svg)](https://gitlab.com/nicksonthc/klse-scrape/-/commits/master)
[![coverage report](https://gitlab.com/nicksonthc/klse-scrape/badges/master/coverage.svg)](https://gitlab.com/nicksonthc/klse-scrape/-/commits/master)


## Introduction

This project objective is to acquire Malaysia KLSE bursa stock market's companies list and scraping through to obtain its financial detail by using python web scraping to help in decision making for stock picking.

1. The 1st step is to obtain all company list and url
2. Afterward 2nd step then we can scrape through every companies then obtain its current price and NTA 
3. Compute the company which current price is lower than its NTA and sort by % in descending order to get the most undervalue company by only comparing those 2 factor [NTA,CURRENT PRICE].

## Prerequisites

* [python](https://www.python.org/downloads/)

## Running the Application

    python main.py
    
## Testing

    F5 to run for debug mode.


## Output
1. You will get printed company url directories.
```
['/servlets/stk/7054.jsp', '/servlets/stk/5238.jsp', '/servlets/stk/7167.jsp', '/servlets/stk/7086.jsp', '/servlets/stk/2488.jsp', '/servlets/stk/7131.jsp', '/servlets/stk/0218.jsp', '/servlets/stk/5281.jsp', '/servlets/stk/7191.jsp', '/servlets/stk/7146.jsp', '/servlets/stk/0181.jsp', '/servlets/stk/6599.jsp', '/servlets/stk/5139.jsp', '/servlets/stk/5185.jsp', '/servlets/stk/5198.jsp', '/servlets/stk/7145.jsp', '/servlets/stk/7315.jsp', '/servlets/stk/7090.jsp', '/servlets/stk/0209.jsp', '/servlets/stk/5099.jsp', '/servlets/stk/5014.jsp', '/servlets/stk/2658.jsp', '/servlets/stk/7609.jsp', '/servlets/stk/5115.jsp', '/servlets/stk/5116.jsp', '/servlets/stk/2674.jsp', '/servlets/stk/1163.jsp', '/servlets/stk/5269.jsp', '/servlets/stk/1015.jsp', '/servlets/stk/5293.jsp', '/servlets/stk/0159.jsp', '/servlets/stk/5120.jsp', '/servlets/stk/1007.jsp', '/servlets/stk/7031.jsp', '/servlets/stk/6351.jsp', '/servlets/stk/7083.jsp', '/servlets/stk/4758.jsp', '/servlets/stk/0048.jsp', '/servlets/stk/0226.jsp', '/servlets/stk/6556.jsp', '/servlets/stk/5082.jsp', '/servlets/stk/9342.jsp', '/servlets/stk/5568.jsp', '/servlets/stk/5015.jsp', '/servlets/stk/6432.jsp', '/servlets/stk/0119.jsp', '/servlets/stk/7214.jsp', '/servlets/stk/7181.jsp', '/servlets/stk/7007.jsp', '/servlets/stk/5210.jsp', '/servlets/stk/5127.jsp', '/servlets/stk/0038.jsp', '/servlets/stk/1481.jsp', '/servlets/stk/0068.jsp', '/servlets/stk/7722.jsp', '/servlets/stk/7129.jsp', '/servlets/stk/4057.jsp', '/servlets/stk/0105.jsp', '/servlets/stk/7162.jsp', '/servlets/stk/6399.jsp', '/servlets/stk/0072.jsp', '/servlets/stk/8176.jsp', '/servlets/stk/7048.jsp', '/servlets/stk/5130.jsp', '/servlets/stk/7099.jsp', '/servlets/stk/8885.jsp', '/servlets/stk/5204.jsp', '/servlets/stk/7579.jsp', '/servlets/stk/6888.jsp', '/servlets/stk/5106.jsp', '/servlets/stk/7120.jsp', '/servlets/stk/2305.jsp', '/servlets/stk/5021.jsp', '/servlets/stk/7078.jsp']
```
