import booking.constants as const
from booking.booking_filter import BookingFilter 
from booking.bookin_report import BookingReport
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from prettytable import PrettyTable


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r";C:/SeleniumDrivers/chromedriver-win64", teardown=False,):
        self.teardown = teardown
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path

        # Setup Chrome options
        banana = Options()
        banana.add_experimental_option("excludeSwitches", ["enable-logging"])
        banana.add_experimental_option("detach", True)

        super(Booking, self).__init__(options=banana)
        self.implicitly_wait(15)
        self.maximize_window()

        


    def __exit__(self, exc_type, exc, traceback):
        if self.teardown:
            self.quit()
    



    def land_first_page(self):
        self.get(const.BASE_URL)
        #self.handle_popups()

    def change_currency(self, currency='EUR'):
        #self.handle_popups()
        currency_element = self.find_element(By.CSS_SELECTOR, "button[data-testid = 'header-currency-picker-trigger']")
        currency_element.click()
        
        # Select currency, default currency will be EUR
        selected_currency_element = self.find_element(By.XPATH, f"//div[contains(@class, ' CurrencyPicker_currency') and text()= '{currency}']")
        selected_currency_element.click()
    
    def select_destination(self, city):
        #self.handle_popups()
        
        destination = self.find_element(By.NAME, "ss")
        destination.clear() # Clears the search field
        destination.send_keys(city)
    #    dropdown = self.find_element(By.ID, "autocomplete-result-0")
    #    dropdown.click()
        try:
            popup = self.find_element(By.CSS_SELECTOR, "button[aria-label='Dismiss sign-in info.']")
            popup.click()
            print("Popup was closed.")
        except:
            print("No popup was found, skipping...")

    def select_dates_box(self):
        dates = self.find_element(By.CSS_SELECTOR, "button[data-testid='searchbox-dates-container']")
        dates.click()
        
    def select_dates(self,check_in, check_out):
        check_in_date = self.find_element(By.XPATH, f'//td[./span[@data-date="{check_in}"]]')
        check_in_date.click()
        check_out_date = self.find_element(By.XPATH, f'//td[./span[@data-date="{check_out}"]]')
        check_out_date.click()

    def select_persons(self, adults=2, rooms=None):
        persons_box = self.find_element(By.CSS_SELECTOR, "button[data-testid='occupancy-config']")
        persons_box.click()
        
        decrease_button = self.find_element(By.XPATH,"//button[@aria-hidden='true' and contains(@class, 'a83ed08757')]")
        while decrease_button.is_enabled():
            decrease_button.click()
            # print("Clicked the '-' button")  just to follow the flow in terminal
            decrease_button = self.find_element(By.XPATH, "//button[@aria-hidden='true' and contains(@class, 'a83ed08757')]")
    
        #  print("Button is disabled, continuing.")  just to follow the flow in terminal

        increase_button = self.find_element(By.XPATH, "//button[@aria-hidden='true' and contains(@class, 'f4d78af12a')]")
        
        for _ in range(1, adults):
            increase_button.click()
            
    def search_button(self):
        search_button = self.find_element(By.CSS_SELECTOR, "button[type='submit']")
        search_button.click()

    
    def apply_filters(self):
        filter = BookingFilter(driver=self)
        
        filter.apply_star_rating(3,4,5)
        filter.sort_by_price_asc()
    

    def report_results(self):
        hotel_list =self.find_element(By.CLASS_NAME, "d4924c9e74"
                          )
        
        report = BookingReport(hotel_list)
        table = PrettyTable(
            table_type = ["Hotel Name", "Hotel Score"]
        )
        table.add_rows(report.pull_hotel_attributes())
        print(table)
    
