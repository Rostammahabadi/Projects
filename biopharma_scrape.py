from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import pandas as pd
import numpy as np
cat_date=[]
website = []
price=[]
disease=[]
stage=[]
ticker=[]
descriptions=[]
url= "https://www.biopharmcatalyst.com/calendars/fda-calendar"
response = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
web_page = urlopen(response).read()
page_soup = BeautifulSoup(web_page, "html.parser")
for date in page_soup.find_all(class_='filter-table__td js-td js-td--ticker js-td--stages js-td--indications js-td--fda js-td--portfolio js-catalyst-searchable'):
    cat_date2= date.get("data-catalyst-searchable")
    cat_date.append(cat_date2)
for href in page_soup.find_all(class_="filter-table__td js-td js-td--ticker js-td--stages js-td--indications js-td--fda js-td--portfolio js-catalyst-searchable"):
    value2= href.find_all('a',href=True)
    #attrs={'href':re.compile("^http://")})
    value= re.search("\"(.*?)\"",str(value2))
    value=value.group()
    website.append(value)
for prices in page_soup.find_all(class_="filter-table__td js-td js-td--price text-right"):
    grab_price= prices.get('data-value')
    price.append(float(grab_price))
for diseases in page_soup.find_all(class_="filter-table__td js-td js-td--ticker js-td--stages js-td--indications js-td--fda js-td--portfolio js-catalyst-searchable"):
    grab_disease = diseases.get('data-indications')
    disease.append(grab_disease)
for stages in page_soup.find_all(class_="filter-table__td js-td js-td--stage"):
    grab_stage=stages.get('data-value')
    stage.append(grab_stage)
for tickers in website:
    result= re.search("([A-Z])\w+",tickers)
    result2=result.group()
    ticker.append(result2)
stage_array=np.asarray(stage)
raw_data={'Ticker':ticker,
          'Price':price,
         'Stage':stage_array,
         'Disease':disease,
         'Website':website,
         'Catalyst Date':cat_date}
df=pd.DataFrame(data=raw_data,index=None)
def make_clickable(val):
    return '<a href="{}">{}</a>'.format(val,val)
for description in page_soup.find_all(class_="catalyst-note"):
    grab_descriptions= re.search("\>(.*?)(?=\<)",str(description))
    clean_descriptions= grab_descriptions.group()
    descriptions.append(clean_descriptions)
    #description.append(description1)
#print(soup.find_all(class_="filter-table__text-wrapper"))
# for description in soup.find_all(class_="catalyst-note"):
#     grab_description= description.
print(df)
