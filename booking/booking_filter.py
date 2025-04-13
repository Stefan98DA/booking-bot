# This file will contain a class with methods responsible for filtering the search

from selenium.webdriver.remote.webdriver import WebDriver # <-- optional step, helps with autocomplete suggestions
from selenium.webdriver.common.by import By
import time

class BookingFilter():
    def __init__(self, driver:WebDriver):
        self.driver = driver


    def apply_star_rating(self, *star_values):
        find_star_rating = self.driver.find_element(By.CSS_SELECTOR, "div[data-filters-group='class']")
        star_child_elements = find_star_rating.find_elements(By.CSS_SELECTOR, '*')
        
        for star_value in star_values:
             for star_element in star_child_elements:
                 if str(star_element.get_attribute('innerHTML')).strip() == f'{star_value} stars':
                     star_element.click()
            
        time.sleep(3) # website didn't have enough time to apply star rating before sorting from low to high
        # this is a quick fix, WebDriverWait would be an option also

    def sort_by_price_asc(self):

        click_sorting_button = self.driver.find_element(By.CSS_SELECTOR, "button[data-testid='sorters-dropdown-trigger']")
        click_sorting_button.click()

        lowest_first = self.driver.find_element(By.CSS_SELECTOR, "button[aria-label='Price (lowest first)']")
        lowest_first.click()

    