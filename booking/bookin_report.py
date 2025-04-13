# This file is going to include method that will print
# The data from the first 25 deals

from selenium.webdriver.remote.webdriver import WebDriver # <-- optional step, helps with autocomplete suggestions
from selenium.webdriver.common.by import By


class BookingReport:
    def __init__(self, boxes_section_element:WebDriver):
        self.boxes_section_element = boxes_section_element
    


    def pull_hotel_attributes(self):
        hotel_names = self.boxes_section_element.find_elements(By.CSS_SELECTOR, "div[data-testid='title']")

        extracted_attributes = []
        for name in hotel_names:
           hotel_name =name.get_attribute('innerHTML').strip()
           hotel_score = self.boxes_section_element.find_element(By.XPATH, "//div[contains(@class, 'ac4a7896c7') and contains(text(), 'Scored')]").get_attribute('innerHTML').strip()
           extracted_attributes.append(
               [hotel_name,hotel_score]
           )
        return extracted_attributes
          # print(f'{hotel_name} --')
           #extracted_names.append(hotel_name)
        #return extracted_names
    
