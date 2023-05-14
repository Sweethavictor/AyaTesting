from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import login
import noreceipt
website = "https://apistaging.net/"
PATH = "D:/PythonPrograms/Testing/chromedriver/chromedriver"

service = Service(executable_path=PATH)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

login_page = login.Login(website)
noreceipt_claim = noreceipt.NoReceipt()
success = login_page.login(driver, "qc+ayapostwsaemp2t2@ayapayments.com", "Test_test1" )
if success:
    #noreceipt_claim.submit_hsa_wsa(driver, True)
    #noreceipt_claim.submit_hsa_only(driver, True)
    noreceipt_claim.submit_wsa_only(driver, False)
    





