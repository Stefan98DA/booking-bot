# This file is going to include method that will print
# The data from the first 25 deals

from selenium.webdriver.remote.webdriver import WebDriver # <-- optional step, helps with autocomplete suggestions
from selenium.webdriver.common.by import By


class BookingReport:
    def __init__(self, boxes_section_element:WebDriver):
        self.boxes_section_element = boxes_section_element
    


    def pull_hotel_attributes(self):
        hotel_cards = self.boxes_section_element.find_elements(By.CSS_SELECTOR, "div[data-testid='property-card']")
        extracted_data = []

        for card in hotel_cards:
            # Hotel name
            
            name_elements = card.find_element(By.CSS_SELECTOR, "div[data-testid='title']")
            name = name_elements.text.strip() if name_elements else "N/A"


            # Hotel score
            hotel_scores = card.find_element(By.XPATH, ".//div[contains(@class, 'ac4a7896c7') and contains(text(), 'Scored')]")
            score = hotel_scores.text.strip() if hotel_scores else "N/A"
            
            # the code was previously displaying Scored 6.5 for all results
            # the solution is in the dot '.' before //div which instructs the program to 
            # START SEARCHING FROM THIS CURRENT ELEMENT (hotel name) and not from the top of the page


            # Hotel price
            
            hotel_prices = card.find_element(By.CSS_SELECTOR, "span[data-testid='price-and-discounted-price']")
            price = hotel_prices.text.strip() if hotel_prices else "N/A"
        


            extracted_data.append([name, score, price])

        return extracted_data
      
