from selenium import webdriver
from selenium.webdriver.common. by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time




        
def load_and_accept_cookies():
        URL = "https://www.zoopla.co.uk/new-homes/property/london/?q=London&results_sort=newest_listings&search_source=new-homes&page_size=25&pn=1&view_type=list"
        driverpath = '/Users/apple/Documents/GitHub/DC_Zoopla/chromedriver 5'
        service = Service(driverpath)
        chrome_options = Options()
        driver = webdriver.Chrome(options=chrome_options, service=service) 
        driver.get(URL)
        time.sleep(3)
        try:
                driver.switch_to_frame('gdpr-consent-notice') # This is the id of the frame
                accept_cookies_button = driver.find_elementh(by=By.XPATH, value='//*[@id="save"]')
                accept_cookies_button.click()
                time.sleep(2)
                driver.switch_to.default_content()
                
        except AttributeError: 
                driver.switch_to.frame('gdpr-consent-notice') # This is the id of the frame
                accept_cookies_button = driver.find_element(by=By.XPATH, value='//*[@id="save"]')
                accept_cookies_button.click()
                time.sleep(2)
                driver.switch_to.default_content()
        
        except:
                pass
                
        return driver

        
time.sleep(2)

        
def get_links(driver: webdriver.Chrome):
        prop_container = driver.find_element(by=By.XPATH, value='//div[@class="css-1itfubx ee416nz0"]')  
        prop_list = prop_container.find_elements(by=By.XPATH, value='./div')
        link_list = []
                
        for house_property in prop_list:
                a_tag = house_property.find_element(by=By.TAG_NAME, value='a')
                link = a_tag.get_attribute('href')
                link_list.append(link)
                print(f'There are {len(link_list)} properties in this page')
                print(link_list)

                return link_list
        
        big_list = []

        
        for i in range(1): # The first 5 pages only
                big_list.extend(get_links(driver))
                next_button = driver.find_element(by=By.XPATH, value='//li[@class="css-qhg1xn-PaginationItemPreviousAndNext-PaginationItemNext eaoxhri2"]')
                next_button.click()  
                time.sleep(5)       
                 # Call the function we just created and extend the big list with the returned list
                ## TODO: Click the next button. Don't forget to use sleeps, so the website doesn't suspect
                # pass # This pass should be removed once the code is complete

        for link in big_list:
                dict_properties = {'Price': [], 'Address': [], 'Bedrooms': [], 'Description': []}
                price = driver.find_element(by=By.XPATH, value='//p[@data-testid="price"]').text
                dict_properties['Price'].append(price)
                address = driver.find_element(by=By.XPATH, value='//address[@data-testid="address-label"]').text
                dict_properties['Address'].append(address)
                bedrooms = driver.find_element(by=By.XPATH, value='//div[@class="c-PJLV c-PJLV-iiNveLf-css"]').text
                dict_properties['Bedrooms'].append(bedrooms)
                div_tag = driver.find_element(by=By.XPATH, value='//div[@data-testid="truncated_text_container"]')
                span_tag = div_tag.find_element(by=By.XPATH, value='.//span')
                description = span_tag.text
                dict_properties['Description'] = description
                print(dict_properties)

        ## TODO: Visit all the links, and extract the data. Don't forget to use sleeps, so the website doesn't suspect
        pass # This pass should be removed once the code is complete

        driver.quit() # Close the browser when you finish

load_and_accept_cookies()

        





           








     


