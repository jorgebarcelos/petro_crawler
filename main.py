from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
from time import sleep


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://economia.uol.com.br/cotacoes/bolsas/')

companies = ['PETR3.SA', 'MGLU3.SA', 'VIVT3.SA']
all_quotes = list()
date_hour = list()

for company in companies:
    input_search = driver.find_element(By.ID, 'filled-normal')
    input_search.send_keys(company)
    sleep(3)
    input_search.send_keys(Keys.ENTER)
    sleep(3)
    span_value = driver.find_element(By.XPATH, '//span[@class="chart-info-val ng-binding"]')
    quote_value = span_value.text
    all_quotes.append(quote_value)
    date_hour.append(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
    # print(f'Quote value for {company}: {quote_value}')
print(companies, all_quotes, date_hour)