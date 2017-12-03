from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class productPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def orderProduct(self):
        for i in range(3):
            try:
                addArticelArt = driver.find_element_by_css_selector('.options [name="options[Size]"]').click()
                addArticelArtDropdown = driver.find_element_by_css_selector('.options [name="options[Size]"] [value="Medium"]').click()
            except:
                pass
        driver.find_element_by_css_selector(".quantity [type='submit']").click()

    def checkCartCounter(self):
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#cart .quantity'), str(i+1)))
        cartCounter = driver.find_element_by_css_selector('#cart .quantity')
        assert(cartCounter.text == str(1+i))