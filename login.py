from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Login():
    def __init__(self, website) -> None:
        self.success = False
        self.website = website
    
    def login(self, driver, user_name, password_txt):
        driver.get(self.website)
        driver.implicitly_wait(10)
        email = driver.find_element(by="name", value="email")
        email.send_keys(user_name)
        loginButton = driver.find_element(by=By.CLASS_NAME, value="sc-bBXxYQ.hlpCAH")
        loginButton.click()
        password = driver.find_element(by="name", value="password")
        password.send_keys(password_txt)
        loginButton2 = driver.find_element(by = By.CLASS_NAME, value="sc-bBXxYQ.hlpCAH")
        loginButton2.click()
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "sc-fLlhyt.ccTQNX"))
            )
            #print(element.text)
            self.success = True
        except Exception as e:
            self.success = False
        if self.success:
            print("Logged In Successfully")
        else:
            print("Failure in logging in")
        return self.success

    