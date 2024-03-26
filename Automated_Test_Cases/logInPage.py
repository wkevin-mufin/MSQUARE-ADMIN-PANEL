import sys
import time
from selenium import webdriver
import subprocess

from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from Config import configs
from Config.configs import filePathToTestcases
from shared_files import xlsUtils

chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
siteport =configs.urlToAdminPOrtal #"https://dev-admin.msq.market/"
expected_title = "Sign in to your"
sheetname = "login"
logintestcase = "MSQA_Admin_LoginTestcase.xlsx"
filePath = (f"{filePathToTestcases}{logintestcase}")
rows = xlsUtils.getRowCount(filePath, sheetname)




for r in range(2, rows + 1):
    driver.get(siteport)
    driver.maximize_window()
    time.sleep(5)
    username = xlsUtils.readDAta(filePath, sheetname, r, 6)
    password = xlsUtils.readDAta(filePath, sheetname, r, 7)

    driver.find_element("id", "input_login_email").send_keys(username)
    driver.find_element("id", "input_login_password").send_keys(password)
    driver.find_element("id", "btn_login_sign_in").click()
    print("button")
    time.sleep(5)

    # checking if the user lands in the correct page.
    # LogIn_title_id = driver.find_element("id","ContentPlaceHolder1_LblWelcomeTo")
    # LogIn_title_id_txt = LogIn_title_id.text
    try:
        LogIn_title_id = driver.find_element("id", "app-header")
        print("Log In successflly test1.")
        xlsUtils.writeData(filePath, sheetname, r, 9, "Log In successfully.")
        xlsUtils.writeData(filePath, sheetname, r, 10, "passed")
        xlsUtils.writeData(filePath, sheetname, r, 12, "its okay")
        time.sleep(2)
        driver.find_element("id","btn_popover_app_layout").click()
        time.sleep(2)
        # Find the "Settings" button by its XPath
        delete_button = driver.find_element(By.XPATH, "//li[contains(., 'Logout')]")

        # Click the delete button
        delete_button.click()
    except NoSuchElementException:
        print("Log In Failed.")
        xlsUtils.writeData(filePath, sheetname, r, 9, "Log In Failed")
        xlsUtils.writeData(filePath, sheetname, r, 10, "FAILED")
        xlsUtils.writeData(filePath, sheetname, r, 12, "Analyse Before approaching developer")
        time.sleep(2)

    if r == 7:
        print("subprocess has been accessed")
        driver.quit()
        #subprocess.run(['python', 'demoQuote.py'])

    else:
        driver.get(siteport)
        time.sleep(5)
#driver.quit()
# subprocess.run(['python', 'loginToTest.py'])
print("print tulipass")