from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore
import time
from bs4 import BeautifulSoup # type: ignore
import re

def getCocktailUrls(driver):
    unforgettables_url = 'https://iba-world.com/category/iba-cocktails/the-unforgettables/' # 33 cocktails
    classics_url = 'https://iba-world.com/category/iba-cocktails/contemporary-classics/' # 31 cocktails
    new_era_url = 'https://iba-world.com/category/iba-cocktails/new-era-drinks/' # 25 cocktails

    driver.get('https://iba-world.com/')
    time.sleep(2.5)
    input_element = driver.find_element(By.CLASS_NAME, 'yes')
    input_element.click()

    all_drinks_sources = []

    for url in [unforgettables_url, classics_url, new_era_url]:
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html, features='lxml')
        all_drinks = soup.find_all(id=re.compile('^post-\d+'))
        for drink in all_drinks:
            source = drink.find('a').attrs['href']
            all_drinks_sources.append(source)

    return all_drinks_sources

def extractRecipes(driver, all_cocktail_urls):

    all_recipes = []
    for cocktail_url in all_cocktail_urls:
        driver.get(cocktail_url)
        html = driver.page_source
        soup = BeautifulSoup(html, features='lxml')
        class_element = soup.find('div', class_='et_pb_module et_pb_post_content et_pb_post_content_0_tb_body blog-post-content')
        p_elements  = class_element.find_all('p')
        info = []
        for p_element in p_elements:
            p_element_str = str(p_element)
            # TODO: fix the below line
            # p_element_str.insert(0, cocktail_url)
            info.append(p_element_str)
        
        cleaned_info = [i for i in info if '<strong>' not in i]
        all_recipes.append(cleaned_info)
    
    return all_recipes