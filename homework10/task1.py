import asyncio
import json
import re

import aiohttp
from bs4 import BeautifulSoup as Bs


async def get_page_content(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def get_companies_list_page(num=1):
    url = f'https://markets.businessinsider.com/index/components/s&p_500?p=' \
          f'{num}'
    soup = await get_page_content(url)
    soup = Bs(soup, 'html.parser')
    table = soup.find_all('table')[0]
    # table_links = table.find_all('a', href=True)
    # return [(company.text, company.get('href')) for company in table_links]
    companies_list = []
    for row in table.find_all('tr')[1:]:
        name = row.find('a')['title']
        link = row.find('a')['href']
        growth = float(row.find_all('td')[-1].text.split()[-1].rstrip('%'))
        companies_list.append((name, link, growth))

    return companies_list


async def get_all_companies():
    companies_list = [await get_companies_list_page(page_num)
                      for page_num in range(1, 12)]
    return [company for item in companies_list for company in item]


async def get_exchange_rate(url='https://www.cbr.ru/scripts/XML_daily.asp?'):
    soup = await get_page_content(url)
    soup = Bs(soup, 'html.parser')
    rate = soup.find('valute', {'id': "R01235"}).value.text.replace(',', '.')
    return float(rate)


async def get_company_data(company, ex_rate=1.0):
    name = company[0]
    link = company[1]
    growth = company[2]
    url = f'https://markets.businessinsider.com{link}'
    soup = await get_page_content(url)
    soup = Bs(soup, 'html.parser')

    # price $
    current_price = soup.find('span',
                              {'class': 'price-section__current-value'})
    current_price = float(current_price.text.replace(',', ''))
    rub_price = round(current_price * ex_rate, 2)

    # Company code
    code = soup.find('span',
                     {'class': 'price-section__category'}).span.text
    code = code.strip(', ')

    # P/E
    try:
        pe_ratio = soup.find('div', string='P/E Ratio').parent.text
        pe_ratio = float(re.findall('\\d*[.]\\d*', pe_ratio)[0])
    except AttributeError:
        pe_ratio = 0

    # 52 week low
    try:
        low = soup.find('div', string='52 Week Low').parent.text
        low = float(re.findall('\\d*[.]\\d*', low)[0])
    except AttributeError:
        low = 0

    # 52 week high
    try:
        high = soup.find('div', string='52 Week High').parent.text
        high = float(re.findall('\\d*[.]\\d*', high)[0])
    except AttributeError:
        high = 0

    summary = dict()
    summary['name'] = name
    summary['price'] = rub_price
    summary['code'] = code
    summary['PE_ratio'] = pe_ratio
    summary['annual_range'] = round((high - low) * ex_rate, 2)
    summary['growth'] = growth
    return summary


async def event_loop():
    result = []
    exchange_rate = await get_exchange_rate()
    for company in await get_all_companies():
        result.append(await get_company_data(company, exchange_rate))
    return result


def find_top_10(companies_list, rating_type):
    return sorted(companies_list, key=lambda x: x[rating_type],
                  reverse=True)[:10]


def save_file(top_list, rating):
    with open(f'{rating}.json', 'w') as f:
        json.dump(top_list, f)


if __name__ == '__main__':
    companies = asyncio.run(event_loop())
    ratings = ['price', 'PE_ratio', 'annual_range', 'growth']
    for r in ratings:
        save_file(find_top_10(companies, r), r)
