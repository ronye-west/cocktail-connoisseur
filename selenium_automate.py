from selenium import webdriver # type: ignore
from selenium.webdriver import Firefox # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from bs4 import BeautifulSoup # type: ignore
import time
import re
import helper

try:
    driver = webdriver.Firefox()
    all_cocktail_urls = helper.getCocktailUrls(driver)
    all_cocktail_recipes = helper.extractRecipes(driver, all_cocktail_urls)
    print(all_cocktail_recipes)
    print(len(all_cocktail_recipes))
    print('PASSED')
    driver.quit()
except:
    print('FAILED')
    driver.quit()

