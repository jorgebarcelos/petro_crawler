from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from time import sleep
import pandas

def get_companies_data():
    """get companies data values"""

    header_options = Options()
    header_options.add_argument('--headless')

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), 
        options=header_options
        )

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

    data_values = {
        'companies': companies,
        'all_quotes': all_quotes,
        'date_hour': date_hour
    }

    return data_values


def create_excel(data_values, file_name):

    data_companies = pandas.DataFrame(data_values)
    data_companies.to_excel(file_name, index=False)


companies_data = get_companies_data()
create_file = create_excel(companies_data, './companies.xlsx')
