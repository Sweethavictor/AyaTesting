from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import logging

class NoReceipt():
    def __init__(self):
        self.success = False
    
    def submit(self, driver):
        submit_claim_btn = driver.find_element(By.CLASS_NAME, "sc-bjUoiL.leXMUQ")
        time.sleep(5)
        submit_claim_btn.click()
        no_recipt = driver.find_element(By.CLASS_NAME, "ClaimSubmission_text__cNzhv")
        time.sleep(5)
        no_recipt.click()
        continue_btn = driver.find_element(By.CLASS_NAME, "sc-bBXxYQ.hlpCAH")
        time.sleep(5)
        continue_btn.click()
        online_btn = driver.find_element(By.XPATH, "//*[@id='root']/div/div/div/div[2]/div/div[2]/div/div[2]/button[2]")
        time.sleep(5)
        online_btn.click()
        merchant_input = driver.find_element(By.NAME, "merchantWebsite")
        merchant_input.send_keys("test.com")
        date_input = driver.find_element(By.NAME, "date")
        date_input.send_keys("03/03/2023")
        total_paid = driver.find_element(By.NAME, "totalPaid")
        total_paid.send_keys("1")
        time.sleep(5)
        claim_amount = driver.find_element(By.NAME, "amountToClaim")
        claim_amount.send_keys("1")
        time.sleep(5)
        claim_submit_btn = driver.find_element(By.XPATH, "//*[@id='root']/div/div/div/div[2]/div/div[2]/div/div[3]/button[1]")
        claim_submit_btn.click()
        time.sleep(10)
        wellness_btn = driver.find_element(By.XPATH,"//*[contains(text(),'Wellness')]")
        wellness_btn.click()
        time.sleep(25)
        print("dropdown")
        #drop_down=driver.find_element(By.XPATH, "(//div[@class='rw-dropdown-list-input'])[1]")
        #drop_down.click()
        select = Select(driver.find_element(By.XPATH, "(//div[@class='rw-dropdown-list-input'])[1]"))
        select.select_by_visible_text('Wellness Spending')
        time.sleep(15)
        item_Amount=driver.find_element(By.XPATH, "//input[@name='claimItems.0.amountPaid']")
        item_Amount.send_keys("2.00")
        time.sleep(10)
        select = Select(driver.find_element(By.XPATH, "(//div[@class='rw-dropdown-list-input'])[2]"))
        select.select_by_visible_text('Dependent')
        time.sleep(15)
        

        '''drop.select_by_value("Wellness Spending")'''
        
        '''spend_category = driver.find_element(By.CSS_SELECTOR, ".rw-dropdown-list-value")
        #//*[@id="ClaimSubmission_dropdownContainerStyle__1dMIR_input"]/div[1]/span/svg
        spend_category.click()
       
        wellness_spending = driver.find_element(By.CLASS_NAME, "ClaimSubmission_p_text__2XUfy")
        wellness_spending.click()
        sub_well_spending = driver.find_element(By.XPATH, "//*[@id='ClaimSubmission_dropdownContainerStyle__1dMIR_input']/div[1]/span/svg")
        sub_well_spending.click()
        sub_well_spending_drop = driver.find_element(By.XPATH, "//*[@id='ClaimSubmission_dropdownContainerStyle__1dMIR_listbox']/div[1]/p")
        sub_well_spending_drop.click()
        drop_down = driver.find_element(By.XPATH, "//body/div[@id='root']/div[@class='fonts_defaultFont__O2COt']/div/div[@class='container']/div[@class='container__inner']/div[@class='ClaimSubmission_cardContainer__3VmfR']/div[@class='ClaimSubmission_cardBox__tfnSG']/div[@class='ClaimSubmission_add_receipt__1VQET']/form[@action='#']/div/div[@class='ClaimSubmission_dropdown_container__2Y4Xd']/div[1]/div[1]/div[1]/span[1]")
        drop_down.click()'''